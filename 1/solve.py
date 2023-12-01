NUMBERS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def find_first_int(string, reversed, with_words=False):
    smallest_index = -1
    value = 0
    if with_words:
        for numberWord in NUMBERS:
            index = string.find(numberWord[::-1] if reversed else numberWord)
            if (index != -1 and (smallest_index > index or smallest_index == -1)):
                smallest_index = index
                value = NUMBERS[numberWord]
            

    for i in range(len(string)):
        if string[i].isnumeric():
            if i < smallest_index or smallest_index == -1:
                return int(string[i])
    return value


def solve(with_words):
    total = 0
    f = open("input", "r")
    for line in f.readlines():
        first_value = find_first_int(line, False, with_words)
        last_value = find_first_int(line[::-1], True, with_words)
        total += first_value * 10 + last_value
    return total

print('Part 1', solve(False))

print('Part 2', solve(True))
