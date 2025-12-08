with open("input/day01.txt", "r") as puzzleInput:
    instructions = [line.strip() for line in puzzleInput]

posA, posB, partA, partB = 50, 50, 0, 0

for instruction in instructions:
    distance = int(instruction[1:])
    if instruction[0] == "L":
        posA -= distance
        while distance > 0:
            posB -= 1
            distance -= 1
            if posB < 0:
                posB += 100
            if posB == 0:
                partB += 1
    else:
        posA += distance
        while distance > 0:
            posB += 1
            distance -= 1
            if posB > 99:
                posB -= 100
            if posB == 0:
                partB += 1
    if posA % 100 == 0:
        partA += 1

print(f"Part 1: {partA}")
print(f"Part 2: {partB}")