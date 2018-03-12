# 401 - s OF SQUARE OF DIVISORS
import timeit
start = timeit.default_timer()

'''
Hver divisor d er repræsenteret n//d gange.
Alle tal større end n/2 er kun repræsenteret én gang, tal større end n/3 2 gange o.s.v.
Tal	1	2	3	4	5	6	7	8	9	10
Rep.	10	5	3	2	2	1	1	1	1	1
Spring		5	2		1					1
Eks: Start vi med 2n+1
Vi laver smerne ved 5 f.eks.: 5^2 + 4^2 + 3^2 + 2^1 + 1^2 o.s.v.
Hver af de næste skal gentages med det forriges spring #gange, før de blive rep. nok.
'''


def s_of_squares(n):
    # Summen af 1^2 + 2^2 + ... + n^2 udover at jeg ikke dividerer med 6.
    # Gemmer det til sidste for kun at dividere én gang.
    return int(n*(n+1)*(2*n+1))


def s_of_divisor_squares(n):
    s = 0
    i = 1
    while i < n + 1:
        num = n//i
        repeats = n//num - i + 1
        s = (s + repeats*s_of_squares(num))
        i += repeats
    s = (s//6) % 10**9
    return s, i


print(s_of_divisor_squares(10**15))
print(timeit.default_timer() - start)