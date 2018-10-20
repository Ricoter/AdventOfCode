def main(data):
    score = 0
    for i, j in data:
        if i%((j-1)*2) == 0:
            score += i*j

    return score 


if __name__ == '__main__':
    with open('input13', 'r') as f:
        data = [line.strip().split(': ') for line in f]
    data = [list(map(int, x)) for x in data]
    print(main(data))
