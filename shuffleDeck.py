import random
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]
deck = []

for i in range(2, 11):
    for suit in suits:
        card = str(i) + " of " + suit
        deck.append(card)

for royal in royals:
    for suit in suits:
        card = royal + " of " + suit
        deck.append(card)

random.shuffle(deck)

for card in deck:
    print(card)
