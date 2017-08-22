f = open('p054_poker.txt', 'r')
hands = f.readlines()
f.close()
for i in range(len(hands)):
    hands[i] = (hands[i][:14].split(' '),hands[i][15:29].split(' '))

cardValues = {}
cards = "23456789TJQKA"
for i in range(len(cards)-5):
    cardValues[cards[i]] = i+2

v = 10
for c in cards[-5:]:
    cardValues[c] = v
    v += 1

def evaluateHand(hand):
    cards = []
    colors = []
    for card in hand:
        cards += [cardValues[card[0]]]
        colors += [card[1]]
    for c in cards:
        count = cards.count(c)
        rem = set(cards) - set([c])
        if (count == 4):
            return (7, [c], sorted(list(rem), reverse=True))
        elif (count == 3):
            if (len(rem) == 2):
                return (3, [c], sorted(list(rem), reverse=True))
            else:
                return (6, [c, rem.pop()], sorted(list(rem), reverse=True))
        elif (count == 2):
            if (len(rem) == 3):
                return (1, [c], sorted(list(rem), reverse=True))
            elif (len(rem) == 2):
                pairs = [c]
                for elem in rem:
                    if (cards.count(elem) == 2):
                        pairs += [elem]
                return (2, sorted(pairs, reverse=True), sorted(list(rem), reverse=True))
    else:
        if (all([min(cards)+i in cards for i in range(5)])):
            if (len(set(colors)) == 1 and min(cards) == 10):
                return (9, [], sorted(list(rem), reverse=True))
            elif (len(set(colors)) == 1):
                return (8, [max(cards)], sorted(list(rem), reverse=True))
            else:
                return (4, [max(cards)], sorted(list(rem), reverse=True))
        elif(len(set(colors)) == 1):
            return (5, sorted(cards, reverse=True), sorted(list(rem), reverse=True))
        else:
            return (0, sorted(cards, reverse=True), sorted(list(rem), reverse=True))                
            

def getWinner(hand):
    playerOne = hand[0]
    playerTwo = hand[1]
    
    valPlayerOne = evaluateHand(playerOne)
    valPlayerTwo = evaluateHand(playerTwo)

    if (valPlayerOne[0] > valPlayerTwo[0]):
        return 1
    elif (valPlayerOne[0] == valPlayerTwo[0]):
        i = 0
        while (i < len(valPlayerOne[1]) and valPlayerOne[1][i] == valPlayerTwo[1][i]):
            i += 1
        if (i < len(valPlayerTwo[1]) and valPlayerOne[1][i] > valPlayerTwo[1][i]):
            return 1
        elif (i >= len(valPlayerTwo[1])):
            i = 0
            while (i < len(valPlayerOne[2]) and valPlayerOne[2][i] == valPlayerTwo[2][i]):
                i += 1
            if (i < len(valPlayerTwo[2]) and valPlayerOne[2][i] > valPlayerTwo[2][i]):
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0
   





playerOneWins = 0

for hand in hands:
    playerOneWins += getWinner(hand)
