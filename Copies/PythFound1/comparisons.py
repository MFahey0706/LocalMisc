'''
Edit this file to complete the exercises in
'Compare Values and do Stuff Based on the Result'
'''


superprime = False
long_standing_customer = True
large_down_payment = True

#Set 'mortgage_approved' equal to true when 'superprime'
#is True *or* when both 'long_standing_customer'
#and 'large_down_payment' are True.
mortgage_approved = None
if superprime == True or (long_standing_customer == True and large_down_payment == True):
	mortgage_approved = True





FICO = 732

#Set credit_description = "good" if FICO is greater than or
#equal to 700, credit_description = "ok" if FICO is less than
#700 but greater than or equal to 600, and
#credit_description = "bad" if FICO is less than 600.
credit_description = None
if FICO >= 700:
	credit_description = 'good'
elif FICO >= 600:\
	credit_description = 'ok'
else:
	credit_description = 'bad'
