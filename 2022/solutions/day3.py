from aocd import data
import string


def score(letter):
    return string.ascii_letters.index(letter) + 1


def find_common_letter(groups):
    result = None
    for group in groups:
        if result:
            result = result.intersection(set(group))
        else:
            result = set(group)
    return list(result)[0]


def score_groups(all_groups):
    return sum(score(find_common_letter(groups)) for groups in all_groups)


def main():
    groups = [
        (line[: len(line) // 2], line[len(line) // 2 :]) for line in data.splitlines()
    ]
    groups_2 = list(zip(*(iter(data.splitlines()),) * 3))
    print("Part 1:", score_groups(groups))
    print("Part 2:", score_groups(groups_2))


if __name__ == "__main__":
    main()
