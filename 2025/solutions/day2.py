from aocd import data
from math import ceil
from itertools import chain

def parse(data):
    return [[int(v) for v in r.split("-")] for r in data.split(",")]

def solve(ranges, f):
    return sum(chain.from_iterable(invalid(*r, f) for r in ranges))

def invalid(start, end, f):
    return [i for i in range(start, end+1) if not f(str(i))]

def divisors(value):
    return [i for i in range(1, int(value) + 1) if int(value) % i == 0 and i > 1]

def valid_part_1(s):
    return len(s) % 2 != 0 or s[:ceil(len(s)/2)] != s[ceil(len(s)/2):]

def valid_part_2(value):
    for d in divisors(len(value)):
        step = int(len(value) / d)
        windows = [value[i:i+step] for i in range(0, len(value), step)]
        if all(w == windows[0] for w in windows):
            return False
    return True

def main():
    ranges = parse(data)
    print(solve(ranges, valid_part_1))
    print(solve(ranges, valid_part_2))

if __name__ == '__main__':
    main()
