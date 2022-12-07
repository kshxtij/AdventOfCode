# # Path: src/2022/day5.py
def parse_input():
    with open('input/2022/day5.input.txt', mode='r') as f:

        line = f.readline()

        row = [line[i * 4 + 1] for i in range(len(line) // 4)]
        crates = [[] for i in range(len(row))]

        while row[0].isalpha() or row[0] == ' ':
            crates = [crates[i] + [row[i]] if row[i] != ' ' else [] for i in range(len(crates))]
            line = f.readline()
            row = [line[i * 4 + 1] for i in range(len(line) // 4)]

        f.readline()
        commands = [line.split(' ') for line in f]
        return crates, commands


def task1(data):
    crates, commands = data
    for command in commands:
        quantity = int(command[1])
        source = int(command[3]) - 1
        target = int(command[5]) - 1
        to_move = crates[source][:quantity]
        crates[source] = crates[source][quantity:]
        to_move.reverse()
        crates[target] = to_move + crates[target]

    print(''.join([crate[0] for crate in crates]))


def task2(data):
    crates, commands = data
    for command in commands:
        quantity = int(command[1])
        source = int(command[3]) - 1
        target = int(command[5]) - 1
        to_move = crates[source][:quantity]
        crates[source] = crates[source][quantity:]
        crates[target] = to_move + crates[target]

    print(''.join([crate[0] for crate in crates]))


if __name__ == "__main__":
    data = parse_input()
    task1(data)
    data = parse_input()
    task2(data)
