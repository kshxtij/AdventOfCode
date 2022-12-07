# Path: src/2022/day3.py
def parse_input():
    with open("input/2022/day3.input.txt") as f:
        return f.readlines()


def task1(data):
    prios = 0
    for line in data:
        x = len(line)
        part1 = line[:x//2]
        part2 = line[x//2:]
        in_both = set(part1).intersection(set(part2))
        prios += sum([ord(c) - 96 if c.islower() else ord(c) - 38 for c in in_both])

    print(prios)


def task2(data):
    prios = 0
    for i in range(0, len(data), 3):
        for item in data[i]:
            if (item in data[i+1]) and (item in data[i+2]):
                prios += ord(item) - 96 if item.islower() else ord(item) - 38
                break
    print(prios)


if __name__ == "__main__":
    data = parse_input()
    task1(data)
    task2(data)
