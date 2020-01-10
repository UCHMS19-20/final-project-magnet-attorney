import random

card_types = {
    'ace': 1,
    'two': 2,
    'three': 3,
    'jack': 10, 
    'queen': 10,
    'king': 10
}

class Card:

    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f"<{self.name}, {self.value}>"

deck = []
# Create a deck
for key, value in card_types.items():
    for reps in range(4):
        deck.append(Card(key, value))

print(deck)

player_hand = []
dealer_hand = []

def draw_card(hand):
    index = random.randrange(0, len(deck))
    hand.append(deck.pop(index))