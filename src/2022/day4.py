# Path: src/2022/day4.py
def parse_input():
    with open("input/2022/day4.input.txt") as f:
        return f.read().splitlines()


def task1(data):
    count1 = 0
    for line in data:
        firstelf, secondelf = line.split(",")
        firstelfstart, firstelfend = firstelf.split("-")
        secondelfstart, secondelfend = secondelf.split("-")

        if int(firstelfstart) <= int(secondelfstart) and int(firstelfend) >= int(secondelfend):
            count1 += 1
        elif int(secondelfstart) <= int(firstelfstart) and int(secondelfend) >= int(firstelfend):
            count1 += 1

    print(count1)


def task2(data):
    count2 = 0
    for line in data:
        firstelf, secondelf = line.split(",")
        firstelfstart, firstelfend = firstelf.split("-")
        secondelfstart, secondelfend = secondelf.split("-")

        if int(firstelfend) >= int(secondelfstart) and int(firstelfstart) <= int(secondelfend):
            count2 += 1

    print(count2)


if __name__ == "__main__":
    data = parse_input()
    task1(data)
    task2(data)
