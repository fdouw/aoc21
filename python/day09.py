#!/usr/bin/env python

from math import prod


def get_basin_id(index: int):
    while basinmap[index] != index:
        index = basinmap[index]
    return index


with open("../input/09") as f:
    heightmap = [[int(c) for c in l.strip()] for l in f.readlines()]

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


# basinmap = [[y * width + x for x in range(width)] for y in range(height)]
basinmap = list(range(width * height))

updated = True
while updated:
    updated = False
    for y in range(height):
        for x in range(width):
            current = heightmap[y][x]
            index = y * width + x
            if heightmap[y][x] == 9:
                # Height 9 is not part of a basin
                continue
            elif (
                y > 0
                and get_basin_id(index) != get_basin_id(index - width)
                and heightmap[y - 1][x] < current
            ):
                basinmap[index] = get_basin_id(index - width)
                updated = True
            elif (
                x + 1 < len(heightmap[y])
                and get_basin_id(index) != get_basin_id(index + 1)
                and heightmap[y][x + 1] < current
            ):
                basinmap[index] = get_basin_id(index + 1)
                updated = True
            elif (
                y + 1 < len(heightmap)
                and get_basin_id(index) != get_basin_id(index + width)
                and heightmap[y + 1][x] < current
            ):
                basinmap[index] = get_basin_id(index + width)
                updated = True
            elif (
                x > 0
                and get_basin_id(index) != get_basin_id(index - 1)
                and heightmap[y][x - 1] < current
            ):
                basinmap[index] = get_basin_id(index - 1)
                updated = True
    pass

basinsizes = [0] * len(basinmap)
for b in basinmap:
    basinsizes[get_basin_id(b)] += 1
total_size = prod(sorted(basinsizes, reverse=True)[:3])

print(f"Part 2: {total_size}")
