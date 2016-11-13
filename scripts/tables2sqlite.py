### * Description

# Store the tab-separated tables into a single SQLite database

# Input: fishbase_table.tsv
#        compilation_*.tsv


### * Parameters

FISHBASE_TEMP_TSV = "../data/fishbase_temperature.tsv"
FISHBASE_ENV_TSV = "../data/fishbase_environment.tsv"
FISHBASE_DATA_TSV = "../data/fishbase_extra_data.tsv"
COI_TSV = "../data/compilation_COI.tsv"
CYTB_TSV = "../data/compilation_cytB.tsv"
ND5_TSV = "../data/compilation_ND5.tsv"

### * Import

import os
import sqlite3 as sql
import pandas as pd

### * Run

### ** Create an SQLite connection to a database file

# Delete the database file if it already exists
if os.path.isfile("../data/fish-prot-evolution.sqlite") :
    os.remove("../data/fish-prot-evolution.sqlite")
con = sql.connect("../data/fish-prot-evolution.sqlite")

### ** Load and save Fishbase data

fishbase_temp = pd.read_table(FISHBASE_TEMP_TSV, sep = "\t")
fishbase_temp.to_sql("fishbase_temperature", con)
fishbase_env = pd.read_table(FISHBASE_ENV_TSV, sep = "\t")
fishbase_env.to_sql("fishbase_environment", con)
fishbase_data = pd.read_table(FISHBASE_DATA_TSV, sep = "\t")
fishbase_data.to_sql("fishbase_extra_data", con)

### ** Load and save COI data

COI = pd.read_table(COI_TSV, sep = "\t")
COI.to_sql("seq_COI", con)

### ** Load and save cytB data

cytB = pd.read_table(CYTB_TSV, sep = "\t")
cytB.to_sql("seq_CYTB", con)

### ** Load and save ND5 data

ND5 = pd.read_table(ND5_TSV, sep = "\t")
ND5.to_sql("seq_ND5", con)

### ** Commit and close database connection

con.commit()
con.close()
