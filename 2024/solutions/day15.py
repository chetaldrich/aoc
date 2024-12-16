from aocd import data
import numpy as np
from copy import deepcopy

directions = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

def main():
    grid, route = parse()
    simulated_grid = simulate(deepcopy(grid), route, robot(grid))
    print("Part 1:", sum([100 * x + y for x, y in np.argwhere(simulated_grid == "O")]))
    double_grid = double(grid)
    simulated_grid = simulate(double_grid, route, robot(double_grid))
    print("Part 2:", sum([100 * x + y for x, y in np.argwhere(simulated_grid == "[")]))

def robot(grid):
    return list(reversed([v[0] for v in np.where(grid == "@")]))

def simulate(grid, route, robot):
    for direction in route:
        x, y = robot
        blocks, should_move = blocks_to_move(grid, x, y, direction)
        if should_move:
            move(grid, blocks, *directions[direction])
            robot = (x+directions[direction][0], y+directions[direction][1])
    return grid

def move(grid, blocks, dx, dy):
    for x, y in blocks:
        value = grid[y, x]
        assert grid[y+dy, x+dx] == "."
        grid[y+dy, x+dx] = value
        grid[y, x] = "."

def blocks_to_move(grid, x, y, direction):
    dx, dy = directions[direction]
    blocks = {(x, y)}
    while True:
        if blocked(grid, blocks, (x, y), direction):
            return blocks, False
        if clear(grid, blocks, (x, y), direction):
            blocks = list(sorted(blocks, key=lambda pos: pos[0] if direction in "><" else pos[1], reverse=(direction in "v>")))
            return blocks, True
        blocks_to_add = new_blocks(grid, blocks, (x, y), direction)
        blocks.update(blocks_to_add)
        x, y = x+dx, y+dy

def new_blocks(grid, blocks, pos, direction):
    x, y = pos
    dx, dy = directions[direction]
    result = set()
    if direction in "><":
        result.update(find_blocks(grid, x, y, dx, dy))
    else:
        for block in blocks:
            result.update(find_blocks(grid, block[0], block[1], dx, dy))
    return result

def find_blocks(grid, x, y, dx, dy):
    blocks = []
    if grid[y+dy, x+dx] == "[":
        blocks.extend([(x+dx, y+dy), (x+dx+1, y+dy)])
    elif grid[y+dy, x+dx] == "]":
        blocks.extend([(x+dx-1, y+dy), (x+dx, y+dy)])
    if grid[y+dy, x+dx] == "O":
        blocks.append((x+dx, y+dy))
    return blocks

def clear(grid, blocks, pos, direction):
    x, y = pos
    dx, dy = directions[direction]
    if direction in "><":
        return grid[y+dy, x+dx] == "."
    else:
        f = max if direction in "v" else min
        furthest_y = f(y for x, y in blocks)
        return all(grid[y+dy, x+dx] == "." for x, y in blocks if y == furthest_y)

def blocked(grid, blocks, pos, direction):
    x, y = pos
    dx, dy = directions[direction]
    if direction in "><":
        return grid[y+dy, x+dx] == "#"
    return any(grid[y+dy, x+dx] == "#" for x, y in blocks)

def double(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for col in row:
            if col == "@":
                new_row.extend(["@", "."])
            elif col == "O":
                new_row.extend(["[", "]"])
            else:
                new_row.extend([col, col])
        new_grid.append(new_row)
    return np.array(new_grid)

def parse():
    grid = []
    route = ""
    for line in data.splitlines():
        if "#" in line:
            grid.append(list(line.strip()))
        elif line != "":
            route += line.strip()
    return np.array(grid), route

if __name__ == '__main__':
    main()
