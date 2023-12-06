TIMES = 0
DISTANCES = 1


def is_valid(time, distance, time_pressed):
    speed = time_pressed
    return speed * (time - time_pressed) > distance 


def solve_races(races):
    total = 1

    for i in range(len(races[TIMES])):
        time, distance = int(races[TIMES][i]), int(races[DISTANCES][i])
        button_pressed_time = 0
        valid_numbers = []
        while (button_pressed_time < time):
            if is_valid(time, distance, button_pressed_time):
                valid_numbers.append(button_pressed_time)
            button_pressed_time += 1
        total *= len(valid_numbers)
    return total


def solve():
    f = open("input", "r")
    races = []
    for i, line in enumerate(f.readlines()):
        line = line.rstrip()
        races.append(line.split()[1::])
    
    big_time, big_distance = ''.join(str(x) for x in races[TIMES]), ''.join(str(x) for x in races[DISTANCES])

    return solve_races(races), solve_races([[int(big_time)], [int(big_distance)]])


print('Results', solve())