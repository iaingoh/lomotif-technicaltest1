import json
import random

with open('response.json') as f:
    data = json.load(f)

deck = []
deck.append(random.choice(data))
print(deck[0]['playerClass'])


next_card = random.choice(data)
print(next_card['playerClass'])

if next_card['playerClass'] == 'Neutral':
    deck.append(next_card)
    print(len(deck))
elif next_card['playerClass'] == deck[0]['playerClass']:
    deck.append(next_card)
    print(len(deck))


next_card = random.choice(data)
print(next_card['playerClass'])

if next_card['playerClass'] == 'Neutral':
    deck.append(next_card)
    print(len(deck))
elif next_card['playerClass'] == deck[0]['playerClass']:
    deck.append(next_card)
    print(len(deck))

print("Deck length is " + str(len(deck)))
