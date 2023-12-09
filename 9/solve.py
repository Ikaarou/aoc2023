
def full_zero(numbers):
    numbers_set = set(numbers)
    return len(numbers_set) == 1 and 0 in numbers_set


def predict_next_value(numbers):
    numbers_copy = numbers.copy()
    steps = []
    
    while (not full_zero(numbers_copy)):
        i = 0
        next_array = []
        while i < len(numbers_copy) - 1:
            next_array.append(numbers_copy[i + 1] - numbers_copy[i])
            i += 1
        steps.append(next_array)
        numbers_copy = next_array
    
    steps.reverse()
    steps.pop(0)
    n = len(steps) - 1
    for i, step in enumerate(steps):
        if (i == 0):
            step.append(step[0])
        else:
            step.append(step[-1] + steps[i - 1][-1])
            step.insert(0, step[0] - steps[i - 1][0])
    return numbers[-1] + steps[-1][-1], numbers[0] - steps[-1][0]


def solve():
    f = open("input_test", "r")
    numbers_list = []
    for i, line in enumerate(f.readlines()):
        line = line.rstrip()
        numbers_list.append(list(map(lambda n: int(n), line.split())))

    total_first = 0
    total_last = 0
    for numbers in numbers_list:
        last, first =  predict_next_value(numbers)
        total_first += first
        total_last += last
    return total_last, total_first

print('Results', solve())