from itertools import product, repeat
import numpy as np
from random import shuffle

deck = list(product(range(4), range(10)))  # suites 0,1,2,3 numbers 0,1,...,9
print(len(deck))

def solitaire(deck):
    """Shuffles the deck of cards and tests if it solves the solitaire game"""
    solved = np.array(list(product(range(4), range(9))))
    solved.resize((4, 9, 2))
    shuffle(deck)
    spread = np.array(deck[:-4])
    spread.resize((4, 9, 2))
    rest = deck[-4:]
    while rest:
        card = rest.pop()
        while card[1] != 9:
            next = spread[card[0], card[1]].copy()
            spread[card[0], card[1]] = card
            card = next
    if (spread == solved).all():
        return True
    else:
        return False
        
def shuffle_deck_generator(deck, ntimes):
    """Generates ntimes shuffled decks."""
    n = 0
    while n < ntimes:
        shuffle(deck)
        yield deck
        n += 1
    
def probability_solved(deck, num_epoch):
    """Estimates the probability of shuffling a deck of cards which solves the solitaire by
       repeating the simulation num_epoch times and calculating the mean."""
    result = list(map(solitaire, list(shuffle_deck_generator(deck, num_epoch))))
    num_true = len(list(filter(lambda x: x, result)))
    print(num_true / num_epoch)
    
    
probability_solved(deck, 10000)  # About 2.5
