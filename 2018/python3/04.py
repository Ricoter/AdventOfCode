import numpy as np

with open('input/4', 'r') as f: # read and sort data
    data = sorted([line.split() for line in f])

# save only minutes and [#xxx, 'asleep', 'up']
data = [[int(line[1][3]+line[1][4]), line[3]] for line in data]


## dict of timetables
minutes = 60
guard_dict = dict()
for line in data:
    
    if line[1] not in ['asleep', 'up']:
        guard = int(line[1].strip('#'))
        if guard not in guard_dict:
            guard_dict[guard] = np.zeros(minutes) 
        continue

    if line[1] == 'asleep':
        begin = line[0] # get minutes
        continue

    if line[1] == 'up':
        end = line[0] % 100 # get minutes
        
        for minute in range(begin,end):
            guard_dict[guard][minute] += 1

## find guard that sleeps most
max_sleep = 0
for guard in guard_dict:
    asleep = guard_dict[guard].sum() 
    if asleep > max_sleep:
        max_sleep = asleep
        max_guard = guard

print('part a:', max_guard * np.argmax(guard_dict[max_guard]))

## find minute that guard sleeps most
max_days = 0
for guard in guard_dict:
    for minute in range(minutes):
        days = guard_dict[guard][minute]
        if days > max_days:
            max_days = days
            most_slept_minute = minute
            max_guard = guard

print('part b:', int(max_guard*most_slept_minute))
