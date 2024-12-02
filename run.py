import sys
from importlib import import_module

day = int(sys.argv[1])
part = int(sys.argv[2])

print(f"Running solution for day {day} part {part}:")

solution = import_module(f"src.day{day}.main")
getattr(solution, f"part_{part}")()
