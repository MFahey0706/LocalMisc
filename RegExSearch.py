def search(pattern, text):
    """Return true if pattern appears anywhere in text
	   Please fill in the match(          , text) below.
	   For example, match(your_code_here, text)"""
    if pattern.startswith('^'):
        return match(pattern[1:], text) # simplify: pattern[1:]
    else:
        return max([match(text[0:i] + pattern, text) for i in range(0, len(text))]) # fill this line
        #or: match('.*'+pattern, text)
        
def match(pattern, text):
    #Return True if pattern appears at the start of text
    
    