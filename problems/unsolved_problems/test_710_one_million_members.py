import unittest

# One Million Members
"""
The number 6 can be written as a palindromic sum in exactly eight different ways:
We shall define a twopal to be a palindromic tuple having at least one element with a value of 2. It should also be noted that elements are not restricted to single digits. For example, $(3, 2, 13, 6, 13, 2, 3)$ is a valid twopal.
If we let $t(n)$ be the number of twopals whose elements sum to $n$, then it can be seen that $t(6) = 4$:
Similarly, $t(20) = 824$.
In searching for the answer to the ultimate question of life, the universe, and everything, it can be verified that $t(42) = 1999923$, which happens to be the first value of $t(n)$ that exceeds one million.
However, your challenge to the "ultimatest" question of life, the universe, and everything is to find the least value of $n \gt 42$ such that $t(n)$ is divisible by one million.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
