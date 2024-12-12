from aocd import data
from functools import cache

def main():
    stones = parse()
    print("Part 1:", sum(blink(stone, 25) for stone in stones))
    print("Part 2:", sum(blink(stone, 75) for stone in stones))

def split(stone):
    return str(int(stone[0:len(stone)//2])), str(int(stone[len(stone)//2:]))

@cache
def blink(stone, times):
    if times == 0:
        return 1
    stones = []
    if stone == '0':
        stones.append('1')
    elif len(stone) % 2 == 0:
        stones.extend(split(stone))
    else:
        stones.append(str(int(stone) * 2024))
    return sum(blink(stone, times - 1) for stone in stones)

def parse():
    return data.split()

if __name__ == '__main__':
    main()
