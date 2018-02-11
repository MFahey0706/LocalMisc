# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import division
from heapq import heappush, heappop
#Strategy: Always take the shortest order on the order list

###Take inputs
N= int(raw_input().strip()) #number of orders #Note: dont use .split(), bc split() will create a list when assigned to a single var
Full_order_list = [] #This will be a heap
for i in range(N):
    heappush(Full_order_list, map(int,raw_input().strip().split(' ')))

###Setup    
Order_list = [] #list of orders that have been taken; this will be a heap
Total_wait = 0 #total wait time for all customers
Next_order_time = 0 #helper var
Kitchen_time = 0

###Complete orders 
while Full_order_list or Order_list:
    #print "Lists", Full_order_list, Order_list, "Time", Kitchen_time
    #If the restaurant is empty, find the next order and update kitchen time
    if Full_order_list and not Order_list:
        #update kitchen time if we had to wait
        Kitchen_time = max(Kitchen_time, Full_order_list[0][0])
        #pop order from full list and push to current orders
        heappush(Order_list, heappop(Full_order_list)[::-1])#this heap ordered by cook time
        if Full_order_list:
            Next_order_time = Full_order_list[0][0]
            
    #print "Lists", Full_order_list, Order_list, "Times", Kitchen_time, Next_order_time      
    #Collect orders up to current kitchen time
    while Full_order_list and Next_order_time <= Kitchen_time:
        heappush(Order_list, heappop(Full_order_list)[::-1])#this heap ordered by cook time
        if Full_order_list:
            Next_order_time = Full_order_list[0][0]
            
    #Take an order (min time among current ) and update kitchen time
    In_oven = heappop(Order_list)
    Kitchen_time += In_oven[0]
    Total_wait += (Kitchen_time - In_oven[1])
    #print In_oven, "cook_end_time", Kitchen_time
    
print int(Total_wait / N)