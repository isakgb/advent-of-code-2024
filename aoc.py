import re

import fs

RE_INT = re.compile(r"-?\d+")
RE_FLOAT = re.compile(r"-?(?:\d?\.\d+|\d+)")


def get_input(day):
    input_fs = fs.open_fs("")
    input_fs.makedirs("inputs", recreate=True)

    filename = f"inputs/day_{day:02}.txt"
    if input_fs.exists(filename):
        return input_fs.readtext(filename)
    else:
        import requests
        import dotenv
        import os
        url = f"https://adventofcode.com/2024/day/{day}/input"
        dotenv.load_dotenv()
        r = requests.get(url, cookies={"session": os.getenv("AOC_COOKIE")})
        if r.status_code != 200:
            raise Exception(f"Could not download input for day {day}")
        input_fs.writetext(filename, r.text)
        return r.text


def split_double_newline(data):
    return data.split("\n\n")


def ints(s: str):
    return list(map(int, RE_INT.findall(s)))


def floats(s: str):
    return list(map(float, RE_FLOAT.findall(s)))


def apply(data, func):
    if isinstance(data, list):
        return [apply(x, func) for x in data]
    elif isinstance(data, dict):
        return {k: apply(v, func) for k, v in data.items()}
    else:
        return func(data)


def dir8(x, y):
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1
    yield x+1, y+1
    yield x-1, y-1
    yield x+1, y-1
    yield x-1, y+1


def dir4(x, y):
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1

