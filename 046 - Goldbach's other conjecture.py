# Goldbach's other conjecture:
# Kan ethvert ulige tal skrives som smen af 2*kvadrat + primtal?

import timeit
start = timeit.default_timer()

num = 10**4
list = [True]*(num+1)
list[0] = list[1] = False
for i in range(2, int(num**.5)):
    ii = i*i
    while ii <= num:
        list[ii] = False
        ii += i

comp = []
for i in range(1,num//2-1):
    if not list[2*i+1]:
        comp.append(2*i+1)


def goldbach(n):
    found = False
    for i in range(1,int(((n/2)**.5))+1):
        if list[n - (i**2)*2]:
            found = True
    if not found:
        print ("Vi fandt det ikke for n = "+str(n))


for i in range(len(comp)):
    goldbach(comp[i])

print(timeit.default_timer() - start)