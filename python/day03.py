#!/usr/bin/env python

import numpy as np


def findRating(diagArr, a, b):
    # filter diagArr, selecting a if zero is the most common bit, b otherwise
    for i in range(len(diagArr[0])):
        zeroCount = str.join("", diagArr.T[i]).count("0")
        oneCount = str.join("", diagArr.T[i]).count("1")
        nextBit = a if zeroCount > oneCount else b
        diagArr = diagArr[np.where(diagArr[:, i] == nextBit)]
        if len(diagArr) == 1:
            break
    return int(str.join("", diagArr[0]), 2)


with open("../input/03") as f:
    rawdata = [list(l.strip()) for l in f.readlines()]

# Part 1
arr = np.array(rawdata, dtype=str)
t = np.transpose(arr)

gamma = int(
    str.join("", ["1" if sum(int(n) for n in r) > len(r) / 2 else "0" for r in t]), 2
)
epsilon = int(
    str.join("", ["1" if sum(int(n) for n in r) <= len(r) / 2 else "0" for r in t]), 2
)
print(f"Part 1: {gamma * epsilon}")

# Part 2
oxygen = findRating(np.array(rawdata, dtype=str), "0", "1")
co2 = findRating(np.array(rawdata, dtype=str), "1", "0")
print(f"Part 2: {oxygen * co2}")
