from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = ints(get_input(1).strip())

print(groups)

acc = 0

left = [
]

right = []
for i in range(len(groups)//2):
    try:
        a=groups[i*2]
        b=groups[i*2+1]
        a = int(a)
        b = int(b)
        print(a, b)
        left.append(a)
        right.append(b)
    except:
        pass

left.sort()
right.sort()

for i in range(len(left)):
    print(left[i], right[i])
    acc += left[i] * right.count(left[i])

print(acc)