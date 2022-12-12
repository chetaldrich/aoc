from aocd import data, lines
import string
from itertools import chain


def height(c):
    if c in "SE":
        return 0 if c == "S" else 25
    return string.ascii_lowercase.index(c)


def get(grid, i, j):
    try:
        if i < 0 or j < 0:
            return None
        return grid[i][j]
    except IndexError:
        return None


class Node:
    def __init__(self, c, coord) -> None:
        self.c = c
        self.height = height(c)
        self.coord = coord
        self.connections = []

    def __repr__(self) -> str:
        return f"Node({self.height}, {[c.coord for c in self.connections]})"


def parse(lines):
    result = []
    for i, line in enumerate(lines):
        result.append([])
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
            elif c == "E":
                end = (i, j)
            result[-1].append(Node(c, (i, j)))

    for i, line in enumerate(result):
        for j, node in enumerate(line):
            possible_connections = [
                get(result, i - 1, j),
                get(result, i, j - 1),
                get(result, i + 1, j),
                get(result, i, j + 1),
            ]
            actual_connections = [
                n
                for n in possible_connections
                if n is not None and n.height <= node.height + 1
            ]
            node.connections.extend(actual_connections)
    return result, start, end


def bfs(grid, start, end):
    queue = [(grid[start[0]][start[1]], 0)]
    visited = set()
    while queue:
        node, dist = queue.pop(0)
        if node.coord == end:
            return dist
        for connection in node.connections:
            if connection.coord not in visited:
                visited.add(connection.coord)
                queue.append((connection, dist + 1))
    return None


def part_2(grid, end):
    starts = chain(
        *[[n.coord for n in line if n.c == "S" or n.c == "a"] for line in grid]
    )
    return min(
        [path for start in starts if (path := bfs(grid, start, end)) is not None]
    )


def main():
    grid, start, end = parse(lines)
    first_part = bfs(grid, start, end)
    second_part = part_2(grid, end)
    print("Part 1:", first_part)
    print("Part 2:", second_part)


if __name__ == "__main__":
    main()
