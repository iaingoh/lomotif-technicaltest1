import time
from random import randint

Suits = [
    ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King"], #hearts
    ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King"], #clubs
    ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King"], #spades
    ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King"]  #diamonds
    ]


for x in range(0,52):
    #selection of random card and suit
    Suit = randint(0,3) 
    Card = randint(0,12)

    # prints what card was received from the deck
    if Suit == 0:
        print("You got a", Suits[0][Card], "of Hearts")
    elif Suit == 1:
        print("You got a", Suits[1][Card], "of Clubs")
    elif Suit == 2:
        print("You got a", Suits[2][Card], "of Spades")
    else:
        print("You got a", Suits[3][Card], "of Diamonds")