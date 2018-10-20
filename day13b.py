def main(data):
    delay = 0
    while True:        
        score = 0
        for i, j in data:
            if (i+delay)%((j-1)*2) == 0:
                score += 1
        if score == 0:
            break

        delay += 1
    return delay


if __name__ == '__main__':
    with open('input13', 'r') as f:
        data = [line.strip().split(': ') for line in f]
    data = [list(map(int, x)) for x in data]
    print(data)
    # data = [[0,3],[1,2],[4,4],[6,4]]
    print(main(data))
