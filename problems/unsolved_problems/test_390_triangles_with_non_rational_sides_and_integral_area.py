import unittest

"""
Triangles with non rational sides and integral area

Consider the triangle with sides $\sqrt 5$, $\sqrt {65}$ and $\sqrt {68}$.
It can be shown that this triangle has area $9$.
$S(n)$ is the sum of the areas of  all triangles with sides $\sqrt{1+b^2}$, $\sqrt {1+c^2}$ and $\sqrt{b^2+c^2}\,$ (for positive integers $b$ and $c$) that have an integral area not exceeding $n$.
The example triangle has $b=2$ and $c=8$.
$S(10^6)=18018206$.
Find $S(10^{10})$.
"""

class Test(unittest.TestCase):
    def test(self):
        pass
