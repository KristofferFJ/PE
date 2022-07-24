import unittest

"""
Totient Chains

Let φ be Euler's totient function, i.e. for a natural number n,
φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.
By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.
E.g. if we start with 5 the sequence 5,4,2,1 is generated.
Here is a listing of all chains with length 4:
Only two of these chains start with a prime, their sum is 12.
What is the sum of all primes less than 40000000 which generate a chain of length 25?
"""

class Test(unittest.TestCase):
    def test(self):
        pass
