import json
import random

with open('response.json') as f:
    data = json.load(f)

# Append the first card to the deck
# Index the playerClass
# The following cards will follow the index
flag = True
deck = []
while flag:
    card = random.choice(data)
    if not deck:
        deck.append(card)
        playerClass = card['playerClass']
        continue
        print(card)
    elif len(deck) < 30:
        if card['playerClass'] == playerClass or card['playerClass'] == 'Neutral':
            deck.append(card)
    else:
        flag = False

for card in deck:
    print(card['playerClass'])

print(len(deck))
# Append the first card to the deck
# Index the playerClass
# The following cards will follow the index
        
        
    
        