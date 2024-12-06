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


def is_loop(board, obs_pos):
    board = [[cell for x, cell in enumerate(row)] for y, row in enumerate(board)]

    board[obs_pos[1]][obs_pos[0]] = "#"

    pos = None

    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == "^":
                pos = (x, y)

    if pos == None:
        return False

    dir = dirs[0]

    visited = set()

    while pos[1] >= 0 and pos[1] < len(board) and pos[0] >= 0 and pos[0] < len(board[0]):
        if (pos, dir) in visited:
            return True
        visited.add((pos, dir))
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])

        if not (next_pos[1] >= 0 and next_pos[1] < len(board) and next_pos[0] >= 0 and next_pos[0] < len(board[0])):
            break

        if board[next_pos[1]][next_pos[0]] != "#":
            pos = next_pos
        else:
            dir = dirs[(dirs.index(dir) + 1) % 4]
    return False


obs_count = 0

for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if is_loop(rows, (x, y)):
            obs_count += 1

print(obs_count)
