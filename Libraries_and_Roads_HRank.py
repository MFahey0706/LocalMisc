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

q = int(raw_input().strip())
for a0 in xrange(q):
    Networks = {}
    num_networks = 0
    n,m,Lcost,Rcost = map(int,raw_input().strip().split(' '))
    for a1 in xrange(m):
        city_1,city_2 = map(int,raw_input().strip().split(' '))
        try:
            Networks[city_2] = Networks[city_1]
        except KeyError:
            try:
               Networks[city_1] = Networks[city_2]
            except KeyError:
                Networks[city_1] = Networks[city_2] = num_networks
                num_networks += 1
    #add isolated cities to network count
    num_networks += (n - len(Networks))
    if Lcost < Rcost:
        print num_networks * Lcost
    else:
        print Lcost + (num_networks -1)*Rcost