def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    result = ''
    i = 0
    for n in word:
        if n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i == 0:
                i += 1
                result = ''.join(['((' for p in range(len(word))]) + result
            else:
                result += '+'
            result += n + ')*10)'
        else:
            result += n
    
    return result

print compile_word('ABC')