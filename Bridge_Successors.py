# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    # your code here 
    d = {} #initialize an empty dict    
    if 'light' in here:#find light
        fromside, toside, dir = here, there, '->'
    else:
        fromside, toside, dir = there, here, '<-'

    for p1 in fromside:
        if p1 is not 'light':
            for p2 in fromside:
                if p2 is not 'light' and p1 <= p2:
                    a = frozenset(fromside - set([p1,p2,'light'])) #can use - to remove elem or one set from another
                    b = frozenset(toside | set([p1,p2,'light'])) #can use | to union two sets
                    if dir == '->':
                        d[a,b,(t + max(p1,p2))] = (p1,p2,dir)
                    else:
                        d[b,a,(t + max(p1,p2))] = (p1,p2,dir)
                    #could have used a dict comprehension 
                    #e.g. dict(((a,b),a+b) for a in x for b in y) is a dict w/ 2ples as keys and their sum as values
                    
    return d 
           

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print bsuccessors((frozenset([]), frozenset([2, 'light']), 0))
print test()