# Path: src/2022/day6.py
def parse_input():
    with open("input/2022/day6.input.txt") as f:
        return f.read().strip()


def find(data, length):
    for i in range(len(data)-length):
        if len(set(data[i:i+length])) == length:
            break

    return i+length


def task1(data):
    print(find(data, 4))


def task2(data):
    print(find(data, 14))


if __name__ == "__main__":
    data = parse_input()
    task1(data)
    task2(data)
