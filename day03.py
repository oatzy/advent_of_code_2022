import string

def part1():
    total = 0
    with open("day03.txt", "r") as f:
        for line in f:
            line = line.strip()
            l = len(line)//2
            dup = [c for c in line[:l] if c in line[l:]]
            total += string.ascii_letters.index(dup[0]) + 1
    return total

def part2():
    total = 0
    with open("day03.txt", "r") as f:
        lines = [l.strip() for l in f]
    for i in range(0, len(lines), 3):
        items = lines[i:i+3]
        dup = [c for c in items[0] if c in items[1] and c in items[2]]
        total += string.ascii_letters.index(dup[0]) + 1
    return total

if __name__ == '__main__':
    print(part1())
    print(part2())
