import pandas as pd
#**********
fishbase_tidy = pd.read_csv('../data/fishbase_joined.csv')

def calc_GRAR740102(seq):
    seq = "".join([letter for letter in seq if letter != 'X'])
    aa_prop = {'A':8.1, 'R':10.5, 'N':11.6, 'M':5.7, 'G':9.0, 'H':10.4, 'D': 13.0, 'C':5.5, 
              'Q':10.5, 'E':12.3, 'I':5.2, 'L':4.9, 'K':11.3, 'F':5.2, 'P':8.0, 'S':9.2, 
              'T':8.6, 'W':5.4, 'Y':6.2, 'V':5.9}
    values = []
    for aa in seq:
        values.append(aa_prop[aa])
    return sum(values)/len(values)

def calc_JURD980101(seq):
    seq = "".join([letter for letter in seq if letter != 'X'])
    aa_prop = {"A": 1.1, "R": -5.1, "N": -3.5,
               "H": -3.2, "G": -0.64, "M": 1.9,
               "D": -3.6, "C": 2.5, "Q": -3.68, 
               "E": -3.2, "H": -3.2, "I": 4.5,
               "L": 3.8, "K": -4.11, "F": 2.8,
               "P": -1.9, "S": -0.5, "T": -0.7, 
               "W": -0.46, "Y": -1.3, "V": 4.2}
    values = []
    for aa in seq:
        values.append(aa_prop[aa])
    return sum(values)/len(values)

def calc_KLEP840101 (seq):
    seq = "".join([letter for letter in seq if letter != 'X'])
    aa_prop = {"A": 0.0, "R": 1.0, 
               "N": 0.0, "D": -1.0,
               "C": 0.0, "Q": 0.0,
              "E": -1.0, "G": 0.0,
              "H": 0.0, "I": 0.0,
              "L": 0.0, "K": 1.0,
              "M": 0.0, "F": 0.0,
              "P": 0.0, "S": 0.0,
              "T": 0.0, "W": 0.0,
              "Y": 0.0, "V": 0.0}
    values = []
    for aa in seq:
        values.append(aa_prop[aa])
    return sum (values)/len(values)

def calc_KRIW790103 (seq):
    seq = "".join([letter for letter in seq if letter != 'X'])
    aa_prop = {"A": 27.5, "R" : 105, "N" : 58.7, "D" : 40, "C" : 44.6, "Q" : 80.7, "E" : 62, "G" : 0, "H" : 79, "I" : 93.5, "L" : 93.5, "K" : 100, "M" : 94.1, "F" : 115.5, "P" : 41.9, "S" : 29.3, "T" : 51.3, "W" : 145.5, "Y" : 117.3, "V" : 71.5} 
    values = []
    for aa in seq:
        values.append(aa_prop[aa])
    return sum(values)/len(values)

fishbase_tidy['CO1_polarity'] = fishbase_tidy["COI_sequence"].apply(calc_GRAR740102)
fishbase_tidy['CO1_hydrophobicity'] = fishbase_tidy["COI_sequence"].apply(calc_JURD980101)
fishbase_tidy['CO1_netcharge'] = fishbase_tidy["COI_sequence"].apply(calc_KLEP840101)
fishbase_tidy['CO1_sidechainvolume'] = fishbase_tidy["COI_sequence"].apply(calc_KRIW790103)
fishbase_tidy.drop('Unnamed: 0', axis = 1, inplace = True)

fishbase_tidy.to_csv('../data/fishbase_tidy_aaprop.csv')

