from aocd import data, lines
from day1 import delimit
import re
from math import prod


class Monkey:
    def __init__(self, id, items, operation, test, if_true, if_false) -> None:
        self.id = id
        self.items = [int(i) for i in items.split(":")[1].split(",")]
        self.operation = operation.split("=")[1].strip()
        self.test = int(test.split("by")[1].strip())
        self.if_true = int(if_true.split("monkey")[1].strip())
        self.if_false = int(if_false.split("monkey")[1].strip())
        self.num_inspections = 0

    def inspect_and_throw(self, modulo, part=1):
        result = []
        for old in self.items:
            new = eval(self.operation)
            new = new % modulo if part == 2 else new // 3
            next_monkey = self.if_true if new % self.test == 0 else self.if_false
            result.append((next_monkey, new))

        self.num_inspections += len(self.items)
        self.items.clear()
        return result

    def __repr__(self) -> str:
        return f"Monkey({self.id}, {self.items}, {self.operation}, {self.test}, {self.if_false}, {self.if_true})"


def parse(lines):
    monkeys = delimit(lines)
    parsed_monkeys = {}
    for monkey in monkeys:
        id, items, operation, test, if_false, if_true = monkey
        id = int(re.match(r"Monkey (\d+):", id).group(1))
        parsed_monkeys[id] = Monkey(id, items, operation, test, if_false, if_true)
    return parsed_monkeys


def solve(lines, iterations=20, part=1):
    monkeys = parse(lines)
    modulo = prod([monkey.test for _, monkey in sorted(monkeys.items())])
    for _ in range(iterations):
        for _, monkey in sorted(monkeys.items()):
            for monkey_id, thrown_item in monkey.inspect_and_throw(modulo, part=part):
                monkeys[monkey_id].items.append(thrown_item)
    return prod(
        list(
            sorted(
                [monkey.num_inspections for _, monkey in sorted(monkeys.items())],
                reverse=True,
            )
        )[:2]
    )


def main():
    print("Part 1:", solve(lines, iterations=20, part=1))
    print("Part 2:", solve(lines, iterations=10000, part=2))


if __name__ == "__main__":
    main()
