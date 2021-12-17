#!/usr/bin/env python

minx, maxx = 209, 238
miny, maxy = -86, -59

# target area: x=20..30, y=-10..-5
# minx, maxx = 20, 30
# miny, maxy = -10, -5

# Compute bounderies for initial x-velocity
a = 0
b = maxx + 1

x_positions = []
for initx in range(0, b):
    x = 0
    x_positions.append([0] + [x := x + dx for dx in range(initx, 0, -1)])

highest = -1
velocities = set()
for inity in range(miny, -miny):
    posy = 0
    dy = inity
    topy = 0
    n = 0
    while posy >= miny:
        if posy <= maxy:
            for initx in range(a, b):
                step = min(n, len(x_positions[initx]) - 1)
                if minx <= x_positions[initx][step] <= maxx:
                    highest = max(highest, topy)
                    velocities.add((initx, inity))
        posy += dy
        if dy == 0:
            topy = posy
        dy -= 1
        n += 1

print(f"Part 1: {highest}")
print(f"Part 2: {len(velocities)}")
