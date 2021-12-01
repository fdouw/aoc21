#!/usr/bin/env python

with open("../input/01") as f:
    depths = [int(l) for l in f]
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1
    print(f"Part 1: {count}")

    # Middle numbers of the sliding windows cancel out, so only need to compare the outer edges of the windows
    count = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i - 3]:
            count += 1
    print(f"Part 2: {count}")
