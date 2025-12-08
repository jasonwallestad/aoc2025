import re
import math
numbers, a1 = [], 0

with open("input/day06.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        if "*" in line or "+" in line:
            symbols = re.findall(r"\+|\*", line)
        else:
            numbers.append([int(n) for n in re.findall(r"\d+", line)])

for col in range(len(symbols)):
    problem = []
    for row in range(len(numbers)):
        problem.append(numbers[row][col])
    a1 += sum(problem) if symbols[col] == "+" else math.prod(problem)

print(f"Part 1: {a1}")