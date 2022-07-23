# 587 - Concave triangle
# We find the intersection and integrate the function.
# Circle is y = - sqrt(1-x^2) + 1 (if centered in (0,1))
# And line is y = 1/n * x + 1/n (where n is number of circles.)
# Intersection is then: x = (-sqrt(2) * n**(3/2) + n - 1)/(n**2 + 1)

from math import *
from scipy import integrate


def f(x):
    return -sqrt(1 - x**2) + 1


def intersection(n):
    return (-sqrt(2) * n**(3/2) + n - 1)/(n**2 + 1)


# So we can return the result as a percentage of the area.
area = (integrate.quad(f, -1, 0)[0])


# The integral under the curve for some n
def int(n):
    res = integrate.quad(f, intersection(n), 0)[0]
    # + the triangle:
    res += (intersection(n) - (-1))*(1/n * intersection(n) + 1/n)/2
    return res/area


i = 1
while int(i) > 0.001:
    i += 1

print(i)
