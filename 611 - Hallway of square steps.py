# 611 Hallway


"""
bignum = 10**12 + 1
list = [0]*bignum

smallnum = bignum**0.5 // 1
i = 1
while i <= smallnum:
    j = i+1
    temp = i**2 + j**2
    while temp < bignum:
        list[temp] = (list[temp] + 1) % 2
        j += 1
        temp = i**2 + j**2
    i += 1"""


# OVERFLOW OG FOR LANGSOM
bignum = 10**12
list = set([])
"""
smallnum = int(bignum**0.5)
i = 1
while i <= smallnum:
    j = i+1
    temp = i**2 + j**2
    while temp < bignum+1:
        if temp in list:
            list.remove(temp)
            print ("fjerner "+str(temp))
        else:
            list.add(temp)
            print ("tilføjer "+str(temp))
        j += 1
        temp = i**2 + j**2
    i += 1
    
print (s(1 for i in list))"""


# Finder alle muligheder. Slet gengangere.
pot = 0
for i in range(1,int((bignum/2)**0.5)):
    pot += int((bignum - i**2)**0.5) - (i)

print (pot)