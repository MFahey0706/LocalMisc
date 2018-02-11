import string, re, itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    # Your code here
    
    #begin the great letter harvest
    letters = ''.join(set([ltr for ltr in formula if ltr in string.letters]))
    #end the great letter harvest
    
    #after the harvest festival, loop through letter:number combos
    for perm in [''.join(nums) for nums in itertools.permutations('1234567890', len(letters))]:
        digit_form = formula.translate(string.maketrans(letters, perm))
        if try_formula(digit_form):
            return digit_form
            
def try_formula(f):
    #return False if Formula f evaluates to False or contains / by 0; otherwise True
    if valid(f):
        try:
            return eval(f)
        except ZeroDivisionError:
            return False
        
# assume: def fill_in(formula):
#        "Generate all possible fillings-in of letters in formula with digits."
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def test():
    print solve('AB + BC == CD')

test()