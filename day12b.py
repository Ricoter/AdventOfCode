def main(data):
    
    groups, used = 0, set()
    for j in range(len(data)):
        if j in used:
            continue
        links = [j] 
        for i in links:
            links += [x for x in data[i] if x not in links]
        used.update(links)
        groups += 1
    return(groups)

if __name__ == '__main__':
    with open('input12', 'r') as f:
        data = [list(map(lambda x: int(x.strip(',')), line.split()[2:])) for line in f]

    print(main(data))
