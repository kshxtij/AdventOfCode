# Path: src/2022/day8.py
import numpy as np

def parse_input():
    with open("input/2022/day8.input.txt") as f:
        return np.array([list(map(int, line)) for line in f.read().splitlines()])

def distance(line, tree):
    i = 0
    for i, x in enumerate(line, 1):
        if x >= tree:
            break
    return i

def task1(data):
    visible = 0 
    for y, x in np.ndindex(data.shape):
        tree = data[y, x]
        visible += int(
            all(data[y, :x] < tree) or 
            all(data[y, x + 1:] < tree) or
            all(data[y + 1:, x] < tree) or
            all(data[:y, x] < tree)
        )
    print(visible)

def task2(data):
    score = 0
    for y, x in np.ndindex(data.shape):
        tree = data[y, x]
        score = max((distance(reversed(data[y, :x]), tree) *
                     distance(data[y, x + 1:], tree) * 
                     distance(reversed(data[:y, x]), tree) * 
                     distance(data[y + 1:, x], tree)), 
                score)
    print(score)

if __name__ == "__main__":
  data = parse_input()
  task1(data)
  task2(data)