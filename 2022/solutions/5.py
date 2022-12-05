from aocd import lines
import re

def parse_crates(crates, columns):
    num_columns = max([int(value) for value in columns.split(" ") if value != ""])
    parsed_crates = [[] for _ in range(num_columns)]
    for line in reversed(crates):
        crate_split = re.split(r'(\s+)', line)
        index = 0
        for value in crate_split:
            if match := re.match(r'\[(.)\]', value):
                parsed_crates[index].append(match.group(1))
                index += 1
            else:
                index += (len(value) - 1) // 4
    return parsed_crates

def parse_instructions(instructions):
    parsed_instructions = []
    for line in instructions:
        parsed_instructions.append([int(value) for value in re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()])
    return parsed_instructions

def move_part_1(crates, instruction):
    num_crates, start, end = instruction
    moved_crates = list(reversed(crates[start-1][-num_crates:]))
    del crates[start-1][-num_crates:]
    crates[end-1].extend(moved_crates)
    return crates

def move_part_2(crates, instruction):
    num_crates, start, end = instruction
    moved_crates = crates[start-1][-num_crates:]
    del crates[start-1][-num_crates:]
    crates[end-1].extend(moved_crates)
    return crates

def solve_part_1(crates, instructions):
    crates = parse_crates(crates[:-1], crates[-1])
    instructions = parse_instructions(instructions)
    for instruction in instructions:
        crates = move_part_1(crates, instruction)
    print("Part 1:", "".join([stack[-1] for stack in crates]))

def solve_part_2(crates, instructions):
    crates = parse_crates(crates[:-1], crates[-1])
    instructions = parse_instructions(instructions)
    for instruction in instructions:
        crates = move_part_2(crates, instruction)
    print("Part 2:", "".join([stack[-1] for stack in crates]))

def main():
    crates, instructions = delimit(lines)
    solve_part_1(crates, instructions)
    solve_part_2(crates, instructions)

def delimit(lst, delimiter=''):
    delimited = []
    current_group = []
    for value in lst:
        if value != delimiter:
            current_group.append(value)
        else:
            delimited.append(current_group)
            current_group = []

    delimited.append(current_group)

    return delimited


if __name__ == '__main__':
    main()
