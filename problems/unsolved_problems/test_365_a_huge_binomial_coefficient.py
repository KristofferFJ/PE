import unittest

"""
A huge binomial coefficient


The binomial coefficient $\displaystyle{\binom{10^{18}}{10^9}}$ is a number with more than 9 billion ($9\times 10^9$) digits.


Let $M(n,k,m)$ denote the binomial coefficient $\displaystyle{\binom{n}{k}}$ modulo $m$.


Calculate $\displaystyle{\sum M(10^{18},10^9,p\cdot q\cdot r)}$ for $1000\lt p\lt q\lt r\lt 5000$ and $p$,$q$,$r$ prime.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
