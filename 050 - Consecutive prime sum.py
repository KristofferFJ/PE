from common import primes

primebool = primes(10**6)
plist = [p for p in range(len(primebool)) if primebool[p]]
record = 21
prime = 0


def finder(n):
    n = n + 2
    k = 0
    min = 0
    while min < 10**6:
        s = 0
        for i in range(n):
            s += plist[k+i]
        if primebool[s]:
            print ("Fundet ved %s, start ved %s" % (s, plist[k+i]))
            print ("Med længden "+str(n))
            break
        else:
            k += 1
            min = s(plist[k+j] for j in range(n))


while record < 10**4:
    finder(record+2)
    record += 2
