import pdb

def is_int(x):
    return x % 1 == 0

M = 100
n =2060
while n < 1000000:
    M+=1
    a,b,c=M,M,M
    while b > 0:
        c=b
        pdb.set_trace() '''sets a stop point like a java debugger'''
        while c > 0:
            if is_int(min([(a**2+(b+c)**2)**(.5),
                        (b**2+(a+c)**2)**(.5),
                       (c**2+(b+a)**2)**(.5)])):
                n+= 1
            c-=1
        b-=1
    print(n,M)
print(M)

