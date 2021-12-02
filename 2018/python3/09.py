import sys
from blist import blist

players = 9
last_marble = 25
players = int(input('number of players: '))
last_marble = int(input('last marble: '))

print(players, last_marble)

marbles = blist([0,1])
d = [0 for _ in range(players)]
player = 1
index = 1
len_marbles = 2
for m in range(2,last_marble + 1):
    if m%23 == 0:
        d[player] += m # add score to player
        index -= 7 # 7 steps back
        if index < 0:
            index %= len_marbles
        d[player] +=  marbles.pop(index) # add score
        len_marbles -= 1 # update
    else:
        index += 2 
        if index > len_marbles:
            index %= len_marbles
        marbles.insert(index, m)
        len_marbles += 1
    player += 1
    player %= players

print(max(d))
