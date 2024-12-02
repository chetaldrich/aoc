from aocd import data

def main():
    first, second = parse(data)
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
