#!/usr/bin/env python

from collections import defaultdict
import numpy as np
import pandas as pd
import re


def printgrid(lenx=10, leny=10):
    # Useful for debugging
    for y in range(leny):
        print(
            str.join(
                "",
                (
                    "." if vents[(x, y)] == 0 else str(vents[(x, y)])
                    for x in range(lenx)
                ),
            )
        )


with open("../input/05") as f:
    rawdata = f.readlines()
    linedata = np.array([int(n) for l in rawdata for n in re.split(r",| -> ", l)])
    linedata = linedata.reshape((len(linedata) // 4, 4))
    # Use a Pandas DataFrame to filter on straight lines, Numpy doesn't allow to filter rows like this
    linedf = pd.DataFrame(linedata, columns=["x1", "y1", "x2", "y2"])

# Part 1
# First register all the vents in a sparse grid
straights = linedf[
    np.logical_or(linedf["x1"] == linedf["x2"], linedf["y1"] == linedf["y2"])
]
vents = defaultdict(lambda: 0)
for _, l in straights.iterrows():
    # Using min and max here, because sometimes the coordinates are in reverse order
    for y in range(min(l["y1"], l["y2"]), max(l["y1"], l["y2"]) + 1):
        for x in range(min(l["x1"], l["x2"]), max(l["x1"], l["x2"]) + 1):
            vents[(x, y)] += 1

# Then count the places with more than 1 vent
multicount = 0
for _, v in vents.items():
    if v > 1:
        multicount += 1
print(f"Part 1: {multicount}")

# Part 2
# We already have the straights, so only consider diagonals
diags = linedf[
    np.logical_and(linedf["x1"] != linedf["x2"], linedf["y1"] != linedf["y2"])
]
for _, l in diags.iterrows():
    dx = -1 if l["x1"] > l["x2"] else 1
    dy = -1 if l["y1"] > l["y2"] else 1
    dist = abs(l["x2"] - l["x1"])
    for i in range(dist + 1):
        vents[(l["x1"] + i * dx, l["y1"] + i * dy)] += 1

# printgrid()

multicount = 0
for _, v in vents.items():
    if v > 1:
        multicount += 1
print(f"Part 2: {multicount}")
