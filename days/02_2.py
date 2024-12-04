from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


#groups = ints(get_input(2).strip())
groups = get_input(2).strip()

total_safe = 0


def is_safe(l: list[int]):
    safe = 1

    prev = None
    prev_diff = None
    diff = None

    for num in l:
        if prev is not None:
            diff = num - prev
            if abs(diff) <= 3:
                if prev_diff is not None:
                    if prev_diff * diff > 0:
                        safe *= 1
                    else:
                        safe *= 0
            else:
                safe *= 0
                break
        prev = num
        prev_diff = diff
    return safe == 1


def is_safe_part_2(l: list[int]):
    for i in range(len(l)):
        new_list = [x for j,x  in enumerate(l) if j != i]
        print(new_list)
        if is_safe(new_list):
            return True
    return False




for group in groups.splitlines():
    nums = ints(group)

    prev_diff = None
    prev = None
    diff = None

    safe = is_safe_part_2(nums)

    print(nums, " ", safe)
    total_safe += 1 if safe else 0


print(total_safe)