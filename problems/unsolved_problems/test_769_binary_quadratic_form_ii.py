import unittest

# Binary Quadratic Form II
""" 
Consider the following binary quadratic form:
A positive integer $q$ has a primitive representation if there exist positive integers $x$ and $y$ such that $q = f(x,y)$ and $\gcd(x,y)=1$.
We are interested in primitive representations of perfect squares. For example:
$17^2=f(1,9)$
$87^2=f(13,40) = f(46,19)$
Define $C(N)$ as the total number of primitive representations of $z^2$ for $0 < z \leq N$. 
Multiple representations are counted separately, so for example $z=87$ is counted twice.
You are given $C(10^3)=142$ and $C(10^{6})=142463$ 
Find $C(10^{14})$.
""" 


class Test(unittest.TestCase):
    def test(self):
        pass
