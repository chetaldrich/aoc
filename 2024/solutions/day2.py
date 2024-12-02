from aocd import data

def main():
    reports = parse()
    print("Part 1:", sum(1 for report in reports if safe(diffs(report))))
    print("Part 2:", sum(1 for report in reports if safe_with_dampener(report)))

def diffs(report):
    return [report[i+1] - report[i] for i in range(len(report) - 1)]

def dampen(report, i):
    return report[:i] + report[i+1:]

def safe(diffs):
    all_positive = all(diff > 0 for diff in diffs)
    all_negative = all(diff < 0 for diff in diffs)
    diffs_in_range = all(abs(diff) <= 3 and abs(diff) >= 1 for diff in diffs)
    return diffs_in_range and (all_positive or all_negative)

def safe_with_dampener(report):
    dampened_reports = [report] + [dampen(report, i) for i in range(len(report))]
    return any(safe(diffs(report)) for report in dampened_reports)

def parse():
    return [[int(a) for a in line.split()] for line in data.split('\n')]

if __name__ == '__main__':
    main()
