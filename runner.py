import os

import requests
token = open("token.txt").read().strip()

from timeit import default_timer as timer
from datetime import datetime
year = datetime.now().year
day = datetime.now().day

from typer import Typer
app = Typer()

from rich.table import Table
from rich.console import Console
console = Console()

template = f"""# Path: src/{year}/day{day}.py
def parse_input():
    with open(".input/{year}/day{day}.input.txt") as f:
        pass

def task1(data):
  pass

def task2(data):
  pass

if __name__ == "__main__":
  data = parse_input()
  task1(data)
  task2(data)
"""

@app.command()
def setup(year: int = year, day: int = day):
  with open(f"src/{year}/day{day}.py", "w") as f:
    f.write(template)

  # check if input file exists
  if not os.path.exists(f"input/{year}/day{day}.input.txt"):
    data = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token})
    with open(f"input/{year}/day{day}.input.txt", "w") as f:
      f.write(data.text)

@app.command()
def run(year: int = year, day: int = day):
  os.system(f"python3 src/{year}/day{day}.py")

if __name__ == "__main__":
    app()