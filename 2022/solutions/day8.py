from aocd import lines
import math


def is_visible(x, y, grid):
    if x == 0 or y == 0 or x == len(grid[0]) - 1 or y == len(grid) - 1:
        return True
    else:
        max_tree_by_line = [max(line) for line in lines_of_sight(x, y, grid)]
        tree = grid[x][y]
        return any(tree > max_tree for max_tree in max_tree_by_line)


def lines_of_sight(x, y, grid):
    left = list(reversed(grid[x][:y]))
    right = grid[x][y + 1 :]
    down = [grid[i][y] for i in range(x + 1, len(grid[0]))]
    up = [grid[i][y] for i in range(x - 1, -1, -1)]
    return [up, down, left, right]


def scenic_score(x, y, grid):
    tree_lines = lines_of_sight(x, y, grid)
    tree_house_candidate = grid[x][y]
    return math.prod(
        direction_score(line, tree_house_candidate) for line in tree_lines
    )


def direction_score(line, tree_house_candidate):
    score = 0
    for tree in line:
        score += 1
        if tree_house_candidate <= tree:
            break
    return score


def parse_data(lines):
    for line in lines:
        yield [int(x) for x in [*line]]


def main():
    trees = list(parse_data(lines))
    print(
        "Part 1:",
        sum(
            1 if is_visible(x, y, trees) else 0
            for x in range(len(trees))
            for y in range(len(trees[0]))
        ),
    )
    print(
        "Part 2:",
        max(
            scenic_score(x, y, trees)
            for x in range(len(trees))
            for y in range(len(trees[0]))
        ),
    )


if __name__ == "__main__":
    main()
