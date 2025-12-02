from aocd import data 
from math import trunc, fmod

def solve(part2=False):
    result, dial = 0, 50
    for turn in parse(data):
        if part2:
            result += abs(trunc(turn / 100))
            result += fmod(turn, 100) + dial > 100 or fmod(turn, 100) + dial < 0 and dial != 0
        dial = (dial + turn) % 100
        result += dial == 0
    return result

def parse(data):
    for turn in data.split("\n"):
        factor = 1 if turn[0] == "R" else -1
        yield factor * int(turn[1:])

def main():
    print(solve())
    print(solve(True))

if __name__ == '__main__':
    main()
