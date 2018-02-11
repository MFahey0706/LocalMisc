#!/bin/python

import sys

def matrixRotation(r,matrix):
    # Complete this function
    m, n = len(matrix[0]), len(matrix)
    cmin,cmax,rmin,rmax = 0,m-1,0,n-1
    temp_m = [['']*m for i in range(n)]
    
    #rotation
    while cmin < cmax and rmin < rmax:
        #corners
        temp_m[rmin][cmin] = matrix[rmin][cmin+1]
        temp_m[rmin][cmax] = matrix[rmin+1][cmax]
        temp_m[rmax][cmax] = matrix[rmax][cmax-1]
        temp_m[rmax][cmin] = matrix[rmax-1][cmin]
        #edges
        if cmin+1 < cmax:
            for i in range(cmin+1,cmax):
                temp_m[rmax][i] = matrix[rmax][i-1]
                temp_m[rmin][i] = matrix[rmin][i+1]   
        if rmin+1 < rmax:
            for j in range(rmin+1,rmax):
                temp_m[j][cmin] = matrix[j-1][cmin]
                temp_m[j][cmax] = matrix[j+1][cmax] 
        #step
        cmin,cmax,rmin,rmax = cmin+1,cmax-1,rmin+1,rmax-1
    if r == 1:
        return temp_m
    else:
        return matrixRotation(r-1,temp_m)
    
if __name__ == "__main__":
    m, n, r = raw_input().strip().split(' ')
    m, n, r = [int(m), int(n), int(r)]
    matrix = []
    for matrix_i in xrange(m):
        matrix_temp = map(int,raw_input().strip().split(' '))
        matrix.append(matrix_temp)
    result = matrixRotation(r,matrix)
    for r in result:
        for c in r:
            print c,
        print ''