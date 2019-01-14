import random

cards = [(s, v) for s in ['H', 'S', 'C', 'D'] 
         for v in [str(i) for i in range(2, 11)] + list("JKQA")]

random.shuffle(cards)

print(len(range(2, 11)))
print(list("JKQA"))
