
def main(n):
    with open("day06.txt", "r") as f:
        s = f.read()
    for i in range(n, len(s)):
        if len(set(s[i-n:i])) == n:
            return i

if __name__ == '__main__':
    print(main(4))
    print(main(14))
