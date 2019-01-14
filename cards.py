import json
import random

with open('response.json') as f:
    data = json.load(f)
    print("There are " + str(len(data)) + " cards in the collection.")

# Remove faulty cards where the key playerClass does not exist.
faulty_cards = []
for card in data:
    if 'playerClass' not in card:
        faulty_cards.append(card)
        index = data.index(card)
        del data[index]
print("The conditional found " + str(len(faulty_cards)) + " faulty cards.")
print("There are now " + str(len(data)) + " cards in the collection.")

# 1) Append the first card to the deck
# 2) Set the playerClass to variable
# 3) The following cards will filter according to that variable
deck = []
while len(deck) < 30:
    card = random.choice(data)
    if not deck:
        deck.append(card)
        playerClass = card['playerClass']
        continue
        print(card)
    elif card['playerClass'] == playerClass or card['playerClass'] == 'Neutral':
        deck.append(card)

for card in deck:
    print(card['playerClass'])

print(len(deck))



        
        
    
        