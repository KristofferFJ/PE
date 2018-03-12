import timeit

start = timeit.default_timer()

num = 5*10**7


def sieve(n):
    sieve[0]=sieve[1]=False
    sieve = [True]*(n+1)
    for i in range(2,int(n**.5)+1):
        ii = i*i
        if sieve[i]:
            while ii <= n:
                sieve[ii] = False
                ii += i
    return sieve


primes = sieve(8000)
print (primes)


def is_prime(n):
    return primes[n]


def calc(N):
    nums = set()
    for i in range(2, int(N**.5)+1):
        if is_prime(i):
            print ("Vi kører med %s" % i)
            for j in range(2, int((N-i**2)**(1./3))+1):
                if is_prime(j):
                    for k in range(2, int((N-i**2-j**3)**.25)+1):
                        if is_prime(k):
                            nums.add(i**2+j**3+k**4)
    return len(nums)


print(calc(num))

print(timeit.default_timer() - start)
