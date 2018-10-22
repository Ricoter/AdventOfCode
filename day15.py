def main(a0, b0):
    factor_a, factor_b = 16807, 48271
    remainder = 2147483647
    N = int(4e7)

    count = 0
    a, b = a0, b0
    for i in range(N):
        a = (a*factor_a) % remainder
        b = (b*factor_b) % remainder
        if a%(2**16) == b%(2**16):
            count += 1

    return count


if __name__ == '__main__':

    a0, b0 = 116, 299
    test_a0, test_b0 = 65, 8921
    print(main(a0, b0))
