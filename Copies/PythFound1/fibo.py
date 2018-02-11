def nacci(length):
    fib = [1, 1]
    i = 2
    while i < length:
        fib += [fib[-1] + fib[-2]]
        i += 1
    return fib

if __name__ == "__main__":
    n = nacci(10)
    assert n[2] == 2
    assert n[3] == 3
    assert n[4] == 5
    assert n[5] == 8
    assert n[6] == 13
