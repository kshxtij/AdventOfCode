# Path: src/2022/day7.py
import os

def parse_input():
    dirs = {}
    subdirs = {}
    curdir = None
    with open("input/2022/day7.input.txt") as f:
        lines = f.read().strip().split("\n")
        for line in lines:
            if len(line.strip()) == 0: continue
            if line[0] == '$':
                _, cmd, *args = line.split()
                if cmd == 'cd':
                    path ,= args
                    if path[0] == '/':
                        curdir = path
                    else:
                        curdir = os.path.normpath(os.path.join(curdir, path))
                    if curdir not in dirs:
                        dirs[curdir] = 0
                        subdirs[curdir] = []
            else:
                sz, fname = line.split()
                if sz != 'dir':
                    dirs[curdir] += int(sz)
                else:
                    subdirs[curdir].append(os.path.normpath(os.path.join(curdir, fname)))
    return (dirs, subdirs)

dirsizes = {}
def dirsize(dirname, dirs, subdirs):
    dsize = dirs[dirname]
    for i in subdirs[dirname]:
        if i in dirs:
            dsize += dirsize(i, dirs, subdirs)
    return dsize

def task1(data):
    dirs, subdirs = data
    totsize = 0
    for d in dirs:
        dsize = dirsize(d, dirs, subdirs)
        if dsize <= 100000:
            totsize += dsize
    print(totsize)


def task2(data):
    dirs, subdirs = data
    totsize = dirsize('/', dirs, subdirs)
    unused = 70000000 - totsize
    ms = None
    for d in dirs:
        ds = dirsize(d, dirs, subdirs)
        if unused + ds >= 30000000:
            if ms is None or ms > ds:
                ms = ds
    print(ms)


if __name__ == "__main__":
    data = parse_input()
    task1(data)
    task2(data)
