# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary_A(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        if args: # if not f(x); note this is being called more than needed via recursion
            if len(args)> 1: # if not f(x,y)
                return f(x, n_ary_f(args[0],*args[1:])) #recursive call, use * to expand tuple to list of args
            else:
                return f(x, args[0]) #handle f(x,y) case
        return x #handle f(x) case
    return n_ary_f

def n_ary_B(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        if args: # if not f(x), ie f(x,None), or f(x,[]), (which is what args[0:] pnce empty)
            return f(x, n_ary_f(args[0],*args[1:])) #recursive call, use * to expand tuple to list of args
        return x #handle f(x) case
    # return x if not args else f(x, n_ary_f(*args)) <<< conditional return & *args will expand into args[0], *args[1:]
    return n_ary_f

t = lambda i,j: i + j
t_seqA = n_ary_A(t)
t_seqB = n_ary_B(t)
print t(2,3)
print t_seqA(1,2,3,4,5)
print t_seqB(1,2,3)

