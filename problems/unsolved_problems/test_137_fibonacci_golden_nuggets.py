import unittest

# Fibonacci golden nuggets
"""
Consider the infinite polynomial series $A_F(x) = x F_1 + x^2 F_2 + x^3 F_3 + \dots$, where $F_k$ is the $k$th term in the Fibonacci sequence: $1, 1, 2, 3, 5, 8, \dots$; that is, $F_k = F_{k-1} + F_{k-2}$, $F_1 = 1$ and $F_2 = 1$.
For this problem we shall be interested in values of $x$ for which $A_F(x)$ is a positive integer.
The corresponding values of x for the first five natural numbers are shown below.
We shall call $A_F(x)$ a golden nugget if $x$ is rational, because they become increasingly rarer; for example, the 10th golden nugget is 74049690.
Find the 15th golden nugget.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
