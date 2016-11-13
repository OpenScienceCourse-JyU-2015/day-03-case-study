### * Description

# Split the Fishbase table into several tables for pedagogical purposes

### * Import

import os
import random
import pandas as pd

### * Parameters

FISHBASE_TSV = "../data/fishbase_table.tsv"
TEMPERATURE_TSV = "../data/fishbase_temperature.tsv"
ENVIRONMENT_TSV = "../data/fishbase_environment.tsv"
EXTRA_DATA_TSV = "../data/fishbase_extra_data.tsv"

### * Run

# Load the original Fishbase table
fb = pd.read_table(FISHBASE_TSV, sep = "\t")

# Split the Fishbase table into three tables
temp = fb.loc[:, ["species", "temperature_min", "temperature_max", "climate", "environment"]]
environment = fb.loc[:, ["species", "climate", "environment", "depth_min", "depth_max"]]
extra_data = fb.loc[:, ["species", "metabolism_data", "speed_data", "gill_area_data"]]

# Shuffle the rows
# http://stackoverflow.com/questions/1022141/best-way-to-randomize-a-list-of-strings-in-python
temp = temp.iloc[random.sample(range(len(fb)), len(fb))]
environment = environment.iloc[random.sample(range(len(fb)), len(fb))]
extra_data = extra_data.iloc[random.sample(range(len(fb)), len(fb))]

# Save the three new tables
temp.to_csv(TEMPERATURE_TSV, sep = "\t", index = False)
environment.to_csv(ENVIRONMENT_TSV, sep = "\t", index = False)
extra_data.to_csv(EXTRA_DATA_TSV, sep = "\t", index = False)
