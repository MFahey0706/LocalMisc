import numpy, math, pandas

def calc_primes(n):
# Find all primes n > prime > 2 using the Sieve of Eratosthenes 
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if sieve[i/2]:
            sieve[i*i/2 :: i] = False
    prime_indexes = numpy.nonzero(sieve)[0][1::]
    primes  = 2 * prime_indexes + 1
    primes = numpy.append([2],primes)
    primes.tofile('primes.csv', sep=',')
    return primes

calc_primes(10)

primelist = map(int,list(pandas.read_csv('primes.csv', sep=',')))
print(primelist)