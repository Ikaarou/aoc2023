def is_part_number(engine, current_number, x, y):
    directions = [(-1, -1), (-1, 1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1),(1, -1)]
    for i in range(len(str(current_number))):
        for direction_x, direction_y in directions:
            if (x + direction_x >= len(engine) or x + direction_x < 0):
                continue
            if ((direction_y + i + y) >= len(engine[x]) or (direction_y + i + y) < 0):
                continue
            current_x, current_y = (x + direction_x, y + i + direction_y)
            if (not engine[current_x][current_y].isnumeric() and engine[current_x][current_y] != '.'):
                return True

def find_gear(engine, current_number, x, y):
    directions = [(-1, -1), (-1, 1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1),(1, -1)]
    for i in range(len(str(current_number))):
        for direction_x, direction_y in directions:
            if (x + direction_x >= len(engine) or x + direction_x < 0):
                continue
            if ((direction_y + i + y) >= len(engine[x]) or (direction_y + i + y) < 0):
                continue
            current_x, current_y = (x + direction_x, y + i + direction_y)
            if (engine[current_x][current_y] == '*'):
                return (current_x, current_y)
    return None 

    

def solve():
    engine = []
    f = open("input", "r")
    for line in f.readlines():
        chars = []
        for char in line.rstrip():
            chars.append(char)
        engine.append(chars)


    total = 0
    gears = {}
    for i in range(len(engine)):
        current_number = 0
        d = 0
        for j in range(len(engine[i])):
            if (d > 0):
                d -= 1
                continue

            if (engine[i][j].isnumeric()):
                save_j = j
                while (j < len(engine[i]) and engine[i][j].isnumeric()):
                    current_number = current_number * 10 + int(engine[i][j])
                    j += 1
                    d += 1
                if is_part_number(engine, current_number, i, save_j):
                    total += current_number
                
                gear = find_gear(engine, current_number, i, save_j)
                if gear:
                    if gear in gears:
                        gears[gear].append(current_number)                 
                    else:
                        gears[gear] = [current_number]
            current_number = 0
    total_gear = 0
    for gear in gears:
        if (len(gears[gear]) == 2):
            n1, n2 = gears[gear]
            total_gear += n1 * n2
        
    return total, total_gear

    
print('Results', part_1())