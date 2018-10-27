import ipdb

# ipdb.set_trace()

buf, pos = [0], 0
for i in range(1,5000001):
    pos = ((pos+343)%i)+1
    buf.insert(pos,i)
    if i%50000==0:
        print(i)
print(buf[buf.index(0)])
    
