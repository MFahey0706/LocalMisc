# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C', '<-CC'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    # your code here
    if C1 > M1 > 0 or C2 > M2 > 0 or B1 + B2 != 1:
        return {}
    else:
        if B1 == 1:
            return dict(((M1-T[0],C1-T[1],0,M2+T[0],C2+T[1],1),'M'*T[0]+'C'*T[1]+'->') for T in 
            set([(mi,ca) for mi in range(M1+1) for ca in range(C1+1) if (mi + ca < 3 and mi + ca > 0)]))
        else:
            return dict(((M1+T[0],C1+T[1],1,M2-T[0],C2-T[1],0),'<-'+'M'*T[0]+'C'*T[1]) for T in 
            set([(mi,ca) for mi in range(M2+1) for ca in range(C2+1) if (mi + ca < 3 and mi + ca > 0)]))
    # note: could have fed dict() a list of two-ples and it will turn them into key:value pairs
    # this way, you can work on lists of two-ples and then convert to a dict at the end, if that's easier

def moves(M,C, boat_capacity = 2):
    return set([(mi,ca) for mi in range(M+1) for ca in range(C+1) if (mi + ca <= boat_capacity and mi + ca > 0)])


def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
                                               (2, 1, 1, 3, 3, 0): '<-M', 
                                               (3, 1, 1, 2, 3, 0): '<-MM', 
                                               (1, 3, 1, 4, 1, 0): '<-CC', 
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print csuccessors((2, 2, 1, 0, 0, 0))
print test()