
# coding: utf-8

# In[36]:

def calc_BHAR880101(seq):
    aa_prop = {"A": 0.357, "R": 0.529, 
               "N": 0.463, "M": 0.295, 
               "H": 0.323, "G": 0.544,
               "D": 0.511, "C": 0.346,
               "Q": 0.493, "E": 0.497,
               "I": 0.462, "L": 0.365,
               "K": 0.466, "F": 0.314,
               "P": 0.509, "S": 0.507,
               "T": 0.444, "W": 0.305,
               "Y": 0.42, "V": 0.386}
    values = []
    for aa in seq:
        values.append(aa_prop[aa])
    return sum(values)/len(values)

