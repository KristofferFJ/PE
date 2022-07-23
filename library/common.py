import unittest


class Common:
    @staticmethod
    def prime_factors(n):
        factor_list = []
        while n != 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    n = n // i
                    factor_list.append(i)
                    break
        return factor_list

    @staticmethod
    def factors(n):
        prime_factor_list = Common.prime_factors(n)
        factors = set([])
        Common.add_factors(factors, prime_factor_list, 1)
        return factors

    @staticmethod
    def add_factors(factor_set, remaining_primes, factor_num):
        if len(remaining_primes) == 1:
            for i in range(2):
                factor_num *= remaining_primes[0] ** i
                factor_set.add(factor_num)
        else:
            new_factor = remaining_primes[0]
            new_remaning_primes = remaining_primes[1:]
            for i in range(2):
                new_factor_num = factor_num * new_factor ** i
                Common.add_factors(factor_set, new_remaning_primes, new_factor_num)

    @staticmethod
    def fact(n):
        if n == 0:
            return 1
        elif n == 1:
            return n
        else:
            return n * Common.fact(n - 1)

    @staticmethod
    def anagrams(n, m):
        n_number_string, m_number_string = str(n), str(m)
        value = True
        for i in range(10):
            if n_number_string.count(str(i)) != m_number_string.count(str(i)):
                value = False
        return value

    @staticmethod
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    @staticmethod
    def sum_of_digits(n):
        return sum([int(m) for m in str(n)])


class Test(unittest.TestCase):
    def test_sum_of_digits(self):
        assert Common.sum_of_digits(1234) == 10
