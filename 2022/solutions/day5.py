from aocd import lines
from day1 import delimit
import re


def parse_crates(crates, columns):
    num_columns = max(int(value) for value in columns.split())
    parsed_crates = [[] for _ in range(num_columns)]
    for line in reversed(crates):
        crate_split = re.split(r"(\s+)", line)
        index = 0
        for value in crate_split:
            if match := re.match(r"\[(.)\]", value):
                parsed_crates[index].append(match.group(1))
                index += 1
            else:
                index += (len(value) - 1) // 4
    return parsed_crates


def parse_instructions(instructions):
    parsed_instructions = []
    for line in instructions:
        parsed_instructions.append(
            [
                int(value)
                for value in re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()
            ]
        )
    return parsed_instructions


def move(crates, instruction, reverse=False):
    num_crates, start, end = instruction
    moved_crates = crates[start - 1][-num_crates:]
    if reverse:
        moved_crates = list(reversed(moved_crates))
    del crates[start - 1][-num_crates:]
    crates[end - 1].extend(moved_crates)
    return crates


def solve(crates, instructions, reverse=False):
    crates = parse_crates(crates[:-1], crates[-1])
    instructions = parse_instructions(instructions)
    for instruction in instructions:
        crates = move(crates, instruction, reverse=reverse)
    return "".join([stack[-1] for stack in crates])


def main():
    crates, instructions = delimit(lines)
    print("Part 1:", solve(crates, instructions, reverse=True))
    print("Part 2:", solve(crates, instructions, reverse=False))


if __name__ == "__main__":
    main()
