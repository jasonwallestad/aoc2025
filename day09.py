with open("input/day09.txt", "r") as puzzleInput:
    reds = [tuple(map(int, line.strip().split(','))) for line in puzzleInput]

x_index, y_index, fill, compressed_reds, dirs, a1, a2, first_inner = set(), set(), set(), [], [(-1, 0), (0, -1), (1, 0), (0, 1)], 0, 0, float('inf')

def compress_index(index):
    sorted(list(index))
    compressed_index = []
    for i in range(min(index), max(index) + 1):
        if i in index:
            compressed_index.extend([str(i), ''])
    return {v: k for k, v in enumerate(compressed_index)}

def check_edges(x1, y1, x2, y2):
    for x in range(min(x1,x2), max(x1,x2)):
        if (x, y1) not in fill or (x, y2) not in fill:
            return False
    for y in range(min(y1,y2), max(y1,y2)):
        if (x1, y) not in fill or (x2, y) not in fill:
            return False
    return True

# build indexes of reds
reversed_x_index = compress_index({x for x, _ in reds})
reversed_y_index = compress_index({y for _, y in reds})

# connect the reds
for i, red in enumerate(reds):
    next_red = i + 1 if i < len(reds) - 1 else 0
    x1, y1 = reversed_x_index[str(red[0])], reversed_y_index[str(red[1])]
    x2, y2 = reversed_x_index[str(reds[next_red][0])], reversed_y_index[str(reds[next_red][1])] 
    compressed_reds.append((x1, y1))
    for y in (range(min(y1,y2), max(y1,y2))):
        fill.add((x1, y))
    for x in (range(min(x1,x2), max(x1,x2))):
        fill.add((x, y1))
    if y1 == 0:
        first_inner = min(first_inner, x1)

# fill the shape
unfilled = [(first_inner + 1, 1)]    
while unfilled:
    x, y = unfilled.pop()
    for dx, dy in dirs:
        coord = (x + dx, y + dy)
        if coord not in fill:
            fill.add(coord)
            unfilled.append(coord)        

# build rectangles
for i, (x1, y1) in enumerate(compressed_reds):
    for j in range(i+1, len(compressed_reds)):
        area = ((abs(reds[i][0] - reds[j][0])) + 1) * ((abs(reds[i][1] - reds[j][1])) + 1)
        a1 = max(a1, area)
        if area < a2:
            continue
        x2, y2 = compressed_reds[j]
        if not {(x1, y1), (x1, y2), (x2, y1), (x2, y2)} <= fill:
            continue
        if not check_edges(x1, y1, x2, y2):
            continue
        a2 = max(a2, area)
             
print(f"Part 1: {a1}")
print(f"Part 2: {a2}")