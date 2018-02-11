# -----------------
# User Instructions
# 
# This problem deals with the one-player game foxes_and_hens. This 
# game is played with a deck of cards in which each card is labelled
# as a hen 'H', or a fox 'F'. 
# 
# A player will flip over a random card. If that card is a hen, it is
# added to the yard. If it is a fox, all of the hens currently in the
# yard are removed.
#
# Before drawing a card, the player has the choice of two actions, 
# 'gather' or 'wait'. If the player gathers, she collects all the hens
# in the yard and adds them to her score. The drawn card is discarded.
# If the player waits, she sees the next card. 
#
# Your job is to define two functions. The first is do(action, state), 
# where action is either 'gather' or 'wait' and state is a tuple of 
# (score, yard, cards). This function should return a new state with 
# one less card and the yard and score properly updated.
#
# The second function you define, strategy(state), should return an 
# action based on the state. This strategy should average at least 
# 1.5 more points than the take5 strategy.

from __future__ import division
import random


def foxes_and_hens(strategy, foxes=7, hens=45):
    """Play the game of foxes and hens."""
    # A state is a tuple of (score-so-far, number-of-hens-in-yard, deck-of-cards)
    state = (score, yard, cards) = (0, 0, 'F'*foxes + 'H'*hens)
    while cards:
        action = strategy(state)
        state = (score, yard, cards) = do(action, state)
    return score + yard

def do(action, state):
    "Apply action to state, returning a new state."
    # Make sure you always use up one card.
    #
    # your code here
    score, yard, cards = state
    draw = cards[random.randint(0,len(cards)-1)]
    cards = cards[1:] if draw == 'F' else cards[:-1]
    if action == 'wait':
        return (score, 0, cards) if draw == 'F' else (score, yard+1, cards)
    elif action == 'gather':
        return (score+yard, 0, cards)
    else:
        raise ValueError
    
def take5(state):
    "A strategy that waits until there are 5 hens in yard, then gathers."
    (score, yard, cards) = state
    if yard < 5:
        return 'wait'
    else:
        return 'gather'

def average_score(strategy, N=1000):
    return sum(foxes_and_hens(strategy) for _ in range(N)) / float(N)

def superior(A, B=take5):
    "Does strategy A have a higher average score than B, by more than 1.5 point?"
    return average_score(A) - average_score(B) > 1.5

def strategy(state):
    (score, yard, cards) = state
    # your code here
    F = cards.count('F')
    H = cards.count('H')
    if F == 0:
        return 'wait'
    if H == 0:
        return 'gather'
    if ((yard + 1) * (H**2-H) / float((H**2+2*H*F+F**2-H-F))) > yard: 
    #if (yard+1) * P(hen this turn) * P(hen next turn | hen this turn) > yard
        return 'wait'
    return 'gather'

def strategy2(state):
    (score, yard, cards) = state
    # your code here
    F = cards.count('F')
    H = cards.count('H')
    if F== 0:
        return 'wait'
    if H == 0:
        return 'gather'
    if yard <= H/(F*2):
        return 'wait'
    return 'gather'
    
def test():
    gather = do('gather', (4, 5, 'F'*4 + 'H'*10))
    assert (gather == (9, 0, 'F'*3 + 'H'*10) or 
            gather == (9, 0, 'F'*4 + 'H'*9))
    
    wait = do('wait', (10, 3, 'FFHH'))
    assert (wait == (10, 4, 'FFH') or
            wait == (10, 0, 'FHH'))
    
    assert superior(strategy)
    return 'tests pass'

print average_score(strategy) 


