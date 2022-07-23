#COUNTING PRIMITIVE PYTHAGOREAN TRIPLES
#Ufærdig - hmm

from numpy import matrix
from numpy import linalg
import time

start = time.time()
bignum = 3141592653589793
# bignum = 10**6


A = matrix([[1,2,2],[-2,-1,-2],[2,2,3]])
B = matrix([[1,2,2],[2,1,2],[2,2,3]])
C = matrix([[-1,-2,-2],[2,1,2],[2,2,3]])

M = matrix([[3,4,5]])

print(M*A)
print(M*B)
print(M*C)
print((M*A)*A)
print((M*A)*B)
print((M*A)*C)


print(time.time()-start)