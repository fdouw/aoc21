#!/usr/bin/env python

with open("../input/06") as f:
    fish = map(int, f.readline().split(","))

# Part 1
for day in range(80):
    nextfish = list()
    for f in fish:
        if f == 0:
            nextfish.append(8)
            nextfish.append(6)
        else:
            nextfish.append(f - 1)
    fish = nextfish
print(f"Part 1: {len(fish)}")
