# Path: src/2022/day1.py
import re

def parse_input():
    with open("input/2022/day1.input.txt") as f:
      return [sum(map(int, re.findall('\d+', block))) for block in f.read().split('\n\n')]

def task1(data):
  print(max(data))

def task2(data):
  print(sum(sorted(data, reverse=True)[:3]))

if __name__ == "__main__":
  data = parse_input()
  task1(data)
  task2(data)
