def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = str.lower(text)
    L = len(text)
    longest = (0,0)
    temp = (0,0)
    if L == 0: return longest #single char string
    if text[0] == text[1]: longest = (0,1) # first two chars match

    for j in range(1,L):
        i,k = j-1, j+1
        if compare(i,k,text):
            temp = (expand(i,k,L,text))
        elif compare(j,k,text):
            i = j
            temp = (expand(i,k,L,text))
        longest = max([longest,temp], key = lambda tupl: tupl[1] - tupl[0])
    return longest
            
def compare(i,k,text):
    try:
        return text[i] == text[k]
    except IndexError:
        return False

def expand(i,k,L,text):
    while i >= 0 and k < L and compare(i,k,text):
        i-=1 
        k+=1
    return i+1, k
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
