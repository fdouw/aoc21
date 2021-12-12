#!/usr/bin/env python

from queue import SimpleQueue


def in_path(cave, path) -> bool:
    while path[1] != None:
        if path[0] == cave:
            return True
        path = path[1]
    return path[0] == cave


def in_path_2(cave, path):
    while path[1] != None:
        if path[0] == cave:
            return True
        path = path[1]
    return path[0] == cave


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

# Part 1
paths = SimpleQueue()
paths.put(("start", None, False))
complete_paths = []
while not paths.empty():
    current_path = paths.get()
    if current_path[0] == "end":
        complete_paths.append(current_path)
    else:
        for nb in neighbours[current_path[0]]:
            if nb.isupper() or not in_path(nb, current_path):
                # NB: Two neighbouring big caves would cause trouble...
                paths.put((nb, current_path, False))

print(f"Part 1: {len(complete_paths)}")

# Part 2
paths = SimpleQueue()
paths.put(("start", None, False))
complete_paths = []
while not paths.empty():
    current_path = paths.get()
    if current_path[0] == "end":
        complete_paths.append(current_path)
    else:
        for nb in neighbours[current_path[0]]:
            if nb.isupper():
                paths.put((nb, current_path, current_path[-1]))
            elif not in_path(nb, current_path):
                paths.put((nb, current_path, current_path[-1]))
            elif nb != "start" and not current_path[-1]:
                paths.put((nb, current_path, True))

print(f"Part 2: {len(complete_paths)}")
