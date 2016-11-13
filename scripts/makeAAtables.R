### * Description

# Extract some amino acid property tables from the AAindex dataset (from the
# seqinr R package) and store them into a SQLite database

### * Packages

library(seqinr)
data(aaindex)
library(RSQLite)

### * Parameters

aaCode = cbind(
    c("Arg", "His", "Lys", "Asp", "Glu",
      "Ser", "Thr", "Asn", "Gln", "Cys",
      "Gly", "Pro", "Ala", "Val", "Ile",
      "Leu", "Met", "Phe", "Tyr", "Trp"),
    c("R", "H", "K", "D", "E",
      "S", "T", "N", "Q", "C",
      "G", "P", "A", "V", "I",
      "L", "M", "F", "Y", "W")
)

# Mapping from three-letter to one-letter code
aaMapping = list()
for (i in 1:nrow(aaCode)) {
    aaMapping[[aaCode[i, 1]]] = aaCode[i, 2]
}

### * Functions

### ** extractProperties(ref)

extractProperties = function(ref) {
    #' @examples extractProperties("JURD980101")
    d = aaindex[[ref]]
    out = data.frame(aa = unlist(aaMapping[names(d$I)]), value = d$I)
    return(out)
}

### ** saveProperties(ref, filename)

saveProperties = function(ref, filename) {
    prop = extractProperties(ref)
    write.table(prop, file = filename, col.names = T, row.names = F,
                sep = "\t", quote = F)
}

### * Run

refs = c("JURD980101", "GRAR740102", "BHAR880101", "KRIW790103",
    "KLEP840101", "RADA880107", "PUNT030102", "DESM900102")

# Remove the database file if exists
if (file.exists("../data/aa_properties.sqlite")) {
    file.remove("../data/aa_properties.sqlite")
}

# Open the database connection
con = dbConnect(SQLite(), "../data/aa_properties.sqlite")

# Save the tables
for (ref in refs) {
    out = extractProperties(ref)
    dbWriteTable(con, ref, out, row.names = FALSE)
}

# Close the connection
dbDisconnect(con)
