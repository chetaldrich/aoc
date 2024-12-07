from aocd import data
from copy import deepcopy

def main():
    grid = parse()
    guard = initial_position(grid)
    visited = guard_forecast(grid, guard, 0)
    print("Part 1:", len(visited))
    print("Part 2:", len(find_loop_obstructions(grid, guard)))

def find_loop_obstructions(grid, guard):
    obstructions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                continue
            grid_copy = deepcopy(grid)
            grid_copy[y][x] = '#'
            if guard_forecast(grid_copy, guard, 0) == True:
                obstructions.append((y, x))
    return obstructions

def initial_position(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                value = (i, j)
                grid[value[0]][value[1]] = '.'
                return value
    raise ValueError('No guard found')

def turn(direction):
    return (direction + 1) % 4

def next(pos, direction):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    y, x = pos
    dy, dx = directions[direction]
    return y + dy, x + dx

def guard_forecast(grid, pos, direction):
    visited = set()
    y, x = pos
    while in_bounds(grid, y, x):
        if (y, x, direction) in visited:
            return True
        visited.add((y, x, direction))
        y_next, x_next = next((y, x), direction)
        if not in_bounds(grid, y_next, x_next):
            break
        if grid[y_next][x_next] == '#':
            direction = turn(direction)
            visited.add((y, x, direction))
        y, x = next((y, x), direction)
    return set((y, x) for y, x, _ in visited)

def in_bounds(grid, y, x):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def print_grid(grid, guard, visited, loop_positions):
    grid[guard[0]][guard[1]] = 'G'
    for y, x in visited:
        grid[y][x] = 'V'
    for y, x in loop_positions:
        grid[y][x] = 'O'
    return '\n'.join([''.join(row) for row in grid])

def parse():
    return [[c for c in line] for line in data.split('\n')]


if __name__ == '__main__':
    main()
