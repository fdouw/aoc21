#!/usr/bin/env python

import numpy as np


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
oxArr = np.array(rawdata, dtype=str)
for i in range(len(oxArr[0])):
    zeroCount = str.join("", oxArr.T[i]).count("0")
    oneCount = str.join("", oxArr.T[i]).count("1")
    nextBit = "0" if zeroCount > oneCount else "1"
    oxArr = oxArr[np.where(oxArr[:, i] == nextBit)]
    if len(oxArr) == 1:
        break
oxygen = int(str.join("", oxArr[0]), 2)
coArr = np.array(rawdata, dtype=str)
for i in range(len(coArr[0])):
    zeroCount = str.join("", coArr.T[i]).count("0")
    oneCount = str.join("", coArr.T[i]).count("1")
    nextBit = "0" if zeroCount <= oneCount else "1"
    coArr = coArr[np.where(coArr[:, i] == nextBit)]
    if len(coArr) == 1:
        break
co2 = int(str.join("", coArr[0]), 2)
print(f"Part 2: {oxygen * co2}")
