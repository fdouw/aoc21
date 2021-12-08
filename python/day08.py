#!/usr/bin/env python

from collections import Counter

with open("../input/08") as f:
    entries = [[s.split() for s in l.split(" | ")] for l in f.readlines()]

# Part 1
counts = Counter(map(len, (segments for display in entries for segments in display[1])))
# Digits 1,7,4, and 8 use 2,3,4, and 7 segments respectively. And each is the only to do so.
print(f"Part 1: {sum((counts[i] for i in (2,3,4,7)))}")

# Part 2
digit_mapping = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

total = 0
for entry in entries:
    # Per entry, collect the patterns by their length (character/segment count). This gives some info on what digit each
    # pattern might represent:
    #
    #   #segments digits
    #   2         1
    #   3         7
    #   4         4
    #   5         2,3,5
    #   6         0,6,9
    #   7         8
    #
    # Next, we can deduce which character maps to which segment by intersecting the right patterns. Using the letters as
    # in the original description:
    #
    #    aaaa
    #   b    c
    #   b    c
    #    dddd
    #   e    f
    #   e    f
    #    gggg
    #
    # Use the #segments as a label, intersect the corresponding patterns (eg, 5 covers a,d, and g: the segments used by
    # 2,3, and 5). Then we can use the following intersections and differences to deduce which character in the input
    # maps to which segment. (Note: letters below refer to the segments as above, not to the input.)
    #
    #   segment   rule
    #   a         3 - 2
    #   b         4 - 2 - 5
    #   c         2 - 6
    #   d         4 ∩ 5
    #   e         7 - 5 - 4
    #   f         2 ∩ 6
    #   g         (5 ∩ 6) - 3
    #
    # Lastly, use digit_mapping to translate each set of segments into a digit

    # Start with fully filled values, so we can use intersection below
    segments_by_len = {
        2: {"a", "b", "c", "d", "e", "f", "g"},
        3: {"a", "b", "c", "d", "e", "f", "g"},
        4: {"a", "b", "c", "d", "e", "f", "g"},
        5: {"a", "b", "c", "d", "e", "f", "g"},
        6: {"a", "b", "c", "d", "e", "f", "g"},
        7: {"a", "b", "c", "d", "e", "f", "g"},
    }
    for pattern in entry[0]:
        segments_by_len[len(pattern)] = segments_by_len[len(pattern)].intersection(
            {c for c in pattern}
        )

    segment_mapping = {
        set.difference(segments_by_len[3], segments_by_len[2]).pop(): "a",
        set.difference(
            segments_by_len[4], segments_by_len[2], segments_by_len[5]
        ).pop(): "b",
        set.difference(segments_by_len[2], segments_by_len[6]).pop(): "c",
        set.intersection(segments_by_len[4], segments_by_len[5]).pop(): "d",
        set.difference(
            segments_by_len[7], segments_by_len[4], segments_by_len[5]
        ).pop(): "e",
        set.intersection(segments_by_len[2], segments_by_len[6]).pop(): "f",
        set.intersection(segments_by_len[5], segments_by_len[6])
        .difference(segments_by_len[3])
        .pop(): "g",
    }

    # Transliterate the input to standard labels for segments, then map these to digits
    # Combine the digits in a string and convert to int
    digits = (
        digit_mapping["".join(sorted(segment_mapping[c] for c in display))]
        for display in entry[1]
    )
    total += int("".join(digits))

print(f"Part 2: {total}")
