CONSTRAINTS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def not_valid(draws):
    for draw in draws:
        draw_params = draw.split(' ')
        if (CONSTRAINTS[draw_params[1]] < int(draw_params[0])):
            return True
    return False

def part_1():
    total_ids = 0
    f = open("input", "r")
    for i, line in enumerate(f.readlines()):
        sets = line.rstrip('\n').replace('Game ' + str(i + 1) + ': ', '').split('; ')
        all_valids = True
        for game_set in sets:
            if not_valid(game_set.split(', ')):
                all_valids = False
                break  

        if all_valids:
            total_ids += i + 1
    return total_ids   

def part_2():
    power = 0
    f = open("input", "r")
    for i, line in enumerate(f.readlines()):
        mins = { 'red': 0, 'green': 0, 'blue': 0 }
        sets = line.rstrip('\n').replace('Game ' + str(i + 1) + ': ', '').split('; ')
        for game_set in sets:
            draws = game_set.split(', ')
            for draw in draws:
                number, color = draw.split(' ')
                if (mins[color] < int(number)):
                    mins[color] = int(number)

        round_power = mins['red'] * mins['blue'] * mins['green']
        power += round_power
    return power   



print('Part 1', part_1())
print('Part 2', part_2())
