# 45 - Triangular, pentagonal and hexagonal numbers
# Jeg prøvede Brute-force nedenunder - duede ikke!
from math import *


def is_pentagonal(n):
    if (1+(sqrt(1+24*n)))/6 % 1 == 0:
        return True


def is_triangle(n):
    if (-1+(sqrt(1+8*n)))/2 % 1 ==0:
        return True


i = 1
while True:		
    hex = i*(2*i-1)
    if (is_triangle(hex)) and (is_pentagonal(hex)):
        print (hex)
    i += 1

"""
limit = 10**8

triangle_bool = [False for i in range(limit)]
pentagonal_bool = [False for i in range(limit)]
hexagonal_bool = [False for i in range(limit)]

i = 1
tri = 1
while tri < limit:
    triangle_bool[tri] = True
    i += 1
    tri = int(i*(i+1)/2)

i = 1
pent = 1
while pent < limit:
    pentagonal_bool[pent] = True
    i += 1
    pent = int(i*(3*i-1)/2)

i = 1
hex = 1
while hex < limit:
    hexagonal_bool[hex] = True
    i += 1
    hex = int(i*(2*i-1))

for i in range(limit):
    if hexagonal_bool[i] == True:
        if pentagonal_bool[i]:
            if triangle_bool[i]:
                print (i)
"""