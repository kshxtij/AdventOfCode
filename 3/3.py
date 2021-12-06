## STAR 1
def star1():
    with open("input.txt", "r") as f:
        data = f.readlines()
        gamma = ""
        epsilon = ""
        for i in range (len(data[0]) - 1):
            zeroes = 0
            ones = 0
            for line in data:
                if line[i] == "0":
                    zeroes += 1
                else:
                    ones += 1
            if zeroes > ones:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"
        return int(gamma,2) * int(epsilon,2)

## STAR 2

def star2():
    with open("input.txt", "r") as f:
        inp = f.read().strip().split('\n') 
    valid = inp
    for i in range(len(valid[0])):
        ones = sum([binary[i] == '1' for binary in valid])
        zeroes = sum([binary[i] == '0' for binary in valid])
        if ones >= zeroes:
            valid = [binary for binary in valid if binary[i] == '1']
        else:
            valid = [binary for binary in valid if binary[i] == '0']

        if len(valid) == 1:
            oxygen = int(valid[0], 2)

    valid = inp
    for i in range(len(valid[0])):
        ones = sum([binary[i] == '1' for binary in valid])
        zeroes = sum([binary[i] == '0' for binary in valid])
        if ones < zeroes:
            valid = [binary for binary in valid if binary[i] == '1']
        else:
            valid = [binary for binary in valid if binary[i] == '0']

        if len(valid) == 1:
            co2 = int(valid[0], 2)

    return oxygen * co2



def main():
    print("Star 1: ", star1())
    print("Star 2:", star2())

if __name__ == '__main__':
    main()