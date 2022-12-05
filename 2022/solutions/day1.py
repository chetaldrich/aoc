from aocd import data

def main():
    elves = delimit(data.splitlines())
    totals = [sum([int(c) for c in elf]) for elf in elves]
    print('Part 1:', max(totals))
    print('Part 2:', sum(sorted(totals, reverse=True)[0:3]))

def delimit(lst, delimiter=''):
    delimited = []
    current_group = []
    for value in lst:
        if value != delimiter:
            current_group.append(value)
        else:
            delimited.append(current_group)
            current_group = []
    delimited.append(current_group)
    return delimited

if __name__ == '__main__':
    main()
