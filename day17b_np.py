import numpy as np
import ipdb

#ipdb.set_trace()
buf, pos = np.asarray([0]), 0
for i in range(1,5000001):
    pos = ((pos+343)%i)+1
    buf = np.insert(buf, pos, i)
    if i%50000==0:
        print(i)

buf = list(buf)
print(buf[buf.index(0)+1])
