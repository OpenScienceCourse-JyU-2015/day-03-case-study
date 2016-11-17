def calc_KRIW790103 (seq):
    aa_prop = {"A": 27.5, "R" : 105, "N" : 58.7, "D" : 40, "C" : 44.6, "Q" : 80.7, "E" : 62, "G" : 0, "H" : 79, "I" : 93.5, "L" : 93.5, "K" : 100, "M" : 94.1, "F" : 115.5, "P" : 41.9, "S" : 29.3, "T" : 51.3, "W" : 145.5, "Y" : 117.3, "V" : 71.5} 
    values = []
    for aa in seq:
        values.append(aa_prop[aa])
    return sum(values)/len(values)



