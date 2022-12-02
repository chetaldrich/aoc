from aocd import data

points = {"X": 1, "Y": 2, "Z": 3}

outcomes_part_1 = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

outcomes_part_2 = {"X": 0, "Y": 3, "Z": 6}

plays = {
    "X": {"A": "Z", "B": "X", "C": "Y"},
    "Y": {"A": "X", "B": "Y", "C": "Z"},
    "Z": {"A": "Y", "B": "Z", "C": "X"},
}


def score(theirs, yours):
    return points[yours] + outcomes_part_1[theirs][yours]


def score_2(theirs, yours):
    return points[plays[yours][theirs]] + outcomes_part_2[yours]


def main():
    matches = [line.split(" ") for line in data.splitlines()]
    scores = sum(score(theirs, yours) for theirs, yours in matches)
    scores_2 = sum(score_2(theirs, yours) for theirs, yours in matches)
    print("Part 1:", scores)
    print("Part 2:", scores_2)


if __name__ == "__main__":
    main()
