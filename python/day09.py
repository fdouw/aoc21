#!/usr/bin/env python

from math import prod


def get_basin_id(index: int):
    while basinmap[index] != index:
        # Use some additional assignments to shorten the chains as we go, this makes look-ups quicker
        basinmap[index] = index = basinmap[basinmap[index]]
    return index


def connect_basins(a, b):
    basinmap[get_basin_id(a)] = get_basin_id(b)


with open("../input/09") as f:
    heightmap = [[int(c) for c in l.strip()] for l in f.readlines()]

# Part 1
risklevel = 0
height = len(heightmap)
width = len(heightmap[0])
for y in range(height):
    for x in range(width):
        current = heightmap[y][x]
        lowest = True
        if y > 0 and heightmap[y - 1][x] <= current:
            lowest = False
        elif x + 1 < len(heightmap[y]) and heightmap[y][x + 1] <= current:
            lowest = False
        elif y + 1 < len(heightmap) and heightmap[y + 1][x] <= current:
            lowest = False
        elif x > 0 and heightmap[y][x - 1] <= current:
            lowest = False
        if lowest:
            risklevel += 1 + current

print(f"Part 1: {risklevel}")


# Part 2
# Use union-find to find the basins, then sort by size
basinmap = list(range(width * height))

for y in range(height):
    for x in range(width):
        index = y * width + x
        if heightmap[y][x] != 9:
            if y > 0 and heightmap[y - 1][x] != 9:
                connect_basins(index, index - width)
            if x + 1 < width and heightmap[y][x + 1] != 9:
                connect_basins(index, index + 1)
            if y + 1 < height and heightmap[y + 1][x] != 9:
                connect_basins(index, index + width)
            if x > 0 and heightmap[y][x - 1] < 9:
                connect_basins(index, index - 1)

basinsizes = [0] * len(basinmap)
for b in basinmap:
    basinsizes[get_basin_id(b)] += 1
total_size = prod(sorted(basinsizes, reverse=True)[:3])

print(f"Part 2: {total_size}")
