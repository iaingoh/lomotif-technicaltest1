import json
import random

with open('response.json') as f:
    rastakhan = json.load(f)

for i in range(30):
    if i == 0:
        deck = []
        deck.append(random.choice(rastakhan))
        print(deck[i]['playerClass'] + " for i=" + str(i))
    elif i == 1:
        next_card = random.choice(rastakhan)
        if next_card['playerClass'] == 'Neutral':
            deck.append(next_card)
            print("Neutral for i=" + str(i))
        elif next_card['playerClass'] == deck[0]['playerClass']:
            deck.append(next_card)
            print(next_card['playerClass'] + " for i=" + str(i))

print("The deck's length is " + str(len(deck)))