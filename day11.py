with open("input/day11.txt", "r") as puzzleInput:
    map = {str(val[0]):val[1].strip().split(' ') for val in [line.strip().split(':') for line in puzzleInput]}

def find_paths(pos, fft, dac, memo):
    if pos == 'out':
        return 1 if fft and dac else 0
    if (pos, fft, dac) in memo:
        return memo[(pos, fft, dac)]
    fft = True if pos == 'fft' else fft
    dac = True if pos == 'dac' else dac
    memo[(pos, fft, dac)] = sum(find_paths(step, fft, dac, memo) for step in map[pos])
    return memo[(pos, fft, dac)]

print(f"Part one: {find_paths('you', True, True, {})}")
print(f"Part two: {find_paths('svr', False, False, {})}")