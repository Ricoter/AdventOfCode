import numpy as np

def readData(infile):
    with open(infile, 'r') as f:
        data = [line.strip('\n') for line in f]
        # data = [line.split(' ') for line in data]
    return data

def part1(data):
    binaryString = ""
    for i in range(len(data[0])):
        nOnes = 0
        for s in data:
            nOnes += int(s[i])
        if (nOnes/len(data)) > 0.5: # weakness: no plan for equal occurence
            binaryString += '1'
        else:
            binaryString += '0'
    gammaRate = int(binaryString, 2)
    epsilonRate = int('111111111111', 2) - gammaRate
    print(binaryString, gammaRate, epsilonRate)

    return gammaRate * epsilonRate

def part2(data):
    L = len(data[1])
    data = np.array([list(line) for line in data]).astype(int)
    data2 = data.copy()
    
    # Oxigen generator rating
    i = 0
    while np.shape(data2)[0] > 1:
        ratio = (sum(data2[:,i]) / np.shape(data2)[0])
        if ratio >= 0.5:
            data2 = data2[data2[:,i] == 1,:]
        else:
            data2 = data2[data2[:,i] == 0,:]
        i = (i+1)%L

    oxGen = int("".join(map(str, data2[0])), 2)

    # CO2 scrubber rating
    i = 0
    while np.shape(data)[0] > 1:
        ratio = (sum(data[:,i]) / np.shape(data)[0])
        if ratio >= 0.5:
            data = data[data[:,i] == 0,:]
        else:
            data = data[data[:,i] == 1,:]
        i = (i+1)%L
    CO2Scrub = int("".join(map(str, data[0])), 2)

    return oxGen * CO2Scrub

if __name__=='__main__':
    data = readData('../Data/day03')
    print(data)
    print(part1(data))
    print(part2(data))