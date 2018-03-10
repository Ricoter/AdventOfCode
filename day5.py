import os
import sys

def read_data(input_file, data):
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip() # get all chars except the last '\n' char
            data.append(int(line))

def count_valids(data, part=1):
    # use copy of the data since we update values
    data = data[:]
    # initialze
    i = 0
    counter = 0
    while(0<=i<len(data)):
        if(part==1):
            data[i] += 1
            i += data[i] - 1
        elif(part==2):
            if(data[i]>=3):
                data[i] -= 1
                i += data[i] + 1
            else:
                data[i] += 1
                i += data[i] - 1
        counter += 1
    print('part{}: {}'.format(part, counter))

#                   __main__
def main(input_file):
    data = []
    read_data(input_file, data)
    count_valids(data, part=1)
    count_valids(data, part=2)

if __name__ == "__main__":
    main("input5.in")
