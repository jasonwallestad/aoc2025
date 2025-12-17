import itertools

with open("input/day10.txt", "r") as puzzleInput:
    data = [[l for l in lines.strip().split(' ')] for lines in puzzleInput]

joltages = [[j for j in d[-1].strip('{}').split(',')] for d in data]
indicators = [[i for i in d[0].strip('[]')] for d in data]
buttons = [[b.strip('()').split(',') for b in d[1:-1]] for d in data]
a1 = 0

def push_button(button, state):
    for b in button:
        state[int(b)] = '#' if state[int(b)] == '.' else '.'
    return state

for i, indicator in enumerate(indicators):
    combos = list(itertools.chain.from_iterable(itertools.combinations(buttons[i], c) for c in range(len(buttons[i]) + 1)))
    for combo in combos:
        state = ['.'] * len(indicator)
        for button in combo:
            state = push_button(button, state)
        if state == indicator:
            a1 += len(combo)
            break

print(f"Part 1: {a1}")