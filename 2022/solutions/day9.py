from aocd import data, lines
import operator
from itertools import permutations


class Head:
    def __init__(self) -> None:
        self.position = Vector(0, 0)

    def move(self, vector):
        self.position = self.position + vector

    def __repr__(self) -> str:
        return f"Head({self.position})"


class Tail:
    def __init__(self) -> None:
        self.position = Vector(0, 0)
        self.knights = [
            Vector(first, second)
            for first, second in permutations([2, -2, 1, -1], 2)
            if abs(first) != abs(second)
        ]
        self.diag_leaps = [
            Vector(x, y) for x, y in list(set(permutations([2, -2, -2, 2], 2)))
        ]
        self.two_aways = [Vector(2, 0), Vector(0, 2), Vector(-2, 0), Vector(0, -2)]

    def move(self, goal_position):
        if self.check_and_move(self.two_aways, goal_position, lambda x: x * 0.5):
            return
        else:
            self.check_and_move(
                self.knights + self.diag_leaps, goal_position, lambda x: x.sign()
            )

    def check_and_move(self, vectors, goal_position, f):
        for vector in vectors:
            if self.position + vector == goal_position:
                self.position = self.position + f(vector)
                return True

    def __repr__(self) -> str:
        return f"Tail({self.position})"


class Vector:
    def __init__(self, x, y) -> None:
        self.position = (x, y)

    def sign(self):
        x, y = self.position
        return Vector(sign(x), sign(y))

    def __add__(self, o):
        return Vector(*map(operator.add, self.position, o.position))

    def __mul__(self, factor):
        return Vector(*[int(x * factor) for x in self.position])

    def __eq__(self, o):
        return self.position == o.position

    def __repr__(self) -> str:
        return f"{self.position}"


class Instruction:
    def __init__(self, direction, distance) -> None:
        self.direction = direction
        self.distance = distance

    def to_vectors(self):
        if self.direction == "U":
            return [Vector(0, 1) for _ in range(self.distance)]
        elif self.direction == "D":
            return [Vector(0, -1) for _ in range(self.distance)]
        elif self.direction == "R":
            return [Vector(1, 0) for _ in range(self.distance)]
        elif self.direction == "L":
            return [Vector(-1, 0) for _ in range(self.distance)]
        else:
            raise ValueError(f"Unknown direction {self.direction}")

    def __repr__(self) -> str:
        return f"Instruction({self.direction} {self.distance})"


def sign(x):
    return -1 if x < 0 else 1


def parse(lines):
    return [
        Instruction(direction, int(distance))
        for direction, distance in [line.split() for line in lines]
    ]


def simulate(instructions, len_tail=1):
    head = Head()
    tail = [Tail() for _ in range(len_tail)]
    visited = set()
    for instruction in instructions:
        for vector in instruction.to_vectors():
            head.move(vector)
            for i, knot in enumerate(tail):
                if i == 0:
                    knot.move(head.position)
                else:
                    knot.move(tail[i - 1].position)
            visited.add(tail[-1].position.position)
    return visited


def main():
    instructions = parse(lines)
    print("Part 1:", len(simulate(instructions)))
    print("Part 2:", len(simulate(instructions, 9)))


if __name__ == "__main__":
    main()
