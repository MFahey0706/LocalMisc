'''
Edit this file to complete the exercises in
'Iterate over Data with for Loops'

Edit this file to complete the exercises in
'Iterating over Data with for Loops and Comprehensions'
'''

#----------------------------------------------------------------------------
#Boilerplate code to set up the exercises. DO NOT MODIFY!
import random
random.seed(891)
account_id_list = range(1,51)
account_balance_list = [random.randint(-2000,2000) for id in account_id_list]
#End boilerplate.
#----------------------------------------------------------------------------

#Set total_balance equal to the sum of all the items in
#account_balance_list:
total_balance = 0
for balance in account_balance_list:
    total_balance = total_balance + balance

#set total_credit_balance equal to the sum of all the items
#in account_balance_list that are greater than or equal to zero.
#Additionally, set num_accounts_with_credit equal to the number
#of items that meet this criteria:
total_credit_balance = 0
num_accounts_with_credit = 0
for b in account_balance_list:
	if b >= 0:
		total_credit_balance += b
		num_accounts_with_credit += 1

#set account_id_debt_list equal to a list of all the items
#in account_id_list that correspond (have the same index)
#as items in account_balance_list that are less than zero:
account_id_debt_list = [account_id_list[i] for i,b in enumerate(account_balance_list) if b < 0 ]

#set all balances less than zero to be zero in account_balance_list:
account_balance_list = [max(b,0) for b in account_balance_list]
