from aocd import data
from collections import Counter

def main():
    first, second = parse(data)
    part1(first, second)
    part2(first, second)


def part2(first, second):
    second = Counter(second)
    print(sum(a * second[a] for a in first))

def part1(first, second):
    result = 0
    for a, b in zip(sorted(first), sorted(second)):
        result += abs(int(a) - int(b))
    print(result)

def parse(data):
    first, second = [], []
    for line in data.splitlines():
        one, two = line.split()
        first.append(int(one))
        second.append(int(two))
    return first, second


if __name__ == '__main__':
    main()
