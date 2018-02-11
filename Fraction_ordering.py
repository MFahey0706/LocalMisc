#
from __future__ import division
target = 3/7
stored_f = 0
stored_n = 0
stored_d = 1000000
n=428571
d=999999

while n > 3:
    if n/d >= target:
        n-=1
    else:
        if n/d > stored_f:
            stored_f, stored_n, stored_d = n/d, n, d
            print(stored_f, stored_n, stored_d)
        d-=1
    
