from math import prod

with open("input/day06.txt", "r") as puzzleInput:
    grid = [list(line) for line in puzzleInput]

a2, problem = 0, []

for i, col in enumerate(list(zip(*grid))):
    if not col[-1].isspace():
        operand = col[-1]
    col_str = ''.join(col).strip('*+ ')
    if col_str:
        problem.append(int(col_str))
    if not col_str or i == len(grid[0]) - 2:
        a2 += sum(problem) if operand == "+" else prod(problem)
        problem.clear()
    
print(f"Part two answer: {a2}")