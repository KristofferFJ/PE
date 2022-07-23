# ALMINDELIGE FUNKTIONER


def prime_factors(n):
    factor_list = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                factor_list.append(i)
                break
    return factor_list


def factors(n):
    prime_factor_list = prime_factors(n)
    factors = set([])
    add_factors(factors, prime_factor_list, 1)
    return factors


def add_factors(factor_set, remaining_primes, factor_num):
    if len(remaining_primes) == 1:
        for i in range(2):
            factor_num *= remaining_primes[0]**i
            factor_set.add(factor_num)
    else:
        new_factor = remaining_primes[0]
        new_remaning_primes = remaining_primes[1:]
        for i in range(2):
            new_factor_num = factor_num * new_factor**i
            add_factors(factor_set, new_remaning_primes, new_factor_num)


if __name__ == '__main__':
    print("24 har faktorerne: %s" % (factors(24)))


def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n*fact(n-1)


def anagrams(n, m):
    n_number_string, m_number_string = str(n), str(m)
    value = True
    for i in range(10):
        if n_number_string.count(str(i)) != m_number_string.count(str(i)):
            value = False
    return value


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
