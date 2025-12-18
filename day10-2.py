from z3 import *

with open("input/day10.txt", "r") as puzzleInput:
    data = [[l for l in lines.strip().split(' ')] for lines in puzzleInput]

joltages = [[j for j in d[-1].strip('{}').split(',')] for d in data]
buttons = [[b.strip('()').split(',') for b in d[1:-1]] for d in data]

def press_buttons(i, joltage):
    buttons_that_press_jolt = [[] for _ in range(len(joltage))]
    for b, button in enumerate(buttons[i]):
        for l in range(len(joltage)):
            if str(l) in button:
                buttons_that_press_jolt[l].append(b)

    s = Optimize()
    vars = list(Ints([f"v{b}" for b in range(len(buttons[i]))]))
    s.minimize(sum(vars))            
    s.add(var >= 0 for var in vars)
    for j, jolt in enumerate(joltage):
        s.add(sum(vars[b] for b in buttons_that_press_jolt[j]) == jolt)
    if s.check() == sat:
        model = s.model()
        return sum(model[vars[i]].as_long() for i in range(len(vars)))

print(f"Part 2: {sum(press_buttons(i, joltage) for i, joltage in enumerate(joltages))}")