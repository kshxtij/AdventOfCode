# Path: src/2022/day9.py
def parse_input():
    with open("input/2022/day9.input.txt") as f:
        return [(d[0], int(d[1])) for d in [tuple(line.split(" ")) for line in f.read().splitlines()]]

offset = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def task1(data):
    hx, hy = 0, 0
    tx, ty = 0, 0
    seen = {(0, 0)}
    for d, n in data:
        dx, dy = offset[d]
        for _ in range(n):
            hx += dx
            hy += dy
            while max(abs(tx - hx), abs(ty - hy)) > 1:
                if abs(tx - hx) > 0:
                    tx += 1 if hx > tx else -1
                if abs(ty - hy) > 0:
                    ty += 1 if hy > ty else -1
                seen.add((tx, ty))
    print(len(seen))

def task2(data):
    rope = [(0, 0)] * 10
    seen = set()
    for d, n in data:
        dx, dy = offset[d]
        for _ in range(n):
            hx, hy = rope[0]
            rope[0] = hx + dx, hy + dy

            for i in range(1, len(rope)):
                px, py = rope[i - 1]
                kx, ky = rope[i]
                while max(abs(kx - px), abs(ky - py)) > 1:
                    if abs(kx - px) > 0:
                        kx += 1 if px > kx else -1
                    if abs(ky - py) > 0:
                        ky += 1 if py > ky else -1
                rope[i] = kx, ky
            seen.add(rope[-1])
    print(len(seen))

if __name__ == "__main__":
  data = parse_input()
  task1(data)
  task2(data)
