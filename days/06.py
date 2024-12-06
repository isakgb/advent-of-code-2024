from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]


text = get_input(6).strip()




rows = text.splitlines()

pos = None

for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col == "^":
            pos = (x, y)
            print("Found pos", pos)


dir = dirs[0]

visited = set()

while pos[1] >= 0 and pos[1] < len(rows) and pos[0] >= 0 and pos[0] < len(rows[0]):
    visited.add(pos)
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])

    if not (next_pos[1] >= 0 and next_pos[1] < len(rows) and next_pos[0] >= 0 and next_pos[0] < len(rows[0])):
        break

    if rows[next_pos[1]][next_pos[0]] != "#":
        pos = next_pos
    else:
        dir = dirs[(dirs.index(dir)+1)%4]

print(len(visited))
