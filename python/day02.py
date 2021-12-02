#!/usr/bin/env python

with open("../input/02") as f:
    data = f.readlines()

# part 1
forward = sum(int(l[7:]) for l in data if l.startswith("forward"))
depth = sum(int(l[4:]) for l in data if l.startswith("down"))
depth -= sum(int(l[2:]) for l in data if l.startswith("up"))
print(f"Part 1: {forward*depth}")

# part 2
# forward will be unchanged
aim = 0
depth = 0
for l in data:
    if l.startswith("up"):
        x = int(l[2:])
        aim -= x
    elif l.startswith("down"):
        x = int(l[4:])
        aim += x
    else:  # l.startswith("forward")
        x = int(l[7:])
        depth += aim * x
print(f"Part 2: {forward*depth}")
