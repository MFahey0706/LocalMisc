if isinstance(n, int):
    times = [timedcall(fn, *args)[0] for _ in range(n)]
else:
    times = []
    while sum(times) < n:
        times += [timedcall(fn, *args)[0]]

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    n, add, sign = 0, 0, -1
    while True:
        n += (add*sign)
        yield n
        add += 1
        sign *= sign

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    n = 0
    yield n
    while True:
        n+=1
        yield n, -n