## STAR 1
def star1():
    with open("input.txt", "r") as f:
        data = [int(x) for x in f.readlines()]
        return (sum(x < y for x, y in zip(data, data[1:])))

## STAR 2
def star2():
    with open("input.txt", "r") as f:
        data = [int(x) for x in f.readlines()]
        grouped = [sum(data[i:i + 3]) for i in range(len(data) - 2)]
        return (sum(x < y for x, y in zip(grouped, grouped[1:])))

def main():
    print("Star 1: ", star1())
    print("Star 2: ", star2())

if __name__ == '__main__':
    main()