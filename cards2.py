import json
import random

with open('response.json') as f:
    data = json.load(f)

for card in data:
    print(card['name'])

print(len(data))