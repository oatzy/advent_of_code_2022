SCORES = {'X': 1, 'Y': 2, 'Z': 3}

def win(a, b):
    a = {'A': 0, 'B': 1, 'C': 2}[a]
    b = {'X': 0, 'Y': 1, 'Z': 2}[b]
    if a == b:
        return 3
    if (b - a) % 3 == 1:
        return 6
    return 0

def part2(a, b):
    a = {'A': 0, 'B': 1, 'C': 2}[a]
    if b == 'X':
        return (a - 1) % 3 + 1
    elif b == 'Y':
        return a + 1 + 3
    else:
        return (a + 1) % 3 + 1 + 6


def main():
    p1 = 0
    p2 = 0
    with open("day02.txt", "r") as f:
        for line in f:
            a, b = line.split()
            p1 += SCORES[b] + win(a, b)
            p2 += part2(a, b)
    print(p1)
    print(p2)

if __name__ == '__main__':
    main()
