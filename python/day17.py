#!/usr/bin/env python

minx, maxx = 209, 238
miny, maxy = -86, -59

# target area: x=20..30, y=-10..-5
# minx, maxx = 20, 30
# miny, maxy = -10, -5

# Compute bounderies for initial x-velocity
a = 0  # int(sqrt(2 * minx) - 1)
b = maxx + 1

x_positions = []
for initx in range(a, b):
    x = 0
    x_positions.append([0] + [x := x + dx for dx in range(initx, 0, -1)])

highest = -1
velocities = set()
for inity in range(miny, 2_000):
    posy = 0
    dy = inity
    topy = 0
    n = 0
    while True:
        posy += dy
        if dy > 0:
            topy += dy
        dy -= 1
        n += 1
        if posy < miny:
            break
        if posy <= maxy:
            for initx in range(a, b):
                step = min(n, len(x_positions[initx]) - 1)
                if minx <= x_positions[initx][step] <= maxx:
                    highest = max(highest, topy)
                    velocities.add((initx, inity))

print(f"Part 1: {highest}")
print(f"Part 2: {len(velocities)}")
