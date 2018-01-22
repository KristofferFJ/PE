#207 - Integer partition equations

from math import *
import time
start = time.time()

limit = 10**7

m = [i for i in range(3,limit+1)]
k = [i*(i-1) for i in m]

def t(n):
	return log(1/2 * (sqrt(4*n + 1) + 1))/log(2)

succes = 1
tries = 1
		
res = 1/12345

num = 0
while (succes/tries) > res:
	if t(k[num]) % 1 == 0:
		succes += 1
		tries += 1
	else:
		tries += 1
	num += 1
print (k[num],time.time()-start)