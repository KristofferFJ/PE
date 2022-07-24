import unittest

"""
Generating polygons


A polygon is a flat shape consisting of straight line segments that are joined to form a closed chain or circuit. A polygon consists of at least three sides and does not self-intersect.


A set S of positive numbers is said to generate a polygon P if:

For example:
The set {3, 4, 5} generates a polygon with sides 3, 4, and 5 (a triangle).
The set {6, 9, 11, 24} generates a polygon with sides 6, 9, 11, and 24 (a quadrilateral).
The sets {1, 2, 3} and {2, 3, 4, 9} do not generate any polygon at all.

Consider the sequence s, defined as follows:

Let Un be the set {s1, s2, ..., sn}. For example, U10 = {1, 2, 3, 4, 6, 9, 13, 19, 28, 41}.
Let f(n) be the number of subsets of Un which generate at least one polygon.
For example, f(5) = 7, f(10) = 501 and f(25) = 18635853.


Find the last 9 digits of f(1018).

"""


class Test(unittest.TestCase):
    def test(self):
        pass
