#Desired flow:
#Network: a group of cities connected to eachother in some way by roads
#
#Total library cost = library cost * # of networks
#Building one road from network to network reduces # of required libraries by 1
#Choice between building a road and building an extra library dictated by: Lcost and Rcost
#If Lcost < Rcost, total cost = # Networks * Lcost, else Lcost + (#networks -1)*Rcost
#
#Most of the work is in building the networks
#What's the lowest cost way of building networks?
#Use a dict: key = city, value = Network
                                
def step(node):
    global nodelist
    global Networks
    global total
    nodelist.remove(node)
    if nodelist and node in Networks: #build roads:
        for x in Networks[node]:
            if x in nodelist:
                total += Rcost
                step(x)  
        return total
    else:
        return total

q = int(raw_input().strip())
for a0 in xrange(q):
    n,m,Lcost,Rcost = map(int,raw_input().strip().split(' '))
    if Lcost < Rcost: #If libs are cheaper than road repairs, just build libs everywhere
        print n*Lcost
        for a1 in xrange(m):#burn through input
            raw_input()
    else:
        nodelist = range(1,n+1)
        Networks = {x:[] for x in nodelist}
        for a1 in xrange(m):
            city_1,city_2 = map(int,raw_input().strip().split(' '))
            Networks[city_1] += [city_2]
            
        total = 0
        while nodelist:
            total += Lcost  
            step(nodelist[0])
        print total 

