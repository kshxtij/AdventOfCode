with open("input.txt") as f:
	data = f.read()

def permutations(string):
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string.replace(char, "", 1))]
    return permutation_list

digits = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

task1,task2 = 0,0
for line in data.splitlines():
    parts = line.split(" | ")
    calib = ["".join(sorted(s)) for s in parts[0].split()]
    target = ["".join(sorted(s)) for s in parts[1].split()]
    for p in permutations("abcdefg"):
        translate_table = str.maketrans("abcdefg", "".join(p))
        translated = ["".join(sorted(c.translate(translate_table))) for c in calib]
        if all(t in digits for t in translated):
            translated2 = [digits["".join(sorted(c.translate(translate_table)))] for c in target]
            task1 += translated2.count(1) + translated2.count(4) + translated2.count(7) + translated2.count(8)
            task2 += int("".join(str(n) for n in translated2))
print("Part 1: ", task1)
print("Part 2: ", task2)