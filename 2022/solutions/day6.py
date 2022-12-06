from aocd import data


def solve(signal, len_start):
    for i in range(len(signal[:-len_start])):
        if len(set(signal[i : i + len_start])) == len_start:
            return i + len_start


def main():
    print("Part 1:", solve(data, 4))
    print("Part 2:", solve(data, 14))


if __name__ == "__main__":
    main()
