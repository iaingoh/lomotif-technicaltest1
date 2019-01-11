import requests
import json
import random

headers = {
        'X-Mashape-Key': 'ZTMJtzbYvXmshPTFEZI4ztIy3I68p1nPwgHjsnIGukKZeJxGcs'
        }

url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Rastakhan%27s%20Rumble'

with open('response.json') as f:
    data = json.load(f)

print(len(data))

deck = []

for i in range(30):
    deck.append(random.choice(data))

print(len(deck))

print(deck[0]['playerClass'])
