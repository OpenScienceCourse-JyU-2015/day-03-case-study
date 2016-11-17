# coding: utf-8
# Importing relevant libraries
import pandas as pd
import sqlite3

# Create a connection and a cursor for querying
conn = sqlite3.connect("../data/fishbase_data.sqlite")
c = conn.cursor()

# Read tables from database. Note! sequence tables contain duplicates, use .drop_duplicates- method to get only one sequence per species
fishbase_env = pd.read_sql_query("SELECT species, climate, environment, depth_min, depth_max FROM fishbase_environment", conn)
fishbase_env.shape

fishbase_temp = pd.read_sql_query("SELECT species, temperature_min, temperature_max FROM fishbase_temperature", conn)
fishbase_temp.shape

seq_COI = pd.read_sql_query("SELECT species, sequence AS COI_sequence FROM seq_COI", conn)
seq_COI.drop_duplicates('species', inplace = True)

seq_CYTB = pd.read_sql_query("SELECT species, sequence AS CYTB_sequence FROM seq_CYTB", conn)
seq_CYTB.drop_duplicates('species', inplace = True)

seq_ND5 = pd.read_sql_query("SELECT species, sequence AS ND5_sequence FROM seq_ND5", conn)
seq_ND5.drop_duplicates('species', inplace = True)

# It is good practice to close the connection to the database once we have finished using it
conn.close()

# Join tables
fishbase_joined = pd.merge(fishbase_env, fishbase_temp, on = 'species', how = 'inner')
fishbase_joined = pd.merge(fishbase_joined, seq_COI, on = 'species', how = 'inner')
fishbase_joined = pd.merge(fishbase_joined, seq_CYTB, on = 'species', how = 'inner')
fishbase_joined = pd.merge(fishbase_joined, seq_ND5, on = 'species', how = 'inner')

# Write joined table as csv file
fishbase_joined.to_csv('../data/fishbase_joined.csv')
