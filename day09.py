
def follow(h, t):
    if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        t = (t[0] + (h[0]-t[0])/(abs(h[0]-t[0]) or 1), t[1] + (h[1]-t[1])/(abs(h[1]-t[1]) or 1))
    return t

def main(l):
    visited = set([(0,0)])
    knots = [(0,0) for _ in range(l)]
    with open("day09.txt", "r") as f:
        for line in f:
            d,n = line.split()
            for _ in range(int(n)):
                h = knots[0]
                if d == 'R':
                    h = (h[0] + 1, h[1])
                elif d == 'L':
                    h = (h[0] - 1, h[1])
                elif d == 'U':
                    h = (h[0], h[1] - 1)
                else:
                    h = (h[0], h[1] + 1)
                knots[0] = h
                for i, t in enumerate(knots[1:]):
                    knots[i+1] = follow(knots[i], t)
                visited.add(knots[-1])
            #print(knots)
    return len(visited)

if __name__ == '__main__':
    print(main(2))
    print(main(10))
