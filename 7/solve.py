from functools import cmp_to_key

ORDER = {"A": 13, "K": 12, "Q": 11 , "J": 10 , "T": 9 , "9": 8 , "8": 7, "7": 6 , "6": 5 , "5": 4 , "4":3 , "3": 2 , '2': 1}



POWER = {
    5: 1000000,
    4: 100000,
    3: 10000,
    2: 1000,
    1: 100
}

POWER_CARD = {
    1: 10000,
    2: 1000,
    3: 100,
    4: 10,
    5: 1,
}

def compare(hand1, hand2):
    cards1, hand1_value, _bid = hand1
    cards2, hand2_value, _bid = hand2
    print(cards1, cards2)
    if (hand1_value == hand2_value):
        for i in range(len(cards1)):
            if (ORDER[cards1[i]] == ORDER[cards2[i]]):
                continue
            else:
                return 1 if ORDER[cards1[i]] > ORDER[cards2[i]] else -1

    return 1 if hand1_value > hand2_value else -1  

def hand_to_hash(hand):
    all_freq = {}
    for i in hand:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

def transform_to_values(hands, part2 = False):
    hands_values = []
    for cards, bid in hands:
        value = 1
        cards_hash = hand_to_hash(cards)
        number_of_cards = len(cards_hash.keys())
        if (part2):
            if ('J' in cards_hash and cards_hash['J'] < 5):
                copy_card_hash = cards_hash.copy()
            
                if 'J' in copy_card_hash:
                    del copy_card_hash['J'] 
                max_count = max(copy_card_hash.values())
                for ordered in ORDER:                    
                    if ordered in cards_hash and cards_hash[ordered] == max_count and ordered is not 'J':
                        cards_hash[ordered] += cards_hash['J']
                        break
                del cards_hash['J']

        for i in cards_hash:
            value += POWER[cards_hash[i]]
        hands_values.append([cards, value, bid])

    hands_values = sorted(hands_values, key=cmp_to_key(compare))
    total_bid = 0
    for rank, hands_value in enumerate(hands_values):
        total_bid += (rank + 1) * hands_value[2] 
    return total_bid

def solve(part2 = False):
    f = open("input", "r")
    if (part2):
        ORDER['J'] = 0
    hands = []
    for i, line in enumerate(f.readlines()):
        line = line.rstrip()
        cards, bid = line.split()
        hands.append((cards, int(bid)))
    
    values = transform_to_values(hands, part2)
    return values

print('results(253910319,254083736)')
print('Results', solve(True))