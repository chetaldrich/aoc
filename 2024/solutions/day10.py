from aocd import data
import numpy as np
from collections import defaultdict

def main():
    grid = parse()
    trailheads = np.argwhere(grid==0)
    points = [(pos, [0], [(pos[0], pos[1])]) for pos in trailheads]
    trails = dfs(points, grid)
    print("Part 1:", score(trails))
    print("Part 2:", len(trails))

def score(trails):
    scores = defaultdict(set)
    for trail in trails:
        scores[trail[0]].add(trail[-1])
    return sum(len(v) for v in scores.values())

def dfs(queue, grid):
    trails = []
    while queue:
        pos, nums, path = queue.pop()
        neighbors = list(get_neighbors(pos, grid))
        if len(neighbors) == 0 and 9 in nums and path not in trails:
            trails.append(path)
            continue
        for neighbor in neighbors:
            queue.append((neighbor, nums + [grid[neighbor]], path + [neighbor]))
    return trails

def get_neighbors(pos, grid):
    x, y = pos
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if 0 <= x+dx < grid.shape[0] and 0 <= y+dy < grid.shape[1] and grid[x+dx,y+dy] - grid[x,y] == 1:
            yield x + dx, y + dy

def parse():
    grid = np.array([[int(i) for i in row] for row in data.split('\n')])
    return grid

if __name__ == '__main__':
    main()
