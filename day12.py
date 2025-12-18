import re
with open("input/day12.txt", "r") as i: 
    print(f"Day 12: {sum([(p[0] * p[1]) > (sum(p[2:-1]) * 9) for p in [[int(n) for n in re.findall(r"\d+", l)] for l in i if len(l) > 5]])}")