import numpy, math, pandas

def calc_primes(n):
# Find all primes n > prime > 2 using the Sieve of Eratosthenes 
    sieve = numpy.ones(n/2, dtype=numpy.bool)
        #boolean flags, only for odd numbers since 2 is the only even prime
    limit = int(math.sqrt(n)) + 1
        #only need to go up to sqrt(n) bc all other nonprimes will have  factor < sqrt(n)
    for i in range(3, limit, 2): #odd nums only; 
        if sieve[i/2]: #recall out list only has odds, so index of 3 is 1, index of 5 is 2...
            sieve[i*i/2 :: i] = False #flag multiples of our prime as not prime; 
                                      #begin at i**2 bc all multiples of primes < i are already flagged
    prime_indexes = numpy.nonzero(sieve)[0][1::] 
        #returns indices of nonzero elements of target in a list, as 1st elem of an array
    primes  = 2 * prime_indexes + 1
        #recall we divided n by 2 at the beginning to take out evens; so index 0 is 1, 1 is 3, etc.
    primes = numpy.append([2],primes)
    primes.tofile('primes_to_%s.csv' % (n), sep=',')
    return primes

N = int(raw_input('Generate file of primes up to what number (enter a positive integer)'))
calc_primes(N)

primelist = map(int,list(pandas.read_csv('primes_to_%s.csv' % (N), sep=',')))
print('Number of primes in file: %i' % (len(primelist)))