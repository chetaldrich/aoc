from aocd import data
import numpy as np
from heapq import heappop, heappush
from collections import defaultdict

class Grid:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.excluded_directions = {
            (1, 0): (-1, 0),
            (-1, 0): (1, 0),
            (0, 1): (0, -1),
            (0, -1): (0, 1)
        }

    def min_path(self, start, end):
        queue = [(0, [start], (1, 0))]
        solutions = defaultdict(lambda: float("inf"))
        seats = set()
        while queue:
            cost, path, direction = heappop(queue)
            node = path[-1]
            if node == end:
                solutions[node] = cost
                seats.update(path)
                continue
            if cost >= solutions[end]:
                continue
            for neighbor, new_direction in self.neighbors(node, direction, cost):
                add_cost = 1 if direction == new_direction else 1001
                new_cost = cost + add_cost
                if solutions[(neighbor, new_direction)] >= new_cost:
                    solutions[(neighbor, new_direction)] = new_cost
                    heappush(queue, (new_cost, path + [neighbor], new_direction))
        return solutions[end], len(seats)

    def neighbors(self, node, direction, cost):
        n = [d for d in [(-1, 0), (1, 0), (0, -1), (0, 1)] if d != self.excluded_directions[direction]]
        return [[(node[0] + i, node[1] + j), (i,j)] for i, j in n if self.grid[node[1] + j, node[0] + i] != '#']

    def __repr__(self):
        return str(self.grid)

def main():
    grid = Grid(*parse())
    min_path_cost, seats = grid.min_path(grid.start, grid.end)
    print("Part 1:", min_path_cost)
    print("Part 2:", seats)

def parse():
    grid = np.array([list(line) for line in data.splitlines()])
    start = reversed(np.argwhere(grid == 'S')[0])
    end = reversed(np.argwhere(grid == 'E')[0])
    return grid, tuple(start), tuple(end)

if __name__ == '__main__':
    main()

