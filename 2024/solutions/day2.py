from aocd import data

def main():
    reports = parse()
    print(sum(1 for report in reports if safe(diffs(report))))

def diffs(report):
    diffs = []
    for i in range(len(report) - 1):
        diffs.append(report[i+1] - report[i])
    return diffs

def safe(diffs):
    all_positive = all(diff > 0 for diff in diffs)
    all_negative = all(diff < 0 for diff in diffs)
    if not (all_positive or all_negative):
        return False
    min = 1 if all_positive else -3
    max = 3 if all_positive else -1
    return all(diff >= min and diff <= max for diff in diffs)

def parse():
    return [[int(a) for a in line.split()] for line in data.split('\n')]

if __name__ == '__main__':
    main()
