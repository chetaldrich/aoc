from aocd import data
import numpy as np
from itertools import chain, combinations
from operator import add, sub

def main():
    antenna_locations, grid_dimensions = parse()
    base_antinodes = find_antinodes(antenna_locations, grid_dimensions, 1)
    resonant_antinodes = find_antinodes(antenna_locations, grid_dimensions, 2)
    print("Part 1:", len(base_antinodes))
    print("Part 2:", len(resonant_antinodes))

def find_antinodes(antenna_locations, grid_dimensions, part=1):
    antinodes = set()
    for _, locations in antenna_locations.items():
        for first, second in combinations(locations, 2):
            for antinode in resonant_antinodes(first, second, grid_dimensions, part):
                antinodes.add(antinode)
    return antinodes

def resonant_antinodes(first, second, grid_dimensions, part=1):
    max_y, max_x = grid_dimensions
    diff = first - second
    max_resonances = abs(int(max(max_x // diff.imag, max_y // diff.real))) if part == 2 else 1
    return [point for i in range(max_resonances)
            for op, pos in [(add, first), (sub, second)]
            if in_bounds(point := op(pos, diff*i), max_x, max_y)]

def in_bounds(point, max_x, max_y):
    return 0 <= point.imag < max_x and 0 <= point.real < max_y

def parse():
    grid = np.array([list(line) for line in data.split("\n")])
    antenna_types = set(c for c in chain(*grid) if c != '.')
    return {c: [complex(y, x) for y, x in np.argwhere(grid == c)] for c in antenna_types}, (len(grid), len(grid[0]))


if __name__ == '__main__':
    main()
