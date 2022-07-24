import unittest

# 10001st prime
from library.primes import Primes

""" 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
""" 


class Test(unittest.TestCase):
    def test(self):
        print(Primes.first_n_primes(15000)[10000])
        # 104743
