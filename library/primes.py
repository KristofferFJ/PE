from math import ceil, log


def primes_up_to(n):
    primes_bool = [True]*n
    prime_list = []
    primes_bool[0] = primes_bool[1] = False
    for i in range(2, int(n**.5)):
        if primes_bool[i]:
            prime_list.append(i)
            ii = i*i
            while ii < n:
                primes_bool[ii] = False
                ii += i
    for i in range(int(n**.5), n):
        if primes_bool[i]:
            prime_list.append(i)
    return prime_list


def primes_bool_up_to(n):
    primes_bool = [True]*n
    primes_bool[0] = primes_bool[1] = False
    for i in range(2, int(n**.5)):
        if primes_bool[i]:
            ii = i*i
            while ii < n:
                primes_bool[ii] = False
                ii += i
    return primes_bool


def first_n_primes(n):
    num = ceil(n * log(n))
    primes_bool = [True]*ceil(n * log(n))
    prime_list = []
    primes_bool[0] = primes_bool[1] = False
    for i in range(2, int(num**.5)):
        if primes_bool[i]:
            prime_list.append(i)
            ii = i*i
            while ii < num:
                primes_bool[ii] = False
                ii += i
    for i in range(int(num**.5), num):
        if primes_bool[i]:
            prime_list.append(i)
    return prime_list


