from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


groups = ints(get_input(4).strip())
lines = get_input(4).strip().splitlines()


rows = """""".strip().splitlines()

rows = lines


def check_pos(input, row, col):
    if input[row][col] != "X":
        return 0
    letters = "XMAS"
    c = 0
    for dx, dy in dir8(0,0):
        for i in range(1,4):
            new_row = i * dx + row
            new_col = i * dy + col
            if new_col >= len(input[0]) or new_col < 0 or new_row >= len(input) or new_row < 0:
                break
            if input[new_row][new_col] != letters[i]:
                break
        else:
            c+=1
    return c


check_pos(rows,0, 5)

count = 0

for i in range(len(rows)):
    for j in range(len(rows[0])):
        check = check_pos(rows, i, j)
        if check > 0:
            print(i, j)
        count += check

print(count)



