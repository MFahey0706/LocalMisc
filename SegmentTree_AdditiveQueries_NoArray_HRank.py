# Enter your code here. Read input from STDIN. Print output to STDOUT

###Setup

N,Q = map(int,raw_input().strip().split(' '))
T = [0]*(N+2) #leave empty nodes at beginning and end 
 
###Log queries

for queries in range(Q):
    j,k,add = map(int,raw_input().strip().split(' '))
    T[j]+=add
    T[k+1]-=add
    
###Find max

V=0
M=0

for x in T:
    V+=x
    M=max(V,M)
    
print M