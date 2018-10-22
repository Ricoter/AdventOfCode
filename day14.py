from day10b import main as hash_fn

def main(data):
    used = 0
    for row in range(128):
        knothash = hash_fn(data + '-' + str(row))
        print(knothash, type(knothash))        
        for c in knothash:
            hexscale, num_of_bits = 16, 4
            b = bin(int(c, hexscale))[2:].zfill(num_of_bits)
            for i in b:
                used += int(i)
    
    return used

if __name__ == '__main__':
    print(main('uugsqrei'))
