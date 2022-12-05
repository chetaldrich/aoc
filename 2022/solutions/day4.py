from aocd import lines

def contains(first, second):
    return (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1])

def overlaps(first, second):
    for end in second:
        if first[0] <= end <= first[1]:
            return True
    return contains(first, second)

def parse_group(interval):
    return [int(i) for i in interval.split("-")]

def main():
    groups = []
    for line in lines:
        first, second = line.split(",")
        group = (parse_group(first), parse_group(second))
        groups.append(group)

    print("Part 1:", sum([1 if contains(first, second) else 0 for first, second in groups]))
    print("Part 2:", sum([1 if overlaps(first, second) else 0 for first, second in groups]))


if __name__ == '__main__':
    main()
