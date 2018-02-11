def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    L = len(text)
        if L == 0: return (0,0) #single char string
    longest = None
        if text(0) == text(1): longest = (0,1) # first two chars match

    for j in range(1:L):
        i,k = j-1, j+1
        if compare(i,k,text)
            while i >= 0 and k < L and compare(i,k,text):
                i-=1 
                k+=1
            longest = (i+1,k-1)
        elif compare(j,k,text):
            i = j
            while i >= 0 and k < L and compare(i,k,text):
                i-=1 
                k+=1
            longest = (i+1,k-1)
    return longest
            
def compare(i,k,text, longest):
    try:
        return text(i) == text(k)
    except IndexError
        return False

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