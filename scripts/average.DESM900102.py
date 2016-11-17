
# coding: utf-8

# In[50]:

def calc_DESM900102 (seq):
    aa_prop = {"A": 1.26, "M": 1.52,
               "R": 0.38, "H": 1   ,
               "G": 1.08, "N": 0.59,
               "D": 0.27, "C": 1.6 ,
               "Q": 0.39, "E": 0.23,
               "I": 1.44, "L": 1.36,
               "K": 0.33, "F": 1.46,
               "P": 0.54, "S": 0.98,
               "T": 1.01, "W": 1.06,
               "Y": 0.89, "V": 1.33}
    values = []
    for aa  in seq:
        values.append(aa_prop[aa])
    return sum(values)/len(values)

