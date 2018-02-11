#!/usr/bin/env python

"""
This is a module containing functions to calculate the arithmetic mean (mean())
or standard deviation (stdev()) of a sequence of numbers.
We provide examples below:

>>> mean([2, 4, 4, 4, 5, 5, 7, 9])
5.0

>>> round(stdev([2, 4, 4, 4, 5, 5, 7, 9]),3)
2.138
"""

__version__ = '1.0.0.0'

def mean(sequence):
    N = len(sequence)
    sum = 0
    for element in sequence:
        sum += element
    mean = sum/N
    return mean

def stdev(sequence):
    N_minus_one = len(sequence)-1
    sum_squared_error = 0
    sample_mean = mean(sequence)
    for element in sequence:
        sum_squared_error += (element - sample_mean)**2
    stdev = (sum_squared_error/N_minus_one)**(0.5)
    return stdev

if __name__ == "__main__":
    sequence = [2, 4, 4, 4, 5, 5, 7, 9]
    print("Mean of {0} is {1}".format(sequence,mean(sequence)))
    print("Standard deviation of {0} is {1}".format(sequence,stdev(sequence)))