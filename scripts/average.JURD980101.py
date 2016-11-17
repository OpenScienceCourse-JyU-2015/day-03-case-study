
# coding: utf-8

# In[53]:

def calc_JURD980101(seq):
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

