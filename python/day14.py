#!/usr/bin/env python


from typing import DefaultDict


class Molecule:
    def __init__(self, name, nxt=None):
        self.name = name
        self.next = nxt

    def insert_after(self, new_molecule):
        new_molecule.next = self.next
        self.next = new_molecule

    def apply_rule(self, rule):
        if (
            self.name == rule[0][0]
            and self.next != None
            and self.next.name == rule[0][1]
        ):
            self.insert_after(Molecule(rule[1]))
            return True
        return False


with open("../input/14") as f:
    template = f.readline().strip()
    _ = f.readline()
    insertion_rules = [l.strip().split(" -> ") for l in f.readlines()]


counts = DefaultDict(int)

# Create initial polymer
polymer = prev = Molecule(template[0])
counts[template[0]] = 1
for c in template[1:]:
    counts[c] += 1
    prev.next = Molecule(c)
    prev = prev.next

for step in range(10):
    molecule = polymer
    while molecule != None:
        nxt = molecule.next
        for rule in insertion_rules:
            if molecule.apply_rule(rule):
                counts[rule[1]] += 1
                break
        molecule = nxt

diff = max(counts.values()) - min(counts.values())
print(f"Part 1: {diff}")
