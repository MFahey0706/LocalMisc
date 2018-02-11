# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import division
#Strategy: Always take the shortest order on the order list

###Take inputs
N= int(raw_input().strip()) #number of orders #Note: dont use .split(), bc split() will create a list when assigned to a single var
Full_order_list = []
for i in range(N):
    Full_order_list += [map(int,raw_input().strip().split(' '))]

###Setup    
Order_list = [] #list of orders that have been taken
temp = [] #temp var to hold an order
Kitchen_time = 0 #current time
Total_wait = 0 #total wait time for all customers
Orders_done = 0
Orders_taken = 0
Start = 0

###Complete orders
while Orders_done < N:
    
    #Collect orders up to current kitchen time
    
    Order_list += [Full_order_list[Orders_taken]]
    Orders_taken += 1
    #print "Orders", Order_list
    #print "Taken", Orders_taken, "Time", Kitchen_time
            
    #If the restaurant is empty, find the next order and update kitchen time
    if not Order_list:
        #take order from full list
        temp = Full_order_list[Orders_taken]
        Orders_taken += 1
        #add to current orders
        Order_list += [temp]
        #update kitchen time
        Kitchen_time = temp[0]
        #print "Orders", Order_list
        #print "Taken", Orders_taken, "Time", Kitchen_time

    #Take an order (min time among current ) and update kitchen time
    In_oven = min(Order_list, key= lambda x:x[1])
    Order_list.remove(In_oven)
    Kitchen_time += In_oven[1]
    Orders_done +=1
    Total_wait += (Kitchen_time - In_oven[0])
    #print "Done", In_oven
    #print "Tot Wait", Total_wait

print int(Total_wait / N)