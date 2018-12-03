import numpy as np

with open('input/2', 'r') as f: # read data
    b = [np.asarray([ord(c) for c in line]) for line in f] # to ascii

def find_one_difference(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if np.count_nonzero(b[i] - b[j]) == 1: # check if exactly one element is different
                string = "".join([chr(n) for n in (b[i][np.where((b[i] - b[j]) == 0)])]) # to string
                print(string) # print result
                return

find_one_difference(b)
