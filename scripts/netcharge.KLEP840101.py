
# coding: utf-8

# In[42]:

def calc_KLEP840101 (seq):
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

