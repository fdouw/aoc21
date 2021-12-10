#!/usr/bin/env python

with open("../input/10") as f:
    lines = f.readlines()

score_table = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}
matching_chars = {")": "(", "]": "[", "}": "{", ">": "<"}
open_chars = matching_chars.values()

score_p1 = 0
scores_p2 = []
for line in lines:
    stack = []
    for c in line.strip():
        if c in open_chars:
            stack.append(c)
        else:
            if matching_chars[c] == stack[-1]:
                stack.pop()
            else:
                score_p1 += score_table[c]
                break
    else:
        # No break out of the loop, so this line must be incomplete
        score = 0
        while len(stack) > 0:
            c = stack.pop()
            score *= 5
            score += score_table[c]
        scores_p2.append(score)

print(f"Part 1: {score_p1}")

ordered = sorted(scores_p2)
score_p2 = ordered[len(scores_p2) // 2]
print(f"Part 2: {score_p2}")
