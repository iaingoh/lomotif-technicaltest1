import json
import random

with open('response.json') as f:
    data = json.load(f)

deck = []

deck.append(random.choice(data))

print(deck[0]['playerClass'])

another_card = random.choice(data)
print(another_card['playerClass'])

if another_card['playerClass'] == 'Neutral':
    deck.append(another_card)
    print(len(deck))
elif another_card['playerClass'] == deck[0]['playerClass']:
    deck.append(another_card)
    print(len(deck))
else:
    print(len(deck))
    pass