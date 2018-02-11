#sum of even numbers in Fibonacci sequence less than or equal to 4mm

x,y,z=1,1,2
tot=0
while z <= 4000000:
    tot+=z
    x=y+z
    y=z+x
    z=x+y

print tot