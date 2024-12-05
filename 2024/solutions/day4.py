from aocd import data
from itertools import chain

directions = [
    [(0, 0), (0, 1), (0, 2), (0, 3)], # up
    [(0, 0), (1, 0), (2, 0), (3, 0)], # right
    [(0, 0), (0, -1), (0, -2), (0, -3)], # down
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)], # left
    [(0, 0), (1, 1), (2, 2), (3, 3)], # up-right
    [(0, 0), (1, -1), (2, -2), (3, -3)], # down-right
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)], # down-left
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)] # up-left
]
xmas_pattern = [['M', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'S']]

def main():
    grid = parse()
    word = "XMAS"
    all_xmas_patterns = list(generate_search_patterns(xmas_pattern))
    print("Part 1:", word_search(grid, word))
    print("Part 2:", pattern_search(grid, all_xmas_patterns))

def pattern_search(grid, patterns):
    count = 0
    for pos in start_positions(grid, 'A'):
        for pattern in patterns:
            if check_pattern(grid, pattern, pos):
                count += 1
    return count

def check_pattern(grid, pattern, pos):
    block = get_block(grid, pos)
    if block is None:
        return False
    pattern = list(chain(*pattern))
    return all(not (p != '.' and p != b) for p, b in zip(pattern, block))

def get_block(grid, pos):
    block = []
    y, x = pos
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if y + dy < 0 or y + dy >= len(grid) or x + dx < 0 or x + dx >= len(grid[0]):
                return None
            block.append(grid[y + dy][x + dx])
    return block

def generate_search_patterns(base_pattern):
    for j in range(4):
        yield base_pattern
        base_pattern = rotate(base_pattern)

def rotate(pattern):
    return list(zip(*pattern[::-1]))

def word_search(grid, word):
    count = 0
    for pos in start_positions(grid, word):
        for direction in directions:
            if check_direction(grid, word, pos, direction):
                count += 1
    return count

def check_direction(grid, word, pos, direction):
    for i, (dy, dx) in enumerate(direction):
        y, x = pos
        if y + dy < 0 or y + dy >= len(grid) or x + dx < 0 or x + dx >= len(grid[0]):
            return False
        if grid[y + dy][x + dx] != word[i]:
            return False
    return True

def start_positions(grid, word):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == word[0]:
                yield y, x

def parse():
    return [[char for char in line.strip()] for line in data.split('\n')]

if __name__ == '__main__':
    main()
