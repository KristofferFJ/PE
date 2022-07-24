import unittest

"""
Weak Goodstein sequence


For any positive integer n, the nth weak Goodstein sequence {g1, g2, g3, ...} is defined as:


For example, the 6th weak Goodstein sequence is {6, 11, 17, 25, ...}:


It can be shown that every weak Goodstein sequence terminates.


Let G(n) be the number of nonzero elements in the nth weak Goodstein sequence.
It can be verified that G(2) = 3, G(4) = 21 and G(6) = 381.
It can also be verified that ∑ G(n) = 2517 for 1 ≤ n < 8.


Find the last 9 digits of ∑ G(n) for 1 ≤ n < 16.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
