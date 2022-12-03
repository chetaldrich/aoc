from aocd import data
import string


def main():
    split = [
        (line[0 : len(line) // 2], line[len(line) // 2 :]) for line in data.splitlines()
    ]
    letters = [list(set(first).intersection(set(second)))[0] for first, second in split]
    result = [string.ascii_letters.index(letter) + 1 for letter in letters]

    groups = list(zip(*(iter(data.splitlines()),) * 3))
    letters_2 = [
        list(set(first).intersection(set(second)).intersection(set(third)))[0]
        for first, second, third in groups
    ]
    result_2 = [string.ascii_letters.index(letter) + 1 for letter in letters_2]

    print("Part 1:", sum(result))
    print("Part 2:", sum(result_2))


if __name__ == "__main__":
    main()
