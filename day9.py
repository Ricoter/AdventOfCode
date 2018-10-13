data = []
with open("input9" , "r") as f:
    for line in f:
        for character in line:
            if character == "\n":
                pass
            else:
                data.append(character)

# remove elements after !
for i, el in enumerate(data):
    if el == '!' and i != len(data)-1:
        del data[i+1]

# remove all '!'
data = list(filter(lambda a: a != '!', data))

# remove garbicz:
garbage = 0
for i in range(len(data)):
    if i >= len(data):
        break
    if data[i] == '<':
        j = i
        while data[j] != '>':
            garbage += 1
            del data[j]
            if j >= len(data)-1:
                break
        garbage -= 1
print("Garbage:", garbage)

def count__data(data):
    score = 0
    depth = 0
    for element in data:
        if element == '{':
            depth+=1
        if  element == '}':
            score += depth
            depth-=1
    return score


#def recursive_group_search(data, i, depth):
#    score = depth
#    if i >= len(data):
#        return(i, score)
#    while i < len(data):
#        if data[i] == '}':
#            continue
#        if data[i] == '{':
#            i, points = recursive_group_search(data, i+1, depth+1)
#            score += points
#        i += 1
#    return(i, score)
#
#_ , score = recursive_group_search(data, 0, 1)

score = count__data(data)
print(score)
