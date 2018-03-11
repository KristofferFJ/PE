import timeit
start = timeit.default_timer()


def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod


def digit_s(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


print(digit_s(factorial(10)))
print(digit_s(factorial(100)))

stop = timeit.default_timer()
print(stop - start)