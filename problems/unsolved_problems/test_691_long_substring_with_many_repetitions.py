import unittest

"""
Long substring with many repetitions

Given a character string $s$, we define $L(k,s)$ to be the length of the longest substring of $s$ which appears at least $k$ times in $s$, or $0$ if such a substring does not exist. For example, $L(3,\text{“bbabcabcabcacba”})=4$ because of the three occurrences of the substring $\text{“abca”}$, and $L(2,\text{“bbabcabcabcacba”})=7$ because of the repeated substring $\text{“abcabca”}$. Note that the occurrences can overlap.
Let $a_n$, $b_n$ and $c_n$ be the $0/1$ sequences defined by:
and $S_n$ the character string $c_0\ldots c_{n-1}$. You are given that $L(2,S_{10})=5$, $L(3,S_{10})=2$, $L(2,S_{100})=14$, $L(4,S_{100})=6$, $L(2,S_{1000})=86$, $L(3,S_{1000}) = 45$, $L(5,S_{1000}) = 31$, and that the sum of non-zero $L(k,S_{1000})$ for $k\ge 1$ is $2460$.
Find the sum of non-zero $L(k,S_{5000000})$ for $k\ge 1$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
