# CIRCULAR PRIMES
# Hvilke primtal under 10**6 er primtal for alle ciffernes permutationer?

from library.primes import primes_bool_up_to

num = 10**6
list = primes_bool_up_to(num)
plist = [i for i in range(len(list)) if list[i]]

count = 0
# Forkert løsning. Alle permutationer tjekkes, men vi skal kun tjekke rotation af cifrene.
"""for i in plist:
    prime = True
    c = []
    for ciffer in str(i):
        c.append(int(ciffer))
    for j in permutations(c):
        num_string = ""
        for k in j:
            num_string = num_string + str(k)
        if list[int(num_string)] == False:
            prime = False
            break
    if prime == True:
        count += 1
        print (i)"""

for i in plist:
    k = i
    prime = True
    pot = len(str(i)) - 1
    for j in range(len(str(i))-1):
        i = 10**pot*(i % 10) + i//10
        if not list[i]:
            prime = False
            break
    if prime:
        count += 1
        print("Succes ved "+str(k))

print(count)
