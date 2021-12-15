#!/usr/bin/env python

with open("../input/15") as f:
    cave = [[int(c) for c in l.strip()] for l in f.readlines()]

width = len(cave[0])
height = len(cave)
deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Part 1
distances = [[100_000_000] * width for _ in range(height)]
next_search = {(0, 1), (1, 0)}

# Don't count the starting position, as we never enter it
distances[0][0] = 0
while len(next_search) > 0:
    current_search = next_search
    next_search = set()
    for x, y in current_search:
        updated = False
        for dx, dy in deltas:
            if 0 <= x + dx < width and 0 <= y + dy < height:
                if distances[y + dy][x + dx] + cave[y][x] < distances[y][x]:
                    distances[y][x] = distances[y + dy][x + dx] + cave[y][x]
                    updated = True
        if updated:
            next_search |= {
                (x + dx, y + dy)
                for dx, dy in deltas
                if 0 <= x + dx < width and 0 <= y + dy < height
            }

print(f"Part 1: {distances[-1][-1]}")


# Generate input for part 2
width2, height2 = width * 5, height * 5
cave2 = [0] * height2
for y in range(height2):
    cave2[y] = [0] * width2
    y1 = y % height
    shift_y = y // height
    for x in range(width2):
        x1 = x % width
        shift_x = x // width
        cave2[y][x] = (cave[y1][x1] + shift_y + shift_x - 1) % 9 + 1

# Part 2
distances = [[100_000_000] * width2 for _ in range(height2)]
next_search = {(0, 1), (1, 0)}

# Don't count the starting position, as we never enter it
distances[0][0] = 0
while len(next_search) > 0:
    current_search = next_search
    next_search = set()
    for x, y in current_search:
        updated = False
        for dx, dy in deltas:
            if 0 <= x + dx < width2 and 0 <= y + dy < height2:
                if distances[y + dy][x + dx] + cave2[y][x] < distances[y][x]:
                    distances[y][x] = distances[y + dy][x + dx] + cave2[y][x]
                    updated = True
        if updated:
            next_search |= {
                (x + dx, y + dy)
                for dx, dy in deltas
                if 0 <= x + dx < width2 and 0 <= y + dy < height2
            }

print(f"Part 2: {distances[-1][-1]}")
