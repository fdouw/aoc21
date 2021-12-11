#!/usr/bin/env python


def neighbours(x, y):
    return [
        (x + dx, y + dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if not (dx == 0 and dy == 0) and 0 <= x + dx < 10 and 0 <= y + dy < 10
    ]


with open("../input/11") as f:
    rawdata = f.readlines()
    grid = [list(map(int, l.strip())) for l in rawdata]

flash_count = 0
full_flash = 0
for step in range(10_000):
    flashed = set()
    queue = []
    for y in range(10):
        for x in range(10):
            grid[y][x] += 1
            if grid[y][x] > 9:
                queue.append((x, y))
    while len(queue) > 0:
        x, y = queue.pop()
        grid[y][x] = 0
        flashed.add((x, y))
        if step < 100:
            flash_count += 1
        for nx, ny in neighbours(x, y):
            if (nx, ny) not in flashed and (nx, ny) not in queue:
                grid[ny][nx] += 1
                if grid[ny][nx] > 9:
                    queue.append((nx, ny))
    if full_flash == 0 and len(flashed) == 100:
        full_flash = step + 1
        if step > 100:
            break

print(f"Part 1: {flash_count}")
print(f"Part 2: {full_flash}")
