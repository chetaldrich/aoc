from aocd import data
import re

def main():
    instructions = parse()
    print("Part 1:", sum(eval(instruction) for instruction in instructions if instruction.startswith('mul')))
    print("Part 2:", sum(eval(instruction) for instruction in filter(instructions)))

def filter(instructions):
    active = True
    for instruction in instructions:
        if instruction.startswith('mul') and active:
            yield instruction
        elif instruction.startswith('don\'t'):
            active = False
        elif instruction.startswith('do'):
            active = True

def mul(a, b):
    return a * b

def parse():
    pattern = re.compile(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)')
    return re.findall(pattern, data)

if __name__ == '__main__':
    main()
