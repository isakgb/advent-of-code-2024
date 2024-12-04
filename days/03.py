from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]



test = ""

groups = ints(get_input(3).strip())
lines = get_input(3).strip().splitlines()


def test_pos(line, pos):
    if line[pos:pos+4] == "do()":
        return True
    if line[pos:pos+7] == "don't()":
        return False
    if line[pos:pos+4] != "mul(":
        return None
    end = line.find(")",pos+4)
    if end is None:
        return None
    digits = line[pos+4:end].split(",")
    if len(digits) != 2:
        return None
    try:
        return int(digits[0]), int(digits[1])
    except:
        return None

test_pos(test, 1)
test = get_input(3)

s = 0
enabled = True
for i in range(len(test)):
    a = test_pos(test, i)
    if a == True:
        print("Enabled", i)
        enabled = True
        continue
    if a == False:
        print("Disabled", i)
        enabled = False
        continue
    if a is not None and enabled:
        s += a[0] * a[1]

print(s)

