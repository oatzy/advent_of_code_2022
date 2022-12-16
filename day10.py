
def part1():
    total = 0

    reg = 1
    cycle = 1

    with open("day10.txt", "r") as f:
        for line in f:
            line = line.strip()

            if line == "noop":
                cycle += 1
                if cycle % 40 == 20:
                    total += cycle * reg

            else:
                inc = int(line.split()[-1])
                cycle += 1
                if (cycle) % 40 == 20:
                    total += cycle * reg
                reg += inc
                cycle +=1
                if (cycle) % 40 == 20:
                    total += cycle * reg

    print(total)


def render(cycle, sx):
    x = (cycle % 40) - 1
    y = cycle // 40
                          
    if x == 0:
        print()
                          
    #print(x, sx)
    #return
    if abs(sx -x) <= 1:
        print('#', end='')
    else:
        print('.', end='')

def part2():
    sx = 1

    cycle = 0

    with open("day10.txt", "r") as f:
        for line in f:
            line = line.strip()
            
            cycle += 1
            render(cycle, sx)

            if line == "noop":
                continue

            cycle += 1
            render(cycle, sx)

            inc = int(line.split()[-1])
            sx += inc
    print()        

if __name__ == '__main__':
    part1()
    part2()
