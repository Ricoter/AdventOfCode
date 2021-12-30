import numpy as np


def part1(position):
    score = [0, 0]
    for i, trow in enumerate(range(6, 10000, 9)):
        player = i%2
        position[player] = (position[player] + trow - 1) % 10 + 1
        score[player] += position[player]
        if score[player] >= 1000:
            return 3 * (i+1) * score[player-1]
        

def part2(position : list, max_score : int = 21, board_size : int = 10):
    # stretch space for all possible universes
    game = np.zeros((max_score, max_score, board_size, board_size), int)

    # starting universe
    game[0, 0, position[0]-1, position[1]-1] = 1

    # count winning universes
    n_universes = [0, 0]

    for i in range(1000):

        # set Player Score Axis (psa)
        psa = 2 + i%2

        # dirac dice
        a, b, c = 1, 2, 3

        # roll the board 3 times
        game = np.roll(game, shift=a, axis=psa) + np.roll(game, shift=b, axis=psa) + np.roll(game, shift=c, axis=psa)    
        game = np.roll(game, shift=a, axis=psa) + np.roll(game, shift=b, axis=psa) + np.roll(game, shift=c, axis=psa)    
        game = np.roll(game, shift=a, axis=psa) + np.roll(game, shift=b, axis=psa) + np.roll(game, shift=c, axis=psa)    

        # update score
        new_game = np.zeros_like(game)
        for j in range(10):
            for k in range(max_score):
                if i%2==0:
                    if k+j+1 >= max_score:
                        n_universes[0] += np.sum(game[k, :, j, :])
                    else:
                        new_game[k+(j+1), :, j ,:] += game[k, :, j, :]
                else:
                    if k+j+1 >= max_score:
                        n_universes[1] += np.sum(game[:, k, :, j])
                    else:
                        new_game[:, k+(j+1), :, j] += game[:, k, :, j]
        game = new_game

        # game over
        if np.sum(game) == 0:
            return n_universes


if __name__=='__main__':
    positions = [9, 10]
    print(part1(positions))
    print(part2(positions))