data = [int(n) for n in open("input.txt").read().split(",")]
print(min([sum(abs(n-x) for n in data) for x in range(max(data))]))
print(min([sum(abs(n-x)*(abs(n-x)+1)//2 for n in data) for x in range(max(data))]))