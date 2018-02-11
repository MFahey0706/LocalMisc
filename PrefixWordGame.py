# -----------------
# User Instructions
# 
# Write a function, readwordlist, that takes a filename as input and returns
# a set of all the words and a set of all the prefixes in that file, in 
# uppercase. For testing, you can assume that you have access to a file 
# called 'words4k.txt'
import timeit, cProfile

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename='testlist.txt'):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename) # opens file
    text = file.read()    # gets file into string
    # your code here
    wordset = set(text.split())
    prefixset = [] 
    #starting with a list to make appending easier; unsure what approach is fastest
    for word in wordset:
        prefixset = prefixset + prefixes(word) 
        #could've started w/ an empty set and used .add() to add elems, but that
        # would require a second for loop to iterate over elems of prefixes() output
    prefixset = set(prefixset) #change list to set
    return wordset, prefixset

def readwordlist2(filename='testlist.txt'):
    """Read the words from a file and return a set of the words 
    and a set of the prefixes."""
    file = open(filename) # opens file
    text = file.read()    # gets file into string
    # your code here
    wordset = set(text.split())
    prefixset = set() 
    #starting with a set and append with add()
    #timer shows this is slightly faster
    for word in wordset:
        for pref in prefixes(word):
            prefixset.add(pref) 
    return wordset, prefixset
    
#WORDS, PREFIXES = readwordlist('words4k.txt')

def test():
    assert len(WORDS)    == 3892
    assert len(PREFIXES) == 6475
    assert 'UMIAQS' in WORDS
    assert 'MOVING' in WORDS
    assert 'UNDERSTANDIN' in PREFIXES
    assert 'ZOMB' in PREFIXES
    return 'tests pass'

def repeat_func(f, N=100):
    for k in range(N):
        w,p = f('testlist.txt')
    return True
    
t = timeit.Timer("""readwordlist()""", setup ="from __main__ import readwordlist")
t2 = timeit.Timer("""readwordlist2()""", setup ="from __main__ import readwordlist2")
#need to give the timer access to user defined functions
#either with an import or by updating the global namespace

print 'Using list to set'
#cProfile.run('readwordlist()')
print t.timeit(10000)

print 'Using set.add()'
#cProfile.run('readwordlist2()')
print t2.timeit(10000)