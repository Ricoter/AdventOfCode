import os
import sys

def read_data(input_file, data):
    with open(input_file, 'r') as f:
        for line in f:
            for n in line[0:-1]: # get all chars except the last '\n' char
                data.append(int(n)) # convert char to int


def total_sum_of_doubles(data, diff=1):
    """
        for part 1 a double is defined by neighbouring digits, so diff = 1
        for part 2 diff = (half the size of the list) = len(data)/2
    """
    total = 0
    for i, number in enumerate(data):
        if data[i] == data[i-diff]:
            total += number
    return total


#                   __main__
def main(input_file):
    data = []
    read_data(input_file, data)
    print('length data: ', len(data))
    # part 1
    answer = total_sum_of_doubles(data)
    print("Part1, total sum of doubles: ", answer)
    # part 2
    diff = int(len(data)/2)
    answer = total_sum_of_doubles(data, diff=diff)
    print("Part2, total sum of doubles: ", answer)


if __name__ == "__main__":
    main(sys.argv[1])
