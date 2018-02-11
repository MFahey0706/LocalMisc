# Enter your code here. Read input from STDIN. Print output to STDOUT
#Max tree size is ~4n:
#In order to ensure that for each parent node k and child nodes are at 2k and 2k+1,
#we need a tree with a number of nodes at lowest level of tree of the power of 2 above n
#which is at most 2(n-1) = L
#Upper roots of the tree will contain, at most L-1 nodes (L/2+L/4+...+1)
#Desired tree size is thus 2L-1 = 4n-5 

from __future__ import division

###Setup

N,Q = map(int,raw_input().strip().split(' '))
T = [0]*(4*N-4) 
 
###Necessary functions

def query(T, nodej, nodek, node, addj, addk, add, parentk = 0):
    
    #Node more than target range; end
    if nodej > addk:
        return T
        
    #Node less than target range; move right
    if nodek < addj: 
        return move_right(T, nodek, parentk, node, addj, addk, add)
        
    #Node entirely within range; update node value (add) and move right
    #Do now to avoid drilling down from a terminal node
    elif nodej >= addj and nodek <= addk:
        T[node]+=add
        #moveright if possible
        return move_right(T, nodek, parentk, node, addj, addk, add)
        
    #End of range (or entire range) is within node; drill down, and abandon this tree level
    elif nodej <= addk <= nodek:
        #drill and abandon level
        return drill_down(T, nodej, nodek, node, addj, addk, add) 
        
    #Beginning of (but not entire) range is  within node; drill down and move right
    elif nodej <= addj <= nodek:
        #drill and moveright if possible
        return move_right(drill_down(T, nodej, nodek, node, addj, addk, add), 
                            nodek, parentk, node, addj, addk, add)
    
def drill_down(T, nodej, nodek, node, addj, addk, add): 
    #Return the index and j,k range of the next node down
    return query(T, nodej, (nodej + nodek -1)//2, 2*node, addj, addk, add, nodek)
    
def move_right(T, nodek, parentk, node, addj, addk, add): 
    #If in a left branch (even node #) and not yet at end of target range, we should check the right branch
    if node%2 == 0 and nodek < addk: 
        return query(T, nodek+1, parentk, node+1, addj, addk, add)
    #Elif we're already on the right node of our branch and and need to move right more, 
    #it's already being handled in a parent, so end this subquery
    return T[:node//2] + [T[node//2] + max(T[node],T[node-1])] + T[node//2+1:]

### Run

for queries in range(Q):
    j,k,add = map(int,raw_input().strip().split(' '))
    T = query(T, 1, N, 1, j, k, add)

print T[1]