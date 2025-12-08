with open("input/day03.txt", "r") as puzzleInput:
    banks = [lines.strip() for lines in puzzleInput]

def find_joltage(needed_bats):
    joltage = 0
    for bank in banks:
        need_to_remove = len(bank) - needed_bats
        while need_to_remove > 0:
            for i in range(len(bank) - 1):
                if bank[i] < bank[i+1]:
                    bank = bank[:i] + bank[i+1:]
                    break
            need_to_remove -= 1
        joltage += int(bank[:needed_bats])
    return joltage

print(f"Part 1 Answer: {find_joltage(2)}")
print(f"Part 2 Answer: {find_joltage(12)}")