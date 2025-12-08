with open("input/day02.txt", "r") as puzzleInput:
    IDs = [tuple(map(int, group.strip().split('-'))) for group in puzzleInput.readline().split(',')]

total = 0

for start, end in IDs:
    startString, endString = str(start), str(end)
    startLen, endLen = len(startString), len(endString)
    if startLen % 2 != 0 and endLen % 2 != 0 and startLen == endLen:
        continue

    midStart = 1 if startLen == 1 else startLen // 2
    midEnd = (endLen + 1) // 2 if endLen % 2 != 0 else endLen // 2
    
    startHalf = 0 if midStart == 1 else startString[:midStart]
    endHalf = endString[:midEnd]
    
    for i in range(int(startHalf), int(endHalf) + 1):
        candidate = int(str(i) + str(i))
        if start <= candidate <= end:
            total += candidate

print(f"Part 1 Answer: {total}")