#!/usr/bin/env python

import numpy as np


class BingoCard:
    def __init__(self, cardData, reverse=False):
        self.card = np.mat(cardData.replace("\n", "; "))
        self.reset(reverse)

    def reset(self, reverse=False):
        self.reverse = reverse
        if reverse:
            self.marked = np.ones_like(self.card, dtype=bool)
        else:
            self.marked = np.zeros_like(self.card, dtype=bool)

    def mark(self, num):
        """
        Marks or unmarks a number on the card, depending on the reverse property of the card.
        Returns True iff there is a fully marked row or column on the card.
        """
        # If playing in reverse, unmark instead of mark
        self.marked[self.card == num] = not self.reverse
        for row in self.marked:
            if np.all(row):
                return True
        for col in self.marked.T:
            if np.all(col):
                return True
        return False

    def score(self):
        """The score is the sum of all unmarked numbers remaining on the card."""
        return np.sum(self.card[self.marked == False])


def finalscore(nums, cards, target: bool):
    for num in nums:
        for card in cards:
            if card.mark(num) == target:
                return (num, card.score())


with open("../input/04") as f:
    randomNums = np.array(f.readline().split(","), dtype=int)
    cards = [BingoCard(d.strip()) for d in f.read().split("\n\n")]

# Part 1
num, score = finalscore(randomNums, cards, True)
print(f"Part 1: {num*score}")

# Part 2
# Play the game in reverse, unmarking numbers until the first card no longer wins. This is the card we're after
for card in cards:
    card.reset(reverse=True)
num, score = finalscore(randomNums[::-1], cards[::-1], False)
# Subtract num: we have just unmarked it, but in the winning condition we are looking for it would be marked
print(f"Part 1: {num*(score-num)}")
