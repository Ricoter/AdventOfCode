import os
import sys

def read_data(input_file, data):
    with open(input_file, 'r') as f:
        for line in f:
            tmp = []
            line = line.strip() # get all chars except the last '\n' char
            for n in line.split(' '):
                tmp.append(n)
            data.append(tmp)

def count_valids(data, part=1):
    valids = 0
    for passphrase in data:
        # Sort letters in word for part 2
        if(part==2):
            for i,n in enumerate(passphrase):
                passphrase[i] = ''.join(sorted(n))

        # Set has only unique combinations
        passphrase_set = set(passphrase)
        # add 1 to valids if there are only unique words
        if len(passphrase) == len(passphrase_set):
            valids += 1

    print('part{}: {}'.format(part, valids))

#                   __main__
def main(input_file):
    data = []
    read_data(input_file, data)
    count_valids(data, part=1)
    count_valids(data, part=2)

if __name__ == "__main__":
    main("input4.in")
