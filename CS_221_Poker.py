# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
#                  counts = [ranks.count(r) for r in ranks]
#                  if counts.count(n) == n:
#                      return ranks[counts.index(n)]
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
#                  if [ranks.count(r) for r in ranks].count(2) == 4:
#                      return (ranks[1], ranks[3])
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.
import random

suits = ['C','D','H','S']
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
cards = [s + r for s in values for r in suits]
    
def deal(numhands, n=5, deck=mydeck):
    deck = [deck[i] for i in random.sample(range(0,52),52)] #shuffle
    if numhands * n <= 52 & numhands >0 & n > 0:
        return [deck[h*n:h*n+n] for h in range(0,numhands)]
    return None

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks) 
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), kind(1, ranks))
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fl = "2D 3D 4D TD JD".split() # Flush
    st = "4D 5C 6H 7S 8D".split() # Straight
    tk = "9D 9H 9C QH 3C".split() # Three of a Kind
    tp = "TH TC 3S 3D 8C".split() # Two Pair
    pa = "JH JD KH 5H 7S".split() # Pair
    hc = "4H 6H 3H QD TC".split() # High Card
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert hand_rank(fl) == (5, (11, 10, 4, 3, 2))
    assert hand_rank(st) == (4, 8)
    assert hand_rank(tk) == (3, 9, (12, 9, 9, 9, 3))
    assert hand_rank(tp) == (2, (10, 3), (10, 10, 8, 3, 3))
    assert hand_rank(pa) == (1, 11, (13, 11, 11, 7, 5))
    assert hand_rank(hc) == (0, (12, 10, 6, 4, 3))
    return 'tests pass'
    
suits = ['C','D','H','S']
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
cards = [s + r for s in values for r in suits]

def best_wild_hand(hand):
    #jokers
    #'?B' and '?R'
    handnoJ =  list(itertools.ifilterfalse(lambda x: x[0] == '?', hand))
    return max([h for h_list in [itertools.combinations(h_jokeropt, 5) 
        for h_jokeropt in [[s + b] + [s + r] + handnoJ 
        for s in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']  
        for b in ['C','S'] if '?B' in hand  for r in ['D','H'] if '?R' in hand]] 
        for h in h_list], key=hand_rank)
   