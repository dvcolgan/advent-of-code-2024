import sys
from importlib import import_module

day = int(sys.argv[1])

print(f"Running solution for day {day}")

solution = import_module(f"src.day{day}.main")
solution.main()
