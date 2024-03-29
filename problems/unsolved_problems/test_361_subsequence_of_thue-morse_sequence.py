import unittest

"""
Subsequence of Thue-Morse sequence

The Thue-Morse sequence {Tn} is a binary sequence satisfying:

The first several terms of {Tn} are given as follows:
01101001100101101001011001101001....


We define {An} as the sorted sequence of integers such that the binary expression of each element appears as a subsequence in {Tn}.
For example, the decimal number 18 is expressed as 10010 in binary. 10010 appears in {Tn} (T8 to T12), so 18 is an element of {An}.
The decimal number 14 is expressed as 1110 in binary. 1110 never appears in {Tn}, so 14 is not an element of {An}.


The first several terms of An are given as follows:

We can also verify that A100 = 3251 and A1000 = 80852364498.


Find the last 9 digits of $\sum \limits_{k = 1}^{18} {A_{10^k}}$.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
