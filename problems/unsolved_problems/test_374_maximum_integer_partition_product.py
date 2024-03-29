import unittest

"""
Maximum Integer Partition Product

An integer partition of a number n is a way of writing n as a sum of positive integers.
Partitions that differ only in the order of their summands are considered the same.
A partition of n into distinct parts is a partition of n in which every part occurs at most once.
The partitions of 5 into distinct parts are:
5, 4+1 and 3+2.
Let f(n) be the maximum product of the parts of any such partition of n into distinct parts and let m(n) be the number of elements of any such partition of n with that product.
So f(5)=6 and m(5)=2.
For n=10 the partition with the largest product is 10=2+3+5, which gives f(10)=30 and m(10)=3.
And their product, f(10)·m(10) = 30·3 = 90
It can be verified that
∑ f(n)·m(n) for 1 ≤ n ≤ 100 = 1683550844462.
Find ∑ f(n)·m(n) for 1 ≤ n ≤ 1014.
Give your answer modulo 982451653, the 50 millionth prime.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
