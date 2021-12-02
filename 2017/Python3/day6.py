import os
import sys

def read_data(input_file, data):
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip() # get all chars except the last '\n' char
            for n in line.split():
                data.append(int(n))

def count_distributions(data, part=1):
    # use copy of the data since we update values
    data = data[:]
    # initialze
    distributions = []
    counter = 0

    while(data not in distributions):
        distributions.append(data[:])
        if(part==1):
            value = max(data)
            i = data.index(value)
            data[i]=0
            while(value>0):
                i += 1
                data[i%len(data)] += 1
                value -= 1

        counter += 1
    cycle_size = counter - distributions.index(data)
    print('counter: {}, cycle size: {}'.format(counter, cycle_size))

#                   __main__
def main(input_file):
    data = []
    read_data(input_file, data)
    count_distributions(data)

if __name__ == "__main__":
    main("input6.in")
