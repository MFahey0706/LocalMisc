# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

F, N = map(int,raw_input().strip().split(' '))

m = []
for i in range(N):
    m += [map(float,raw_input().strip().split(' '))]
  
a = np.matrix(m)
y = a[:,2]
a=np.delete(a,2,axis=1)

x=[]
for j in range(0,F):
    for k in range(0,j):
        for exp1 in range(0,4):
            for exp2 in range(0,4-exp1):
                x += [np.multiply(map(lambda z:z**exp1,a.T.tolist()[j]),map(lambda z:z**exp2,a.T.tolist()[k]))]
                
x = np.matrix(x).T
#x >> 1, x1, x2, x1^2, x2^2, x1^3, x2^3, x1x2, x1^2x2, x2^2x1

b = (((x.T)*x).I)*(x.T)*y:

R = int(raw_input())
s=[]
for i in range(R):
    s+=[map(float,raw_input().strip().split(' '))]
    
s=np.matrix(s)
x_test = []
for j in range(0,F):
    for k in range(0,j):
        for exp1 in range(0,4):
            for exp2 in range(0,4-exp1):
                x_test += [np.multiply(map(lambda z:z**exp1,s.T.tolist()[j]),map(lambda z:z**exp2,s.T.tolist()[k]))]

x_test = np.matrix(x_test).T

y_pred = x_test * b

for pred in y_pred.A1:
    print pred