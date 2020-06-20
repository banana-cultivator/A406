import numpy as np

def times_table_lists (number):

    return ([[(i + 0) * (j + 0)
                      for i in range(number)] for j in range(number)])

def times_table_numpy (number):
    i = np.arange (0, number)
    ii = i * i [:, None ]
    return ii
