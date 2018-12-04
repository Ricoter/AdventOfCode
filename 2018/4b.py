import numpy as np

with open('input/4', 'r') as f:
    data = [line for line in f]

data = [[int(c[1:5]+c[6:8]+c[9:11]+c[12:14]+c[15:17]),c[19:].strip('\n')] for c in data]
# print(data[0]) # [151806122357, 'Guard #2633 begins shift']

data = sorted(data, key=lambda x: x[0]) # sort chonologically

data = [[line[0], line[1].split()[1].strip('#')] for line in data]

## dict of timetables
minutes, days =  60, 3200
guard_dict = dict()
for line in data:
    
    if line[1] not in ['asleep', 'up']:
        guard = int(line[1])
        if guard not in guard_dict:
            guard_dict[guard] = np.zeros((minutes, days)) 
        continue

    if line[1] == 'asleep':
        begin = line[0] % 100 # get minutes
        continue

    if line[1] == 'up':
        end = line[0] % 100 # get minutes
        
        for minute in range(begin,end):
            day = int(str(line[0])[4:8])
            guard_dict[guard][minute,day] = 1

## find guard that sleeps most
#max_sleep = 0
#for guard in guard_dict:
#    asleep = guard_dict[guard].sum() 
#    if asleep > max_sleep:
#        max_sleep = asleep
#        max_guard = guard

## find minute that guard sleeps most
max_days = 0
for guard in guard_dict:
    for minute in range(minutes):
        days = guard_dict[guard][minute].sum()
        if days > max_days:
            max_days = days
            most_slept_minute = minute
            max_guard = guard
print(int(max_guard*most_slept_minute))
