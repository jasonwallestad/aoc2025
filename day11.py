from functools import cache

with open("input/day11.txt", "r") as puzzleInput:
    map = {str(val[0]):val[1].strip().split(' ') for val in [line.strip().split(':') for line in puzzleInput]}

@cache
def find_paths(pos, fft, dac):
    if pos == 'out':
        return 1 if fft and dac else 0
    fft = True if pos == 'fft' else fft
    dac = True if pos == 'dac' else dac
    return (sum(find_paths(step, fft, dac) for step in map[pos]))

print(f"Part one: {find_paths('you', True, True)}")
print(f"Part two: {find_paths('svr', False, False)}")