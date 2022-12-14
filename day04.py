def contained(a, b):
    return (a[0] <= b[0] and a[1] >= b[1])

def overlaps(a, b):
    return (a[0] <= b[0] <= a[1]) or (a[1] >= b[1] >= a[0])

def main():
    contain = 0
    overlap = 0
    with open("day04.txt", "r") as f:
        for line in f:
            a, b = [list(map(int, i.split("-"))) for i in line.split(",")]
            contain += contained(a,b) or contained(b,a)
            overlap += overlaps(a,b) or overlaps(b,a)
    print(contain)
    print(overlap)

if __name__ == '__main__':
    main()
