from aocd import numbers
from collections import Counter


def main():
    fish = Counter(numbers)
    print("Part 1:", run_full_simulation(fish, 80))
    print("Part 2:", run_full_simulation(fish, 256))


def run_full_simulation(fish, days):
    result = fish
    for _ in range(days):
        result = run_simulation(result)
    return sum(result.values())


def run_simulation(fish):
    result = Counter()
    for stage, num_fish in fish.most_common():
        if stage == 0:
            result[6] += num_fish
            result[8] += num_fish
        else:
            result[stage - 1] += num_fish
    return result


if __name__ == "__main__":
    main()
