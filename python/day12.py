#!/usr/bin/env python


def count_paths(cave="start", visited={"start"}, allow_small_cave=False) -> int:
    if cave == "end":
        return 1
    count = 0
    for nb in neighbours[cave]:
        if nb.isupper():
            count += count_paths(nb, visited, allow_small_cave)
        elif nb not in visited:
            count += count_paths(nb, visited | {nb}, allow_small_cave)
        elif allow_small_cave and nb != "start":
            count += count_paths(nb, visited, False)
    return count


with open("../input/12") as f:
    rawdata = f.readlines()
    neighbours = {}
    for l in rawdata:
        a, b = l.strip().split("-")
        if a not in neighbours:
            neighbours[a] = set({b})
        else:
            neighbours[a].add(b)
        if b not in neighbours:
            neighbours[b] = set({a})
        else:
            neighbours[b].add(a)


print(f"Part 1 - dfs: {count_paths()}")
print(f"Part 2 - dfs: {count_paths(allow_small_cave=True)}")
