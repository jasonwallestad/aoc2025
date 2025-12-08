import math

with open("input/day08.txt", "r") as puzzleInput:
    boxes = [[int(n) for n in line.strip().split(",")] for line in puzzleInput.readlines()]

distances, circuits, merged_index, p1_limit = [], [], set(), 1000

for b1, box1 in enumerate(boxes):
    for b2 in range(b1 + 1, len(boxes)):
        distances.append((b1, b2, math.dist(box1, boxes[b2])))

distances.sort(key=lambda x: x[2])
for i in range(len(distances)):
    b1, b2, distance = distances[i]
    connection = {b1, b2}
    for c, circuit in enumerate(circuits):
        if connection & circuit:
            circuits[c].update(connection)
            if i <= p1_limit - 1 and connection <= merged_index:
                for cc, circuit_check in enumerate(circuits):
                    if c != cc and connection & circuit_check:
                        circuits[c].update(circuits.pop(cc))
                        break
            break
    else:
        circuits.append(connection)
    merged_index.update(connection)
    
    if i == p1_limit - 1:
        circuits.sort(key=len, reverse=True)
        print(f"Part 1: {math.prod([len(n) for n in circuits[:3]])}")

    if len(merged_index) == len(boxes):
        print(f"Part 2: {boxes[b1][0] * boxes[b2][0]}")
        break