import timeit

start = timeit.default_timer()


def divisor_s(n):
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s += i
    return s


def amicable(n):
    if divisor_s(n) != n:
        if divisor_s(divisor_s(n)) == n:
            return True
        else:
            return False
    else:
        return False


s = 0		
for i in (range(10000)):
    if amicable(i):
        s += i

print (s)

print (timeit.default_timer() - start)