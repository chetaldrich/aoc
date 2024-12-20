from aocd import data
from util import delimit
from functools import cache

def main():
    matcher, onsens = parse()
    print("Part 1:", len([o for o in onsens if matcher.variations(o)]))
    print("Part 2:", sum([matcher.variations(o) for o in onsens]))

class PatternMatcher:
    def __init__(self, patterns):
        self.patterns = patterns

    @cache
    def variations(self, onsen):
        if onsen == "":
            return 1
        return sum(self.variations(onsen[len(p):]) for p in self.patterns if onsen.startswith(p))

def parse():
    patterns, onsens = delimit(data.splitlines())
    patterns = [p.strip() for p in patterns[0].split(",")]
    return PatternMatcher(patterns), onsens

if __name__ == '__main__':
    main()
