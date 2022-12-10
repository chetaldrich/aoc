from aocd import lines


def parse(lines):
    result = []
    for line in lines:
        if line.startswith("addx"):
            _, value = line.split()
            result.extend([0, int(value)])
        else:
            result.append(0)
    return result


def run(register, instructions, cycles):
    results = []
    screen = []
    for i, instruction in enumerate(instructions):
        if i + 1 in cycles:
            results.append(register * (i + 1))
        screen.append(pixel(i % 40, register))
        register += instruction
    return results, screen


def pixel(position, sprite_center):
    return "#" if position in range(sprite_center - 1, sprite_center + 2) else "."


def print_screen(screen):
    for row in range(0, len(screen), 40):
        print("".join(screen[row : row + 40]))


def main():
    cycles = [20 + (40 * i) for i in range(6)]
    instructions = parse(lines)
    results, screen = run(1, instructions, cycles)
    print("Part 1:", sum(results))
    print("Part 2:")
    print_screen(screen)


if __name__ == "__main__":
    main()
