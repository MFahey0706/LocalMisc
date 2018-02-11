#test Grammar

from functools import update_wrapper
from string import split
import re



def grammar(description, whitespace=r'\s*'):
    """Convert a description to a grammar.  Each line is a rule for a
    non-terminal symbol; it looks like this:
        Symbol =>  A1 A2 ... | B1 B2 ... | C1 C2 ...
    where the right-hand side is one or more alternatives, separated by
    the '|' sign.  Each alternative is a sequence of atoms, separated by
    spaces.  An atom is either a symbol on some left-hand side, or it is
    a regular expression that will be passed to re.match to match a token.
    
    Notation for *, +, or ? not allowed in a rule alternative (but ok
    within a token). Use '\' to continue long lines.  You must include spaces
    or tabs around '=>' and '|'. That's within the grammar description itself.
    The grammar that gets defined allows whitespace between tokens by default;
    specify '' as the second argument to grammar() to disallow this (or supply
    any regular expression to describe allowable whitespace between tokens)."""
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs!
    for line in split(description, '\n'):
        lhs, rhs = split(line, ' => ', 1)
        alternatives = split(rhs, ' | ')
        G[lhs] = tuple(map(split, alternatives))
    return G

TEST = grammar(r"""Var => [a-zA-Z_]\w*
Num => [-+]?[0-9]+([.][0-9]*)?
VarOrNum => Var | Num""")

#for some reason the code provided by the course puts the r""" and """
#on separate lines, but I've found that this adds a leading and trailing 
#empty string that can't be split into lhs, rhs and causes errors
#my code is less readable though so I'd love to figure out the problem

print TEST

k = split(r"""Var => [a-zA-Z_]\w*
Num => [-+]?[0-9]+([.][0-9]*)?
VarOrNum => Var | Num""", '\n')


