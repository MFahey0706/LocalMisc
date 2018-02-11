file = open('numlist_100_50.txt')
nums = file.read().upper()
numlist = map(int,[n for n in nums.splitlines()])

a=0
for i in numlist:
    a+=i

print str(a)[0:10]

