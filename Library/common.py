# ALMINDELIGE FUNKTIONER


def factors(n):
    factor_list = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                factor_list.append(i)
                break
    return factor_list

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
