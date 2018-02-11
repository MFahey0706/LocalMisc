'''
Edit this file to complete the exercises in
'Print to Screen and Transform Strings'
'''

#Just to get you going, here's the answer to
#the first exercise:
print("Change Banking For Good.")

import math
e = math.e
#Now print "e to 10 decimal places: ", followed by the
#numerical value of e out to 10 decimal places, using
#string formatting and e, defined above.
print('e to 10 decimal places:{0:11.10f}'.format(e))

mixed_case_string = "cHAngE BANKing fOR GooD."
#Set lower_case_string equal to mixed_case_string, only
#with all lower case letters.
lower_case_string = mixed_case_string.lower()

print("Is this string lowercase? {0:s}".format(lower_case_string))

#The first paragraph of Capital One's Wikipedia article
#(Accessed 4/20/2015):
wiki_intro = "Capital One Financial Corporation is a U.S."\
  "-based bank holding company specializing in credit cards,"\
  " home loans, auto loans, banking and savings products. When "\
  "measured in terms of total assets and deposits, Capital One is "\
  "the eighth largest bank holding company in the United States. "\
  "As of 2012, The bank has 963 Capital One Bank Branches including "\
  "10 cafe style locations for their Capital One 360 brand and 2,000 "\
  "ATMs. Capital One Financial is a member of the Fortune 500, and "\
  "also conducts business in Canada and the United Kingdom. The "\
  "company helped pioneer the mass marketing of credit cards in "\
  "the 1990s, and it is now the fourth-largest customer of the "\
  "United States Postal Service."
  
#set num_branches to equal the 311th through 313th characters
#of the wiki_intro string. Note that wiki_intro uses linebreaks
#(backslashes \) to make this long string easier to read. The
#linebreaks don't count as a character in the string.
num_branches = wiki_intro[310:313]
#print(num_branches)

#set wiki_intro_nospaces to equal wiki_intro, but with *ALL* of
#the spaces removed - e.g. "Capital One Financial Corporation"
#becomes "CapitalOneFinancialCorporation".
wiki_intro_nospaces = wiki_intro.replace(" ","")
