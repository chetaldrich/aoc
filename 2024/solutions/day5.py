from aocd import data
from functools import cmp_to_key

def main():
    rules, updates = parse()
    print("Part 1:", sum(mid(update) for update in updates if valid_update(rules, update)))
    print("Part 2:", sum(mid(sort_by_rules(rules, update)) for update in updates if not valid_update(rules, update)))

def sort_by_rules(rules, update):
    return sorted(update, key=cmp_to_key(lambda x, y: -1 if [x,y] in rules else 1))

def valid_update(rules, update):
    update = {int(v): i for i, v in enumerate(update)}
    for first, second in rules:
        if first in update and second in update and update[first] > update[second]:
            return False
    return True

def mid(update):
    return update[len(update) // 2]

def parse():
    all_data = data.split('\n')
    i = all_data.index('')
    rules = [[int(v) for v in rule.split('|')] for rule in all_data[:i]]
    updates = [[int(v) for v in update.split(',')] for update in all_data[i+1:]]
    return rules, updates

if __name__ == '__main__':
    main()
