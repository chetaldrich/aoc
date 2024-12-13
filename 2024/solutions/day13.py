from aocd import data
import numpy as np
from itertools import groupby, chain
import re

def solve(inputs, prizes, part=1):
    if part == 2:
        prizes = [10000000000000 + prize for prize in prizes]
    x, y = np.linalg.solve(inputs, prizes)
    if integerish(x) and integerish(y):
        return round(x), round(y)
    return None, None

def integerish(f):
    # good enough for government work
    return abs(f - round(f)) < 1e-2

def solution(equations, part=1):
    return sum(3*a + b for a, b in (solve(inputs, prizes, part) for inputs, prizes in equations) if a and b)

def main():
    equations = parse()
    print("Part 1:", solution(equations))
    print("Part 2:", solution(equations, 2))

def parse():
    systems = [list(group) for key, group in groupby(data.splitlines(), lambda x: x == '') if not key]
    equations = []
    for a, b, prize in systems:
        xa, ya, xb, yb, x, y = chain(*(re.findall('(\\d+)', expression) for expression in [a, b, prize]))
        inputs = np.array([[int(xa), int(xb)], [int(ya), int(yb)]])
        prizes = np.array([int(x), int(y)])
        equations.append((inputs, prizes))
    return equations

if __name__ == '__main__':
    main()
