import ipdb
from blist import blist
# ipdb.set_trace()

buf, pos = blist([0]), 0
for i in range(1,int(5e7)+1):
    pos = ((pos+343)%i)+1
    buf.insert(pos,i)
    if i%50000==0:
        print(i)
print(buf[buf.index(0)+1])
    
