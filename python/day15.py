#!/usr/bin/env python


def get_distance(cave):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    width = len(cave[0])
    height = len(cave)
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
                for dx, dy in deltas:
                    if 0 <= x + dx < width and 0 <= y + dy < height:
                        next_search.add((x + dx, y + dy))
    return distances[-1][-1]


with open("../input/15") as f:
    data = [[int(c) for c in l.strip()] for l in f.readlines()]

# Generate input for part 2
width, height = len(data[0]), len(data)
width2, height2 = width * 5, height * 5
data2 = [0] * height2
for y in range(height2):
    data2[y] = [0] * width2
    y1 = y % height
    shift_y = y // height
    for x in range(width2):
        x1 = x % width
        shift_x = x // width
        data2[y][x] = (data[y1][x1] + shift_y + shift_x - 1) % 9 + 1

print(f"Part 1: {get_distance(data)}")
print(f"Part 2: {get_distance(data2)}")
