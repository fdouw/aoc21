#!/usr/bin/env python

from queue import PriorityQueue


def get_distance(cave):
    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
    width = len(cave[0])
    height = len(cave)
    distances = [[100_000_000] * width for _ in range(height)]
    next_search = PriorityQueue()
    next_search.put((0, (0, 0)))

    # Don't count the starting position, as we never enter it
    distances[0][0] = 0
    while not next_search.empty():
        dist, pos = next_search.get()
        x, y = pos
        if pos == (width - 1, height - 1):
            return dist
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if cave[ny][nx] + dist < distances[ny][nx]:
                    distances[ny][nx] = dist + cave[ny][nx]
                    next_search.put((distances[ny][nx], (nx, ny)))
    return -1


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
