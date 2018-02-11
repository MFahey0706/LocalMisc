import logging
logging.basicConfig(filename='number_chain_Riddler.log',level=logging.DEBUG)

def removed(L,x):
    return [i for i in L if i != x]

def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args refuses to be a dict key
            return f(*args)
    _f.cache = cache
    return _f

def wrap(chain, last, options, master):
    cache={}
    def find_next(chain, last, options, master, forward = 1):
        try:
            return cache[(tuple(set(chain)),last,chain[0])]
        except KeyError:
            for x in options:
                if len(chain) > len(master):
                        master = chain
                if forward and (last % x == 0 or x % max(last,1) == 0):
                    ##logging.debug('Last: %d  X: %d  Modulos %d , %d' % (last, x, last % x, x % max(last,1)))
                    ##logging.debug('Chain: %s Last: %d Options: %s Master: %s' % (str(chain),x,str(options),str(master))) 
                    cache[(tuple(set(chain + [x])), x, chain[0])] = master = max((find_next(chain + [x], x, removed(options,x),master),master), key=len)
                elif chain[0] % x == 0 or x % chain[0] == 0:
                    ##logging.debug('Last: %d  X: %d  Modulos %d , %d' % (last, x, last % x, x % max(last,1)))
                    ##logging.debug('Chain: %s Last: %d Options: %s Master: %s' % (str(chain),x,str(options),str(master)))
                    cache[(tuple(set([x]+chain)), chain[len(chain)-1], x)] = master = max((find_next([x]+chain, x, removed(options,x),master, forward=0),master), key=len)
            return master
        return master
    return find_next(chain, last, options, master)
    
if __name__ == "__main__":
    top = int(raw_input('Input top of range for number chain (inclusive) /n note that runtime could be brutal for n > 10:'))
    answer = wrap([1],1,range(2,top+1),[1])
    print answer
    logging.info(str(answer) + ' end record' + '\n')