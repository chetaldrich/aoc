from aocd import data
import numpy as np
from itertools import chain

def main():
    plot = parse()
    regions = get_regions(plot)
    print("Part 1:", sum([area(region) * perimeter(region) for region in regions]))
    print("Part 2:", sum(area(region) * corners(region) for region in regions))

def perimeter(region):
    return sum(1 for x,y in region for nx, ny in neighbors(x, y) if (nx, ny) not in region)

def area(region):
    return len(region)

def corners(region):
    convex_corners = [[(1, 0), (0, 1)], [(-1, 0), (0, 1)], [(0, -1), (1, 0)],[(0, -1), (-1, 0)]]
    concave_corners = [[(1, 0), (0, 1), (1, 1)], [(0, -1), (1, 0), (1, -1)],
                       [(0, -1), (-1, 0), (-1, -1)],[(-1, 0), (0, 1), (-1, 1)]]
    corner_count = 0
    for x, y in region:
        for corner in concave_corners:
            x1, y1, x2, y2, x3, y3 = chain(*corner)
            if (x + x1, y + y1) in region and (x + x2, y + y2) in region and (x + x3, y + y3) not in region:
                corner_count += 1
        for corner in convex_corners:
            x1, y1, x2, y2 = chain(*corner)
            if (x + x1, y + y1) not in region and (x + x2, y + y2) not in region:
                corner_count += 1
    return corner_count

def neighbors(x, y):
    return [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]

def flood_fill(grid, pos):
    region = set()
    queue = [pos]
    while queue:
        x, y = queue.pop(0)
        if (x,y) in region:
            continue
        region.add((x, y))
        for nx, ny in neighbors(x,y):
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == grid[x, y]:
                queue.append((nx, ny))
    return region

def get_regions(grid):
    regions = []
    visited_plots = set()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if (x, y) not in visited_plots:
                region = flood_fill(grid, (x, y))
                regions.append(region)
                visited_plots.update(region)
    return regions

def parse():
    grid = np.array([list(x) for x in data.split('\n')])
    return grid


if __name__ == '__main__':
    main()
