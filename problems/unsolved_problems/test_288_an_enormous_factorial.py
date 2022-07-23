import unittest

# An enormous factorial
"""

For any prime p the number N(p,q) is defined by
N(p,q) = ∑n=0 to q Tn*pn with Tn generated by the following random number generator:

S0 = 290797
Sn+1 = Sn2 mod 50515093
Tn = Sn mod p


Let Nfac(p,q) be the factorial of N(p,q).
Let NF(p,q) be the number of factors p in Nfac(p,q).


You are given that NF(3,10000) mod 320=624955285.


Find NF(61,107) mod 6110
"""


class Test(unittest.TestCase):
    def test(self):
        pass
