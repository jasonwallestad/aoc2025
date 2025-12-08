with open("input/day02.txt", "r") as puzzleInput:
    IDs = [tuple(map(int, group.strip().split('-'))) for group in puzzleInput.readline().split(',')]

invalid = set()

for start, end in IDs:
    tried = set()
    startStr, endStr = str(start), str(end)
    startLen, endLen = len(startStr), len(endStr)

    midStart = 1 if startLen == 1 else startLen // 2
    midEnd = (endLen + 1) // 2 if endLen % 2 != 0 else endLen // 2
    
    startHalf = 0 if midStart == 1 else startStr[:midStart]
    endHalf = endStr[:midEnd]
    
    for i in range(int(startHalf), int(endHalf) + 1):
        test, repeats = str(i), 2
        while test:
            if test in tried:
                break
            tried.add(test)
            reset = repeats
            while repeats <= endLen:
                candidate = test * repeats
                if len(candidate) > endLen:
                    break
                if start <= int(candidate) <= end:
                    invalid.add(int(candidate))
                repeats += 1
            test = test[:-1]
            repeats = reset

print(f"Part 2 Answer: {sum(invalid)}")