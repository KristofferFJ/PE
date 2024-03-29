import unittest

"""
Counting Binary Matrices

A binary matrix is a matrix consisting entirely of 0s and 1s. Consider the following transformations that can be performed on a binary matrix:
Two binary matrices $A$ and $B$ will be considered equivalent if there is a sequence of such transformations that when applied to $A$ yields $B$. For example, the following two matrices are equivalent:
via the sequence of two transformations "Flip all elements in column 3" followed by "Swap rows 1 and 2".
Define $c(n)$ to be the maximum number of $n\times n$ binary matrices that can be found such that no two are equivalent. For example, $c(3)=3$. You are also given that $c(5)=39$ and $c(8)=656108$.
Find $c(20)$, and give your answer modulo $1\,001\,001\,011$.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
