with open("input/day07.txt", "r") as puzzleInput:
    manifold = [list(line.strip()) for line in puzzleInput]

a1, timelines = 0, [[0 for _ in row] for row in manifold]

for y, row in enumerate(manifold):
    for x, cell in enumerate(row):
        if cell == "S":
            timelines[y][x] = 1
        elif cell == "^":
            timelines[y][x-1] += timelines[y-1][x]
            timelines[y][x+1] += timelines[y-1][x] + timelines[y-1][x+1]
            if timelines[y-1][x] > 0:
                a1 += 1
        else:
            timelines[y][x] = max(timelines[max(y-1,0)][x],timelines[y][x])

print(f"Part one: {a1}")
print(f"Part two: {sum([n for n in timelines[-1]])}")