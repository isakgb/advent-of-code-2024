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
    if input[row][col] != "A":
        return 0
    c = 0

    if col >= len(input[0])-1 or col < 1 or row >= len(input)-1 or row < 1:
        return 0

    word = input[row-1][col-1] + input[row-1][col+1] + input[row+1][col-1] + input[row+1][col+1]

    allowed_values = ["MMSS", "MSMS", "SSMM", "SMSM"]
    if word in allowed_values:
        return 1
    return 0



check_pos(rows,1, 2)

count = 0

for i in range(len(rows)):
    for j in range(len(rows[0])):
        check = check_pos(rows, i, j)
        if check > 0:
            print(i, j)
        count += check

print(count)



