from aocd import lines
from day1 import delimit
from itertools import zip_longest, chain
import functools
from math import prod


def parse(lines):
    return [(eval(left), eval(right)) for left, right in delimit(lines)]


def compare(left, right, level=0, p=False):
    if left == right:
        return 0

    def _compare(left, right, level=0, p=False):
        if p:
            print(f"{'  ' * level}- Compare {left} vs {right}")
        if left is None:
            return (True, True)
        elif right is None:
            return (False, False)
        elif type(left) == int and type(right) == int:
            return (right is not None and left <= right, left < right)
        elif type(left) == list and type(right) == list:
            for l, r in zip_longest(left, right):
                correct, short_circuit = _compare(l, r, level=level + 1, p=p)
                if correct and short_circuit:
                    return (True, True)
                if not correct:
                    return (False, False)
            return (True, False)
        elif type(left) == int and type(right) == list:
            if p:
                print(
                    f"{'  ' * level}- Mixed types; convert {left} to list and try again"
                )
            return _compare([left], right, level=level, p=p)
        elif type(left) == list and type(right) == int:
            if p:
                print(
                    f"{'  ' * level}- Mixed types; convert {right} to list and try again"
                )
            return _compare(left, [right], level=level, p=p)
        else:
            return (False, False)

    return 1 if _compare(left, right, level=level, p=p)[0] else -1


def part_1(groups, p=False):
    solution = 0
    for i, group in enumerate(groups):
        if p:
            print(f"== Pair {i+1} ==")
        result = compare(*group, p=p)
        if p:
            print(result)
        solution += i + 1 if result == 1 else 0
    return solution


def part_2(groups):
    decoder_packets = [[[2]], [[6]]]
    packets = list(chain(*groups)) + decoder_packets
    packets.sort(key=functools.cmp_to_key(compare), reverse=True)
    return prod(
        [i + 1 for i, packet in enumerate(packets) if packet in decoder_packets]
    )


def main():
    groups = parse(lines)
    p = False
    print("Part 1:", part_1(groups, p=p))
    print("Part 2:", part_2(groups))


if __name__ == "__main__":
    main()
