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
#Use a dict: key = city, value = Network?
#List of sets?

def find_in_sublist(list,elem):
    x=0
    while elem not in list[x]:
        x+=1
    return x
    
q = int(raw_input().strip())
for a0 in xrange(q):
    n,m,Lcost,Rcost = map(int,raw_input().strip().split(' '))
    if Lcost < Rcost: #If libs are cheaper than road repairs, just build libs everywhere
        print n*Lcost
        for a1 in xrange(m):#burn through input
            raw_input()
    else: #Roads are cheaper than libs; evaluate the road networks
        Networks = [] #list of sets of cities that can be connected by roads
        log = [] #list of cities that we've added to a network
        for a1 in xrange(m):
            city_1,city_2 = map(int,raw_input().strip().split(' '))
            print "input", city_1, city_2
            if city_1 in log:
                if city_2 in log:
                    i,j = find_in_sublist(Networks,city_1), find_in_sublist(Networks,city_2)
                    if i != j:
                        Networks[i]= Networks[i] | Networks[j]
                        Networks.remove(Networks[j])
                else:
                    i = find_in_sublist(Networks,city_1)
                    Networks[i] = Networks[i] | set([city_2])
                    log += [city_2]
                    print "add c2", Networks
            elif city_2 in log:
                j = find_in_sublist(Networks,city_2)
                Networks[j] = Networks[j] | set([city_1])
                log += [city_1]
                print "add c1", Networks
            else:
                log += [city_1, city_2]
                Networks += [set([city_1, city_2])]
                print "add both", Networks
        print "Pre-calc", Networks
        print Lcost * (len(Networks) + n - len(log)) + Rcost * sum([len(N)-1 for N in Networks])
