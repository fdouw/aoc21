#!/usr/bin/env python

with open("../input/10") as f:
    lines = f.readlines()

# Part 1
score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
matching_chars = {")": "(", "]": "[", "}": "{", ">": "<"}
open_chars = matching_chars.values()
score = 0
for line in lines:
    stack = []
    for c in line.strip():
        if c in open_chars:
            stack.append(c)
        else:
            if matching_chars[c] == stack[-1]:
                stack.pop()
            else:
                score += score_table[c]
                break

print(f"Part 1: {score}")
