#!/usr/bin/env python

from collections import defaultdict

player1_start = 4
player2_start = 2

# Testvalues
# player1_start = 4
# player2_start = 8


class Die:
    def __init__(self):
        self.num = 1

    def roll(self):
        val = 3 * self.num + 3
        self.num += 3
        return val


die = Die()
pos = [player1_start - 1, player2_start - 1]
score = [0, 0]
while True:
    pos[0] = (pos[0] + die.roll()) % 10
    score[0] += pos[0] + 1
    if score[0] >= 1000:
        print(f"Part 1: {score[1] * (die.num-1)}")
        break
    pos[1] += die.roll()
    score[1] += (pos[1] % 10) + 1
    if score[1] >= 1000:
        print(f"Part 1: {score[0] * (die.num-1)}")
        break


player1_wins = 0
player2_wins = 0
states = defaultdict(int)
states[(player1_start - 1, player2_start - 1, 0, 0)] = 1
die_rolls = [sum((x, y, z)) for z in (1, 2, 3) for y in (1, 2, 3) for x in (1, 2, 3)]
while len(states) > 0:
    # player 1
    new_states = defaultdict(int)
    for state, count in states.items():
        for n in die_rolls:
            new_pos = (state[0] + n) % 10
            new_score = state[2] + new_pos + 1
            if new_score >= 21:
                player1_wins += count
            else:
                new_states[(new_pos, state[1], new_score, state[3])] += count
    states = new_states

    # player 2
    new_states = defaultdict(int)
    for state, count in states.items():
        for n in die_rolls:
            new_pos = (state[1] + n) % 10
            new_score = state[3] + new_pos + 1
            if new_score >= 21:
                player2_wins += count
            else:
                new_states[(state[0], new_pos, state[2], new_score)] += count
    states = new_states

print(f"Part 2: {max(player1_wins,player2_wins)}; {player1_wins=}, {player2_wins=}")
