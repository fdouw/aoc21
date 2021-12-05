#!/usr/bin/env python

from collections import defaultdict
import numpy as np
import pandas as pd
import re

with open("../input/05") as f:
    rawdata = f.readlines()
    linedata = np.array([int(n) for l in rawdata for n in re.split(r",| -> ", l)])
    linedata = linedata.reshape((len(linedata) // 4, 4))
    # Use a Pandas DataFrame to filter on straight lines, Numpy doesn't allow to filter rows like this
    linedf = pd.DataFrame(linedata, columns=["x1", "y1", "x2", "y2"])

# Part 1
# First register all the vents in a sparse grid
straights = np.array(
    linedf[np.logical_or(linedf["x1"] == linedf["x2"], linedf["y1"] == linedf["y2"])]
)
vents = defaultdict(lambda: 0)
for x1, y1, x2, y2 in straights:
    # Using min and max here, because sometimes the coordinates are in reverse order
    if y1 == y2:
        # horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
            vents[(x, y1)] += 1
    else:
        # vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            vents[(x1, y)] += 1

# Then count the places with more than 1 vent
multicount = sum((1 for _, v in vents.items() if v > 1))
print(f"Part 1: {multicount}")

# Part 2
# We already have the straights, so only consider diagonals
diags = np.array(
    linedf[np.logical_and(linedf["x1"] != linedf["x2"], linedf["y1"] != linedf["y2"])]
)
for x1, y1, x2, y2 in diags:
    dx = -1 if x1 > x2 else 1
    dy = -1 if y1 > y2 else 1
    dist = abs(x2 - x1)
    for i in range(dist + 1):
        vents[(x1 + i * dx, y1 + i * dy)] += 1

multicount = sum((1 for _, v in vents.items() if v > 1))
print(f"Part 2: {multicount}")
