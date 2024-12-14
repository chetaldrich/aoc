from aocd import data
import re
from operator import lt, gt
from math import prod
import numpy as np

def main():
    robots = parse()
    shape = (101, 103)
    print("Part 1:", part1(robots, shape))
    part2(robots, shape)

def part1(robots, shape):
    new_positions = [new_position(pos, vel, 100, shape) for pos, vel in robots]
    groups = group_by_quadrant(new_positions, shape)
    return prod(groups)

def part2(robots, shape):
    # command f in the terminal for lots of #s in a row
    for i in range(7138, 7139):
        new_positions = [new_position(pos, vel, i, shape) for pos, vel in robots]
        p(new_positions, shape)

def p(robots, shape):
    grid = np.zeros(shape, dtype=int)
    for pos in robots:
        grid[pos] = 1
    for row in grid:
        print(''.join('#' if x else '.' for x in row))

def group_by_quadrant(positions, shape):
    groups = [0, 0, 0, 0]
    quadrants = [(lt, gt), (lt, lt), (gt, gt), (gt, lt)]
    for position in positions:
        for i, quadrant in enumerate(quadrants):
            if all(quadrant[j](position[j], shape[j] // 2) for j in range(2)):
                groups[i] += 1
    return groups

def new_position(pos, direction, times, shape):
    return tuple([(pos[i] + direction[i] * times) % shape[i] for i in range(2)])

def parse():
    robots = []
    for line in data.split('\n'):
        x, y, vx, vy = [int(v) for v in re.findall(r'-?\d+', line)]
        robots.append([(x, y), (vx, vy)])
    return robots

if __name__ == '__main__':
    main()
