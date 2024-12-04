from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]



text = get_input(5).strip()

rules, data = split_double_newline(text)

rules = rules.splitlines()
rules = apply(rules, ints)

def is_correct_order(seq, rules):
    for low, high in rules:
        if low in seq and high in seq:
            if seq.index(low) > seq.index(high):
                return False
    return True

a = 0

for line in data.splitlines():
    if is_correct_order(ints(line), rules):
        a += ints(line)[len(ints(line))//2]
print(a)

