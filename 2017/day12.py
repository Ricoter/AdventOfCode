def main(data):
    links = [0] 
    for i in links:
        links += [x for x in data[i] if x not in links]
    
    return(len(links))

if __name__ == '__main__':
    with open('input12', 'r') as f:
        data = [list(map(lambda x: int(x.strip(',')), line.split()[2:])) for line in f]

    print(main(data))
