from itertools import product, repeat
from copy import copy, deepcopy
from random import shuffle

deck = list(product(range(4), range(1, 11)))
suites = {k: [0] for k in range(4)}

def decides(stack, suites):
    while stack != [] and suites[stack[-1][0]][-1] + 1 == stack[-1][1]:
        # print("decision")
        card = stack.pop()
        suites[card[0]].append(card[1])

def turn(deck, suites):
    stack = []
    while deck:
        # print("turno")
        card = deck.pop()
        stack.append(card)
        if deck:
            card = deck.pop()
            stack.append(card)
        decides(stack, suites)
    stack.reverse()
    deck = deepcopy(stack) # Genera nueva variable.
    return deck

def solitaire(deck):
    shuffle(deck)
    deck = copy(deck)
    suites = {k: [0] for k in range(4)}
    while True:
        # print("continua")
        suites_copy = deepcopy(suites)
        deck = turn(deck, suites)
        if suites == suites_copy:
            break
    return suites
    
def check(deck):
    solved = {k: list(range(0, 11)) for k in range(4)}
    result = solitaire(deck)
    if solved == result:
        return True
    else:
        return False

def prob(deck, ntimes):
    samples = list(repeat(deck, ntimes))
    result = list(map(check, samples))
    print(len(list(filter(lambda x: x, result)))/ntimes)
            
prob(deck, 100)
