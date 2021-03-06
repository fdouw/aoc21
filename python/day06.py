#!/usr/bin/env python


def fishcount(initial, days):
    """Returns the total number of fish after <days> days, starting with <initial> population."""
    fishcounts = [0] * 9
    for i in initial:
        fishcounts[i] += 1

    for _ in range(days):
        resetcount = fishcounts[0]
        for i in range(1, 9):
            fishcounts[i - 1] = fishcounts[i]
        fishcounts[8] = resetcount
        fishcounts[6] += resetcount
    return sum(fishcounts)


with open("../input/06") as f:
    fish = list(map(int, f.readline().split(",")))

print(f"Part 1: {fishcount(fish, 80)}")
print(f"Part 2: {fishcount(fish, 256)}")
