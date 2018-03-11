import timeit
start = timeit.default_timer()

num = 2 * 10**6
primes = [True] * (num)


def find_primes(list):
    for i in range(2,num):
        n = 2
        while i * n <= len(list)-1:
            primes[i*n] = False
            n += 1
    return primes


find_primes(primes)


def s_primes(list):
    s = 0
    for i in range(2,len(list)):
        if list[i]:
            s += i
    return s


print(s_primes(primes))

stop = timeit.default_timer()
print(stop - start)
