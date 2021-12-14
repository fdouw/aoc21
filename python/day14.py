#!/usr/bin/env python


from typing import DefaultDict


with open("../input/14") as f:
    template = f.readline().strip()
    _ = f.readline()
    rules = [l.strip().split(" -> ") for l in f.readlines()]

# For each type of pair, remember how many there are: don't track the entire polymer
# A polymer ABC is AB:1, BC:1. A rule AB->X means AB-=1,AX+=1,and XB+=1.
pair_counts = DefaultDict(int)

molecule_counts = [0] * 26

# count pairs and molecules in initial template
for i in range(len(template) - 1):
    pair_counts[(template[i], template[i + 1])] += 1
    molecule_counts[ord(template[i]) - 65] += 1
molecule_counts[ord(template[-1]) - 65] += 1

# Step through the rules
for step in range(40):
    # Copy the pair`_counts each time, because we don't want to consider newly added molecules yet
    new_counts = pair_counts.copy()
    for rule in rules:
        a, b, c = rule[0][0], rule[0][1], rule[1]
        occurrences = pair_counts[(a, b)]
        if occurrences > 0:
            new_counts[(a, b)] -= occurrences
            new_counts[(a, c)] += occurrences
            new_counts[(c, b)] += occurrences
            molecule_counts[ord(c) - 65] += occurrences
    pair_counts = new_counts
    if step == 9:
        diff = max(molecule_counts) - min(c for c in molecule_counts if c > 0)
        print(f"Part 1: {diff}")

diff = max(molecule_counts) - min(c for c in molecule_counts if c > 0)
print(f"Part 2: {diff}")
