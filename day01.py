
def main():
    with open("day01.txt", "r") as f:
        totals = sorted((sum(map(int, block.splitlines())) for block in f.read().split("\n\n")), reverse=True)
    print(totals[0])
    print(sum(totals[:3]))

if __name__ == '__main__':
    main()
