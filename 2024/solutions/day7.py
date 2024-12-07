from aocd import data
from operator import add, mul

def main():
    equations = parse()
    print("Part 1:", sum(left for left, right in equations if check(left, right, [add, mul])))
    print("Part 2:", sum(left for left, right in equations if check(left, right, [add, mul, concat])))

def concat(a, b):
    return int(str(a) + str(b))

def check(left, right, ops, result=0, i=0):
    if i == len(right) or result > left:
        return left == result
    for op in ops:
        if check(left, right, ops, op(result, right[i]), i + 1):
            return True
    return False

def parse():
    result = []
    for line in data.split('\n'):
        first, rest = line.split(':')
        result.append((int(first), [int(v) for v in rest.strip().split()]))
    return result


if __name__ == '__main__':
    main()
