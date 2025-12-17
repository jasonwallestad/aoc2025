with open("input/day09.txt", "r") as puzzleInput:
    reds = [tuple(map(int, line.strip().split(','))) for line in puzzleInput]

filled, compressed_reds, first_inner, a1, a2  = set(), [], float('inf'), 0, 0

def check_edges(x1, y1, x2, y2):
    for x in range(min(x1,x2), max(x1,x2)):
        if (x, y1) not in filled or (x, y2) not in filled:
            return False
    for y in range(min(y1,y2), max(y1,y2)):
        if (x1, y) not in filled or (x2, y) not in filled:
            return False
    return True

red_x_map = {red: i for i, red in enumerate(sorted(list({x for x, _ in reds})))}
red_y_map = {red: i for i, red in enumerate(sorted(list({y for _, y in reds})))}

# connect the reds
for i, red in enumerate(reds):
    next_red = i + 1 if i < len(reds) - 1 else 0
    x1, y1 = red_x_map[red[0]], red_y_map[red[1]]
    x2, y2 = red_x_map[reds[next_red][0]], red_y_map[reds[next_red][1]] 
    compressed_reds.append((x1, y1))
    for y in (range(min(y1,y2), max(y1,y2))):
        filled.add((x1, y))
    for x in (range(min(x1,x2), max(x1,x2))):
        filled.add((x, y1))
    if y1 == 0:
        first_inner = min(first_inner, x1)

# fill the shape
unfilled = [(first_inner + 1, 1)]    
while unfilled:
    x, y = unfilled.pop()
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        coord = (x + dx, y + dy)
        if coord not in filled:
            filled.add(coord)
            unfilled.append(coord)        

# build rectangles
for i, (x1, y1) in enumerate(compressed_reds):
    for j in range(i+1, len(compressed_reds)):
        area = ((abs(reds[i][0] - reds[j][0])) + 1) * ((abs(reds[i][1] - reds[j][1])) + 1)
        a1 = max(a1, area)
        if area < a2:
            continue
        x2, y2 = compressed_reds[j]
        if not {(x1, y1), (x1, y2), (x2, y1), (x2, y2)} <= filled:
            continue
        if not check_edges(x1, y1, x2, y2):
            continue
        a2 = max(a2, area)
             
print(f"Part 1: {a1}")
print(f"Part 2: {a2}")