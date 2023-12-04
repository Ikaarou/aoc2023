def get_card_value(winning_numbers, numbers):
    card_value = 0
        for winning_number in winning_numbers:
            if winning_number in numbers:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2
    return card_value

def solve():
    total = 0
    f = open("input", "r")
    list_winning_numbers = {}
    list_numbers = {}
    for i, line in enumerate(f.readlines()):
        winning_numbers, numbers = map(lambda numbers: numbers.strip().split(' '), line.rstrip().replace(f'Card {i + 1}: ', '').replace(f'Card  {i + 1}: ', '').replace(f'Card   {i + 1}: ', '').split('|'))
        winning_numbers = [int(numeric_string) for numeric_string in list(filter(''.__ne__, winning_numbers))]
        numbers = [int(numeric_string) for numeric_string in list(filter(''.__ne__, numbers))]
        list_winning_numbers[i] = (winning_numbers, 1)
        list_numbers[i] = numbers

        card_value = get_card_value(winning_numbers, number)
        total += card_value

    for i in range(len(list_winning_numbers)):
        card_value = 0
        multiplier = list_winning_numbers[i][1]
        for winning_number in list_winning_numbers[i][0]:
            if winning_number in list_numbers[i]:
                card_value += 1
        for m in range(multiplier):
            for j in range(card_value):
                list_winning_numbers[i + j + 1] = (list_winning_numbers[i + j + 1][0], list_winning_numbers[i + j + 1][1] + 1)
    total_cards = 0
    for i in range(len(list_winning_numbers)):
        total_cards += list_winning_numbers[i][1]
    return total, total_cards

print('Results', solve())