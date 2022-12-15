
def visible(trees):
    visible = set()

    columnmax = {}
    for i, row in enumerate(trees):
        rowmax = -1
        for j, n in enumerate(row):
            if n > rowmax:
                visible.add((i, j))
                rowmax = n
            if n > columnmax.setdefault(j, -1):
                visible.add((i,j))
                columnmax[j] = n
    return visible


def visible_rev(trees):
    visible = set()

    h = len(trees)
    w = len(trees[0])

    columnmax = {}
    for i in range(h):
        rowmax = -1
        for j in range(w):
            I,J = h-i-1,w-j-1
            n = trees[I][J]
            if n > rowmax:
                visible.add((I, J))
                rowmax = n
            if n > columnmax.setdefault(J, -1):
                visible.add((I,J))
                columnmax[J] = n
    return visible

def scenic(trees, pos):
    h = len(trees)
    w = len(trees[0])

    res = 1

    x,y = pos
    n = trees[y][x]
    
    t = 0
    x -= 1
    while x >= 0:
        t += 1
        if trees[y][x] >= n:
            break
        x -= 1

    res *= t

    t = 0
    x = pos[0] + 1
    while x < w:
        t += 1
        if trees[y][x] >= n:
            break
        x += 1
    res *= t

    x,y = pos
    t = 0
    y -= 1
    while y >= 0:
        t += 1
        if trees[y][x] >= n:
            break
        y -= 1
    res *= t

    y = pos[1] + 1
    t = 0
    while y < h:
        t += 1
        if trees[y][x] >= n:
            break
        y += 1
    res *= t

    return res 

def part2(trees):
    m = max(scenic(trees, (x,y)) for y in range(1, len(trees)-1) for x in range(1,len(trees[0])-1))
    print(m)

def part1():
    with open("day08.txt", "r") as f:
        trees = [list(map(int, line.strip())) for line in f]

    vis = visible(trees)
    vis.update(visible_rev(trees))

    #print(vis)
    print(len(vis))
    part2(trees) 


if __name__ == '__main__':
    part1()
