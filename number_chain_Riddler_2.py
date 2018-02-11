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
    
    
def find_all(chain, last, options, master):
    @memo
    def find_next(chain, last, options):
            logging.debug('Last: %d  X: %d  Modulos %d , %d' % (last, x, last % x, x % max(last,1)))
            logging.debug('Chain: %s Last: %d Options: %s Master: %s' % (str(chain),x,str(options),str(master)))
            return find_next(chain + [x], x, removed(options,x))
    return check(chain)
    
    def check(chain):
        return max((chain,master) key = len)
        
    for x in options:
        if last % x == 0 or x % max(last,1) == 0:
    return master
    
if __name__ == "__main__":
    top = int(raw_input('Input top of range for number chain (inclusive) /n note that runtime could be brutal for n > 10:'))
    print find_next([],0,range(1,top+1),[])
    logging.info('end record' + '\n')