x=int(raw_input("limit?"))
primes = [1,2]
check = {}
for y in range(1,x+1):
    check[str(y)]=0
ci = 1
while ci < len(primes):
    c=primes[ci]
    r=c*primes[ci-1]
    while r <= x:
        r+=c
        check[str(r)]=1
    c+=1
    while (c < x) and check[str(c)]:
        c+=1
    if check[str(c)] == 0:
        primes+=[c]
    ci+=1
print(primes)
         
    
        