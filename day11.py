
def main(data):
    steps = [data.count(x) for x in ['n', 'ne', 'se', 's', 'sw', 'nw']]

    # substract opposite dir
    for i in range(3):
        steps[i] = steps[i]-steps[i-3]
        steps[i-3] = -steps[i]

    # merge double neighbours twice
    steps = [0 if i<0 else i for i in steps]
    for _ in range(2):
        for i in range(6):    
            # lowest neighor
            ln = min(steps[i-1], steps[i-5])
            steps[i] += ln
            steps[i-1] -= ln
            steps[i-5] -= ln

    return(sum(steps))

if __name__ == '__main__':
    # convert input to list 
    with open('input11', 'r') as f:
        data = f.readline().strip('\n').split(',')
    print(main(data))

    # check test I/O
    test = ['ne,ne,ne', 'ne,ne,sw,sw', 'ne,ne,s,s', 'se,sw,se,sw,sw']
    testcheck = [3, 0, 2, 3]
    testresult = [main(x.split(',')) for x in test]
    if testcheck == testresult:
        print('test complete')
    else:
        print('test failed')
        print(testcheck, testresult)

    # part b: find furthest pos ever gotten
    hi = 0
    for i in range(len(data)):
        hi = max(hi, main(data[:i]))

    print(hi)
