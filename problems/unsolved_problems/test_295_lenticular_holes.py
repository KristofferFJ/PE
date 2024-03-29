import unittest

"""
Lenticular holes

We call the convex area enclosed by two circles a lenticular hole if:

Consider the circles:
C0: x2+y2=25
C1: (x+4)2+(y-4)2=1
C2: (x-12)2+(y-4)2=65


The circles C0, C1 and C2 are drawn in the picture below.

C0 and C1 form a lenticular hole, as well as C0 and C2.

We call an ordered pair of positive real numbers (r1, r2) a lenticular pair if there exist two circles with radii r1 and r2 that form a lenticular hole.
We can verify that (1, 5) and (5, √65) are the lenticular pairs of the example above.

Let L(N) be the number of distinct lenticular pairs (r1, r2) for which 0 < r1 ≤ r2 ≤ N.
We can verify that L(10) = 30 and L(100) = 3442.

Find L(100 000).

"""


class Test(unittest.TestCase):
    def test(self):
        pass
