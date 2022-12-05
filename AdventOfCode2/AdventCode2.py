
def input_reader():
    f = open('Input2.txt', 'r')
    lines = f.readlines()
    hands = []
    current = []
    for string in lines:
        for s in string:
            if s != ' ' and s != '\n':
                current.append(s)

        hands.append(current)
        current = []
    return hands

def handCalc(hands):
    score = 0
    for hand in hands:
        guideSwap(hand)
        if hand[0] == 'A':
            if hand[1] == 'X':
                score += 4
            elif hand[1] == 'Y':
                score += 8
            elif hand[1] == 'Z':
                score += 3
        elif hand[0] == 'B':
            if hand[1] == 'X':
                score += 1
            elif hand[1] == 'Y':
                score += 5
            elif hand[1] == 'Z':
                score += 9
        elif hand[0] == 'C':
            if hand[1] == 'X':
                score += 7
            elif hand[1] == 'Y':
                score += 2
            elif hand[1] == 'Z':
                score += 6
    return score
def guideSwap(hand):
        if hand[0] == 'A':
            if hand[1] == 'X':
                hand[1] = 'Z'
            elif hand[1] == 'Y':
                hand[1] = 'X'
            elif hand[1] == 'Z':
                hand[1] = 'Y'
        elif hand[0] == 'B':
            if hand[1] == 'X':
                hand[1] = 'X'
            elif hand[1] == 'Y':
                hand[1] = 'Y'
            elif hand[1] == 'Z':
                hand[1] = 'Z'
        elif hand[0] == 'C':
            if hand[1] == 'X':
                hand[1] = 'Y'
            elif hand[1] == 'Y':
                hand[1] = 'Z'
            elif hand[1] == 'Z':
                hand[1] = 'X'

input = input_reader()
score = handCalc(input)
print(score)
