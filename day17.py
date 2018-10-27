import ipdb

# ipdb.set_trace()

buf, pos = [0], 0
for i in range(1,2018):
    pos = ((pos+343)%i)+1
    buf.insert(pos,i)

print(buf[pos+1])
    
