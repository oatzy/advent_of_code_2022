import re
from collections import defaultdict

def part1():
    with open("day05.txt", "r") as f:
        init, moves = f.read().split("\n\n")

    stacks = defaultdict(list)
    for line in init.splitlines()[::-1]:
        for n, c in enumerate(line):
            if c.isalpha():
                stacks[1 + (n-1)//4].append(c)

    for line in moves.splitlines():
        count, from_, to_ = re.match("move (\d+) from (\d+) to (\d+)", line).groups()
        # part1
        #for _ in range(int(count)):
        #    stacks[int(to_)].append(stacks[int(from_)].pop())
        # part2
        stacks[int(to_)].extend(stacks[int(from_)][-int(count):])
        stacks[int(from_)] = stacks[int(from_)][:-int(count)]

    # dicts are ordered in py3
    for s in stacks.values():
        print(s[-1], end='')

if __name__ == '__main__':
    part1()
