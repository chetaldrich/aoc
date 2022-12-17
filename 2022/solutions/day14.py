from aocd import lines


def parse(lines):
    paths = []
    for line in lines:
        path = []
        for group in line.split("->"):
            pair = (int(i) for i in group.strip().split(","))
            path.append(pair)
        paths.append(path)
    return paths


def flatten(paths):
    pairs = []
    for path in paths:
        for pair in path:
            pairs.append(pair)
    return pairs


def grid(paths, part=2):
    pairs = flatten(paths)
    max_x = max(x for x, _ in pairs)
    min_x = min(x for x, _ in pairs)
    max_y = max(y for _, y in pairs)
    min_y = min(y for _, y in pairs)
    grid = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for path in paths:
        scans = [path[i : i + 2] for i in range(0, len(path) - 1)]
        for pair_1, pair_2 in scans:
            pair_1, pair_2 = sorted([pair_1, pair_2])
            x_1, y_1 = pair_1
            x_2, y_2 = pair_2
            if x_1 == x_2:
                for y in range(y_1, y_2 + 1):
                    grid[y - min_y][x_1 - min_x] = 1
            else:
                for x in range(x_1, x_2 + 1):
                    grid[y_1 - min_y][x - min_x] = 1
    padding = [[0 for _ in range(max_x - min_x + 1)] for _ in range(min_y)]
    grid = padding + grid
    if part == 2:
        floor = [[i for _ in range(max_x - min_x + 1)] for i in range(2)]
        grid = grid + floor
    grid[0][500 - min_x] = 2
    if part == 2:
        grid = [
            pad_sides(1 if i + 1 == len(grid) else 0, row, (max_x - min_x) * 2)
            for i, row in enumerate(grid)
        ]
    sand_point = (0, grid[0].index(2))
    return grid, sand_point


def pad_sides(value, row, pad_len):
    padding = [value for _ in range(pad_len)]
    return padding + row + padding


def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 1:
                print("#", end="")
            elif cell == 2:
                print("+", end="")
            elif cell == 3:
                print("o", end="")
            else:
                print(".", end="")
        print()


def simulate(grid, start_point):
    current = start_point
    next_point = None
    while next_point != current:
        if next_point is not None:
            current = next_point
        y, x = current
        future_points = [(y + 1, x), (y + 1, x - 1), (y + 1, x + 1)]
        next_point = next(
            ((y, x) for y, x in future_points if grid[y][x] == 0),
            (current[0], current[1]),
        )
        if next_point[1] < 0 or next_point[0] >= len(grid) or next_point == start_point:
            return grid, True
    y, x = current
    grid[y][x] = 3
    return grid, False


def solve(paths, part=1):
    cave, sand_point = grid(paths, part=part)
    for i in range(100000):
        cave, done = simulate(cave, sand_point)
        if done:
            return i + (part - 1)


def main():
    paths = parse(lines)
    print("Part 1:", solve(paths))
    print("Part 2:", solve(paths, part=2))


if __name__ == "__main__":
    main()
