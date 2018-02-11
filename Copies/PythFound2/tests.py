#Edit this file to complete the exercises in
#'Ensuring Reliable Code with Tests'

# You'll need to write a function, `is_prime(n)` which passes
# the following suite of tests. Note that the input values are
# outside the usual domain of numbers greater than zero.
# Indeed, your function will have to handle values that aren't even numbers.
def is_int(x):
    try:
        d = x%1
    except TypeError:
        return False
    if x%1 == 0:
        return True
    else:
        return False
    
def is_prime(x):
    if type(x) == str:
        return False
    if is_int(x):
        x=int(x)
        if x < 0:
            x = -x
        if x > 1:
            for i in range(2,x):
                if(is_int(x/float(i))):
                    #print("Found factor")
                    return False
            return True
    #print("Not positive int")
    return False
    
def test_is_prime_11():
    assert is_prime(11) == True
def test_is_prime_12():
    assert is_prime(12) == False
def test_is_prime_13():
    assert is_prime(13) == True
def test_is_prime_7919():
    assert is_prime(7919) == True
def test_is_prime_6025():
    assert is_prime(6025) == False
def test_is_prime_neg17():
    assert is_prime(-17) == True #negatives are typically not consider prime but test_tests.py wants this answer
def test_is_prime_neg18():
    assert is_prime(-18) == False
def test_is_prime_string():
    assert is_prime('primeapple') == False
def test_is_prime_0():
    assert is_prime(0) == False
def test_is_prime_1():
    assert is_prime(1) == False
def test_is_prime_2():
    assert is_prime(2) == True
def test_is_prime_3():
    assert is_prime(3) == True
def test_is_prime_bool():
    assert is_prime(True) == False
    
# You'll need to write a function, `multiples(f, b, limnit)` which passes
# the following suite of tests.
# Note that the output might be an iterator or might be a collection.
# The test cases don't care.

def multiples(f,b,lim):
    if is_int(f) and is_int(b) and is_int(lim):
        f=float(f)
        b=float(b)
        lim=float(lim)
        if f < 0:
            f = -f
        if b < 0:
            b = -b
        if lim < 0:
            print("Invalid negative limit")
            return None
        lim -= 1 #only want integer multiples strictly less than lim
        flim = int(lim/f-(lim%f)/f)#find the greatest multiples of f and b < lim
        blim = int(lim/b-(lim%b)/b)
        print(blim)
        print(range(1,blim+1))
        m=set()
        for fi in range(1,flim+1):
            m.update([int(f*fi)])
        for bi in range(1,blim+1):
            m.update([int(b*bi)])
        return m
    else:
        print "Noninteger values passed"
        return None

def test_GIVEN_multiples_WHEN_sum_THEN_result():
    assert sum(multiples(3, 5, 10)) == 23
def test_GIVEN_multiples_WHEN_set_THEN_result():
    assert set(multiples(3, 5, 10)) == set([3, 5, 6, 9])
    
if __name__ == "__main__":
    pass
