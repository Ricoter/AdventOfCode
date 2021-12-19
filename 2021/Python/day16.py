import numpy as np

def readData(infile):
    with open(infile, 'r') as f:
        line = f.read().strip('\n')
    return line


def hex2bin(hex):
    binary = bin(int(hex, 16))[2:]
    while len(binary) != len(hex)*4:
        binary = "0" + binary
    return binary


def read_literal(residual):
    literal_bin = ""
    while True:
        prefix = residual[0]
        literal_bin += residual[1:5]
        residual = residual[5:]
    
        if prefix == '0':
            break
    return int(literal_bin, 2), residual

def solve1(bin, total_V=0):
    V = bin[0:3] # packet_version
    T = bin[3:6] #type_ID
    residual = bin[6:]
    if T == '100':
        _, residual = read_literal(residual)
    else:
        I = bin[6] # length_type_ID
        if I == '0':
            L = int(bin[7:7+15], 2)
            sub_packets = bin[7+15: 7+15+L]
            while sub_packets != "":
                local_V, sub_packets = solve1(sub_packets)
                total_V += local_V
            residual = bin[7+15+L:]
        elif I == '1':
            """ 
            If the length type ID is 1, then the next 11 bits are a number that represents:
             the number of sub-packets immediately contained by this packet.
            """
            L = bin[7:7+11]
            n_sub_packets = int(L, 2)
            residual = bin[7+11:]
            for _ in range(n_sub_packets):
                local_V, residual = solve1(residual)
                total_V += local_V

    return total_V + int(V, 2), residual

def part1(data):
    bin = hex2bin(data)
    return solve1(bin)[0]

OPS = {
    '000': np.sum,
    '001': np.prod,
    '010': np.min,
    '011': np.max,
    '101': lambda x: x[0] > x[1],
    '110': lambda x: x[0] < x[1],
    '111': lambda x: x[0] == x[1],
}

def solve2(bin, total_V=0):
    V = bin[0:3] # packet_version
    T = bin[3:6] # type_ID
    residual = bin[6:]
    if T == '100':
        total_V, residual = read_literal(residual)
    else:
        I = bin[6] # length_type_ID
        if I == '0':
            L = int(bin[7:7+15], 2)
            sub_packets = bin[7+15: 7+15+L]
            subvalues = []
            while sub_packets != "":
                _V, sub_packets = solve2(sub_packets)
                subvalues.append(_V)
            total_V = int(OPS[T](subvalues))
            residual = bin[7+15+L:]
        elif I == '1':
            L = bin[7:7+11]
            n_sub_packets = int(L, 2)
            residual = bin[7+11:]
            subvalues = []
            for _ in range(n_sub_packets):
                _V, residual = solve2(residual)
                subvalues.append(_V)
            total_V = OPS[T](subvalues)
    return total_V, residual

def part2(data):
    bin = hex2bin(data)
    return solve2(bin)[0]


if __name__=='__main__':
    data = readData('../Data/day16')
    print(part1(data))
    print(part2(data))