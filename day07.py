from dataclasses import dataclass, field
from typing import List
from pathlib import Path

@dataclass
class File:
    name: str
    size: int

@dataclass
class Dir:
    name: str
    children: List = field(default_factory=list)
    _size: int = None
    
    @property
    def size(self):
        if self._size is None:
            self._size = sum(c.size for c in self.children)
        return self._size


def main():
    pwd = None
    tree = {Path("/"): Dir('/')}
    
    with open("day07.txt", "r") as f:
        for line in f:
            if line.startswith("$ ls"):
                continue
            if line.startswith("$ cd"):
                to_ = line.split()[2]
                if to_ == '/':
                    pwd = Path("/")
                elif to_ == '..':
                    pwd = pwd.parent
                else:
                    pwd = pwd.joinpath(to_)
            else:
                size, name = line.split()
                path = pwd.joinpath(name)
                if size == 'dir':
                    inode = tree.setdefault(path, Dir(name))
                else:
                    inode = tree.setdefault(path, File(name, int(size)))
                tree[pwd].children.append(inode)

    total = 0
    for path, inode in tree.items():
        if isinstance(inode, Dir):
            #print(str(path), inode.size, type(inode))
            s = inode.size
            if s <= 100000:
                total += s

    print(total)

    free = 70000000 - tree[Path("/")].size
    need = 30000000 - free

    delete = min(i.size for i in tree.values() if isinstance(i, Dir) and i.size >= need)
    print(delete)


if __name__ == '__main__':
    main()
