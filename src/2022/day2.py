# Path: src/2022/day2.py
def parse_input():
    with open("input/2022/day2.input.txt") as f:
        return [(line[0], line[1]) for line in [line.split(" ") for line in f.read().splitlines()]]

R = {
      "A": 1, # rock
      "B": 2, # paper
      "C": 3, # sciss
    }
Q = {
    "X": 1,
    "Y": 2,
    "Z": 3
    }  

def task1(data):
  score = 0
  for (enemy, you) in data:
    if R[enemy] == Q[you]:
      score += 3
    elif enemy == "A" and you == "Y" or enemy == "B" and you == "Z" or enemy == "C" and you == "X":
      score += 6
    score += Q[you]

  print(score)

def task2(data):
  score = 0
  for (enemy, you) in data:
    play = None
    if you == "X":
      score += 0
      if enemy == "A":
        play = "Z"
      elif enemy == "B":
        play = "X"
      elif enemy == "C":
        play = "Y"
    elif you == "Y":
      score += 3
      if enemy == "A":
        play = "X"
      elif enemy == "B":
        play = "Y"
      elif enemy == "C":
        play = "Z"
    elif you == "Z":
      score += 6
      if enemy == "A":
        play = "Y"
      elif enemy == "B":
        play = "Z"
      elif enemy == "C":
        play = "X"

    score += Q[play]

  print(score)

if __name__ == "__main__":
  data = parse_input()
  task1(data)
  task2(data)