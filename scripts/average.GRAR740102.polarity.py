
# coding: utf-8

# In[32]:

def calc_GRAR740102(seq):
    aa_prop = {'A':8.1, 'R':10.5, 'N':11.6, 'M':5.7, 'G':9.0, 'H':10.4, 'D': 13.0, 'C':5.5, 
              'Q':10.5, 'E':12.3, 'I':5.2, 'L':4.9, 'K':11.3, 'F':5.2, 'P':8.0, 'S':9.2, 
              'T':8.6, 'W':5.4, 'Y':6.2, 'V':5.9}
    values = []
    for aa in seq:
        values.append(aa_prop[aa])
    return sum(values)/len(values)

