#613 - PYTHAGOREAN ANT
#Hvad er sandsynligheden for at en myre i en trekant med
#sidelængderne 3, 4 og 5 forlader trekanten gennem den
#længste side?
#IDÉ
#Del trekanten op i en masse små punkter (flere hvis der
#manger præcision) og for hver af dem udregn sandsynligheden
#for at den forlader gennem den længste side (vinklen mellem
#myrens udgangspunkt og endepunkterne for den længste side /
#2pi radianer).
#0.391641135378 ved 10**3
#0.391656651071 ved 2*10**3

"""
import numpy as np
import time
time.clock

bignum = 10**3
x_coordinates = [i for i in range(4*bignum)]
y_coordinates = [i for i in range(3*bignum)]

def in_triangle(x,y):
	if (-3/4)*x+3*bignum >= y:
		return True
	else:
		return False

def prob_5(x,y):
	return np.arccos((x**2+y**2-(4*bignum*x+3*bignum*y))/np.sqrt((x**2+(3*bignum-y)**2)*(y**2+(4*bignum-x)**2)))/(2*np.pi)
	
count = 0
prob_s = 0
for x in x_coordinates:
	for y in y_coordinates:
		if in_triangle(x,y):
			count += 1
			prob_s += prob_5(x,y)
	

print (time.clock())
"""

#Lånt fra ProjectEuler

from scipy import integrate
from math import *

def f(x, y):
	u = [0.0-x, 3.0-y]
	v = [4.0-x, 0.0-y]
	dot = u[0]*v[0] + u[1]*v[1]
	length_u = sqrt(u[0]**2 + u[1]**2)
	length_v = sqrt(v[0]**2 + v[1]**2)
	return acos(dot/(length_u * length_v))/(2*pi)
	
def bounds_x(y):
	return [0.0, 4.0-(4.0/3.0)*y]

def bounds_y():
	return [0.0, 3.0]

res = integrate.nquad(f, [bounds_x, bounds_y])
print (res[0]/6)










		