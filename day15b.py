def main(a0, b0):
    factor_a, factor_b = 16807, 48271
    remainder = 2147483647
    N = int(5e6)
    
    #import ipdb
    #ipdb.set_trace()

    count = 0
    a, b = a0, b0
    que_a, que_b = [], []
    while N>0:
        a = (a*factor_a) % remainder
        b = (b*factor_b) % remainder
        if a%4 == 0:
            que_a.append(a%(2**16))
        if b%8 == 0:
            que_b.append(b%(2**16))
        if que_a and que_b:
            if que_a.pop(0) == que_b.pop(0):
                count += 1
            N -= 1
    return count


if __name__ == '__main__':

    a0, b0 = 116, 299
    test_a0, test_b0 = 65, 8921
    print(main(a0, b0))
