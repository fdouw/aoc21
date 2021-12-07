#!/usr/bin/env python

with open("../input/07") as f:
    positions = list(map(int, f.readline().split(",")))


# Part 1
# Distribute crabs on the x-axis, rather than tracking individual positions
linex = [0] * (max(positions) + 1)
for p in positions:
    linex[p] += 1

# Move crabs inwards from the sides, always choosing the side with the fewest crabs to minimise fuel use
i = 0
j = len(linex) - 1
fuel = 0
while i < j:
    if linex[i] < linex[j]:
        fuel += linex[i]
        linex[i + 1] += linex[i]
        i += 1
    else:  # linex[i] > linex[j]:
        fuel += linex[j]
        linex[j - 1] += linex[j]
        j -= 1
# print(f"Location: {i} == {j}")
print(f"Part 1: {fuel}")

# Part 2
# Distribute crabs on the x-axis, rather than tracking individual positions
linex = [0] * (max(positions) + 1)
cost = [0] * len(linex)
for p in positions:
    linex[p] += 1
    cost[p] += 1

# Move crabs inwards from the sides, always choosing the side with the fewest crabs to minimise fuel use
i = 0
j = len(linex) - 1
fuel = 0
while i < j:
    if cost[i] < cost[j]:
        fuel += cost[i]
        cost[i + 1] += cost[i] + linex[i]
        linex[i + 1] += linex[i]
        i += 1
    else:  # cost[i] > cost[j]:
        fuel += cost[j]
        cost[j - 1] += cost[j] + linex[j]
        linex[j - 1] += linex[j]
        j -= 1
# print(f"Location: {i} == {j}")
print(f"Part 2: {fuel}")
