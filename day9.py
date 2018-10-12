data = []
with open("input9test1" , "r") as f:
    for line in f:
        for character in line:
            data.append(character)
print("check1", data[-1])

# remove "/n" element
del data[-1]

# remove elements after !
for i, el in enumerate(data):
    if el == '!' and i != len(data)-1:
        del data[i+1]

# remove garbicz:
for i in range(len(data)):
    if i >= len(data):
        break
    if data[i] == '<':
        j = i
        while data[j] != '>':
            del data[j]
            j += 1
            if j >= len(data)-1:
                break

# remove unused "}"


print(data.count('{'), data.count('}'), "check")
testdata = ['{','{','{','{','}','}','}']
# print(data)
data = data[::-1]
def count__data(data):
    score = 0
    depth = 0
    for element in data:
        if element == '{':
            depth+=1
        if  element == '}':
            if depth ==0:
                depth =0
            else:
                depth-=1
                score +=  depth
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
