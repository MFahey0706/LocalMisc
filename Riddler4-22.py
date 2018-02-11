#python Riddler4-22.py
#import necessary tools
from __future__ import division
from fractions import Fraction
from decimal import Decimal

#create function to calculate expected occupied houses in nbrhd size m, 
#1st occupied house at position p

#test
print "v1.5"

def Riddle(max_nbrhd_size, list=[], p=1):
	if max_nbrhd_size <= 0:
		return 0
	
	#for recursion purposes, 
	#if we already know the answer for this size just return it
	if len(list) > 0 and list[max_nbrhd_size-1] > 0:
		return list[max_nbrhd_size-1]
	
	flist=[]
	
	#initialize the list of answers with 0s
	for z in range (0,max_nbrhd_size):
		list.append(0)
		flist.append(0)
	
	#test
	if p == 2:
		print list
	
	#for each neighborhood size up to the max
	for i in range(1,max_nbrhd_size+1):
		#init variables	
		num_occ = Decimal(0.0)
		frac_occ = Decimal(0.0)
		
		if p==2:
			print "\n Calculating for size %d" % i
		
		#for each possible first home position in the nbrhd of size i
		for j in range(1,i+1):
			#recursion - wooooooh
			num_occ += Decimal(1+Riddle(j-2,list,0)+Riddle(i-j-1,list,0))
			if p == 2:
				print "out %d" % j
				print Riddle(j-2,list,0)
				print Riddle(i-j-1,list,0)
				print num_occ
		
		num_occ= Decimal(num_occ/i)
		frac_occ = Decimal(num_occ/i)
		list[i-1] = round(num_occ,4)
		flist[i-1] = round(frac_occ,4)
		
		if p == 2:
			print "E[number occupied] =" 
			print num_occ
			print "E[fraction occupied] =" 
			print frac_occ
	
	if p == 1:
		print "Done"
		print list
		print flist
		
	return num_occ

#print "It's been defined - now let's test it"	
#Riddle(1)
#Riddle(2)
#Riddle(5)
Riddle(100)	

#well crap... it's not converging... or it is but very very slowly	
			