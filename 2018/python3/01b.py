"""
    Advert of Code 2018, day 1b
    author==Rico van Midde
    python==python3.6.7
"""

with open('input/1', 'r') as f: # read data
    list_of_changes = [int(i.strip('/n')) for i in f]

i, n, used = 0, 0, set() # initialize variables
L = len(list_of_changes)

while True:
    n += list_of_changes[i%L] # change current number

    if n in used: # check if number is used
        print(n)
        break

    used.add(n) # update list and iterator
    i += 1
