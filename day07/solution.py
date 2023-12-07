from collections import Counter

def read_input(filename):
    with open(filename) as f:
        contents = f.read()
        return [
            (hands[0], int(hands[1]))
            for line in contents.split('\n')
            if line and (hands := line.split(' '))
        ]

def determine_hand(hand):
    match sorted(Counter(hand).values()):
        case [5]:
            return 0
        case [1, 4]:
            return 1
        case [2, 3]:
            return 2
        case [1, 1, 3]:
            return 3
        case [1, 2, 2]:
            return 4
        case [1, 1, 1, 2]:
            return 5
        case [1, 1, 1, 1, 1]:
            return 6

CARD_STRENGTHS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def card_index(hand):
    return [CARD_STRENGTHS.index(c) for c in hand]

def solve1(filename):
    hands = read_input(filename)
    hands.sort(key=lambda x: (determine_hand(x[0]), card_index(x[0])), reverse=True)
    return sum(h[1]*(i+1) for i, h in enumerate(hands))

# part 2

CARD_STRENGTHS_WITH_JOKER = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def card_index2(hand):
    return [CARD_STRENGTHS_WITH_JOKER.index(c) for c in hand]

def determine_hand2(hand):
    match sorted(Counter(hand).values()):
        case [5]:
            return 0
        case [1, 4]:
            return 0 if 'J' in hand else 1
        case [2, 3]:
            return 0 if 'J' in hand else 2
        case [1, 1, 3]:
            return 1 if 'J' in hand else 3
        case [1, 2, 2]:
            match Counter(hand).get('J'):
                case 2:
                    return 1
                case 1:
                    return 2
                case None:
                    return 4
        case [1, 1, 1, 2]:
            return 5 if 'J' not in hand else 3
        case [1, 1, 1, 1, 1]:
            return 6 if 'J' not in hand else 5

def solve2(filename):
    hands = read_input(filename)
    hands.sort(key=lambda x: (determine_hand2(x[0]), card_index2(x[0])), reverse=True)
    return sum(h[1]*(i+1) for i, h in enumerate(hands))
