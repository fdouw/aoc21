#!/usr/bin/env python

from queue import SimpleQueue


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
paths.put(["start"])
complete_paths = []
while not paths.empty():
    current_path = paths.get()
    if current_path[-1] == "end":
        complete_paths.append(current_path)
    else:
        for nb in neighbours[current_path[-1]]:
            if nb.isupper() or nb not in current_path:
                # NB: Two neighbouring big caves would cause trouble...
                paths.put(current_path.copy() + [nb])

print(f"Part 1: {len(complete_paths)}")

# # Part 2
# paths = SimpleQueue()
# paths.put(["start"])
# complete_paths = []
# while not paths.empty():
#     current_path = paths.get()
#     if current_path[-1] == "end":
#         complete_paths.append(current_path)
#     else:
#         for nb in neighbours[current_path[-1]]:
#             if nb.isupper() or nb not in current_path:
#                 # NB: Two neighbouring big caves would cause trouble...
#                 paths.put(current_path.copy() + [nb])
#             elif nb.islower() and nb in current_path:
#                 for i in range(len(current_path)):
#                     if current_path[i] != nb and current_path[i].islower():
#                         if current_path[i] in current_path[:i]:
#                             # Duplicate lower case, distinct from nb
#                             break
#                 else:
#                     paths.put(current_path.copy() + [nb])

# print(f"Part 2: {len(complete_paths)}")
