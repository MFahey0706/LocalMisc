#!/usr/bin/env python

"""
This module provides functions that calculate correlation (corr(x,y)), return a specified sequence from
a file (get_sequence(filename, variable)) and return the correlation of two sequences named "x" and "y"
in a given file (compare(filename)).
"""

__version__ = '1.0.0.0'

import stats
import csv

def corr(x,y):
    N=len(x)
    if len(y) != N:
        raise Exception("Sequences must be of the same length. X length: {0} ; Y length {1}".format(N,len(y)))
    else:
        sum = 0
        for index,xi in enumerate(x):
            sum += xi*y[index]
        r = (sum -N*stats.mean(x)*stats.mean(y))/((N-1)*stats.stdev(x)*stats.stdev(y))
        return r

def get_sequence(filename, variable):
    with open(filename, "rb") as source:
        rdr = csv.DictReader(source)
        series = [float(row[variable]) for row in rdr]
        return series

def compare(filename):
    x = get_sequence(filename,"x")
    y = get_sequence(filename,"y")
    r = round(corr(x,y),3)
    print("Correlation {0}".format(r))
    return r

if __name__ == "__main__":
    for filename in ['data/series_I.dat','data/series_II.dat','data/series_III.dat','data/series_IV.dat']:
        compare(filename)