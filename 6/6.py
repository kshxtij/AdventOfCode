from collections import defaultdict

def solve(data, days):
    fish = defaultdict(int)
    for times in data.split(','):
        n = int(times)
        fish[n] += 1
    for _ in range(days):
        stepped = defaultdict(int)
        for value, count in fish.items():
            if value > 0:
                stepped[value-1] += count
            else:
                stepped[6] += count
                stepped[8] += count
        fish = stepped
    return sum(fish.values())


if __name__ == '__main__':
    input_data = open("input.txt").read()
    ans1 = solve(input_data,80)
    print("Day 1: ", ans1)
    ans2 = solve(input_data,256)
    print("Day 2: ", ans2)
                
    