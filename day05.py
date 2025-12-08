fresh_ranges, ingredients = [], []
highest, a1, a2 = 0, 0, 0

with open("input/day05.txt", "r") as puzzleInput:
    for line in puzzleInput:
        line = line.strip()
        if "-" in line:
            fresh_ranges.append(list(map(int, line.split('-'))))
        elif line:
            ingredients.append(int(line))   
            
for ingredient in ingredients:
    for start, end in fresh_ranges:
        if start <= ingredient <= end:
            a1 += 1
            break

fresh_ranges.sort()
for start, end in fresh_ranges:
    if start > highest:
        a2 += end - start + 1
    elif end > highest:
        a2 += end - highest
    highest = max(highest,end)

print(f"Part 1: {a1}")
print(f"Part 2: {a2}")