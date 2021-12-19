#!/usr/bin/env python

from itertools import permutations
import numpy as np


# Rotation matrices
Rx = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
Ry = [[0, 0, -1], [0, 1, 0], [1, 0, 0]]
Rz = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
Mx = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
My = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
Mz = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
transformations = ((Mx, Rx), (My, Ry), (Mz, Rz))


def cloud_rotations(cloud):
    x = cloud
    for i in range(4):
        yield x
        y = list(map(lambda v: tuple(np.dot(Rz, v)), x))
        yield y
        y = list(map(lambda v: tuple(np.dot(Rz, v)), y))
        y = list(map(lambda v: tuple(np.dot(Rz, v)), y))
        yield y
        y = list(map(lambda v: tuple(np.dot(Rx, v)), x))
        yield y
        y = list(map(lambda v: tuple(np.dot(Rx, v)), y))
        yield y
        y = list(map(lambda v: tuple(np.dot(Rx, v)), y))
        yield y
        # print("==========================")
        if i < 4:
            x = list(map(lambda v: tuple(np.dot(Ry, v)), x))


# I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# for rot in cloud_rotations([I]):
#     r = rot[0]
#     print(f"{r[0]}\n{r[1]}\n{r[2]}\n")


with open("../input/19") as f:
    scanner_data = [
        [tuple(map(int, l.split(","))) for l in block.splitlines()[1:]]
        for block in f.read().split("\n\n")
    ]


matched = [scanner_data[0]]
scanners = [(0, 0, 0)]
next_search = scanner_data[1:]
fixed_points = set(scanner_data[0])

i = 0
while len(matched) < len(scanner_data):
    print(f"{len(matched):3} clouds matched so far", end="", flush=True)
    reference = matched[i]
    search_count = 0
    to_search = next_search
    next_search = []
    for search_cloud in to_search:
        found_match = False
        print(".", end="", flush=True)
        for anchor_point in reference:
            for transformed_cloud in cloud_rotations(search_cloud):
                for target_point in transformed_cloud:
                    delta = np.subtract(target_point, anchor_point)
                    moved_cloud = [
                        tuple(np.subtract(v, delta)) for v in transformed_cloud
                    ]
                    overlap = set.intersection(set(moved_cloud), set(reference))
                    if len(overlap) == 12:
                        matched.append(moved_cloud)
                        scanners.append((-delta[0], -delta[1], -delta[2]))
                        fixed_points |= set(moved_cloud)
                        found_match = True
                        break
                if found_match:
                    break
            if found_match:
                break
        if not found_match:
            next_search.append(search_cloud)
        search_count += 1
    i += 1
    print()

print(f"Part 1: {len(fixed_points)}")


max_dist = 0
for p, q in permutations(scanners, 2):
    d = abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])
    if d > max_dist:
        max_dist = d
print(f"Part 2: {max_dist}")
