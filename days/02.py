from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


#groups = ints(get_input(2).strip())
groups = get_input(2).strip()

total_safe = 0




for group in groups.splitlines():
    nums = ints(group)

    prev_diff = None
    prev = None
    diff = None

    safe = 1

    for num in nums:
        if prev is not None:
            diff = num - prev
            print(prev_diff)
            if abs(diff) <= 3:
                print("Abs less than three", abs(diff))
                if prev_diff is not None:
                    if prev_diff * diff > 0:
                        safe *= 1
                    else:
                        print("Not the same prev_diff", prev_diff, diff)
                        safe *= 0
            else:
                print("Fail,", )
                safe *= 0
                break
        prev = num
        prev_diff = diff
    print(group, " ", safe)
    total_safe += safe

    print(nums)


print(total_safe)