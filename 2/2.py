## STAR 1
def star1():
    with open("input.txt", "r") as f:
        h = 0
        d = 0
        data = f.readlines()
        for x in data:
            splitted = x.split(" ")
            if splitted[0] == "forward":
                h += int(splitted[1])
            elif splitted[0] == "down":
                d += int(splitted[1])
            elif splitted[0] == "up":
                d -= int(splitted[1])
        return h * d


## STAR 2
def star2():
    with open("input.txt", "r") as f:
        h = 0
        d = 0
        a = 0
        data = f.readlines()
        for x in data:
            splitted = x.split(" ")
            if splitted[0] == "forward" and a != 0:
                h += int(splitted[1])
                d += int(splitted[1]) * a
            if splitted[0] == "forward" and a == 0:
                h += int(splitted[1])
            elif splitted[0] == "down":
                a += int(splitted[1])
            elif splitted[0] == "up":
                a -= int(splitted[1])
        return h * d
            

def main():
    print("Star 1: ", star1())
    print("Star 2: ", star2())

if __name__ == '__main__':
    main()