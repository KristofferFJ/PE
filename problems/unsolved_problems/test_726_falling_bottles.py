import unittest

"""
Falling bottles


Consider a stack of bottles of wine. There are $n$ layers in the stack with the top layer containing only one bottle and the bottom layer containing $n$ bottles. For $n=4$ the stack looks like the picture below.


The collapsing process happens every time a bottle is taken. A space is created in the stack and that space is filled according to the following recursive steps:


This process happens recursively; for example, taking bottle $A$ in the diagram above. Its place can be filled with either $B$ or $C$. If it is filled with $C$ then the space that $C$ creates can be filled with $D$ or $E$. So there are 3 different collapsing processes that can happen if $A$ is taken, although the final shape (in this case) is the same.


Define $f(n)$ to be the number of ways that we can take all the bottles from a stack with $n$ layers. 
Two ways are considered different if at any step we took a different bottle or the collapsing process went differently.


You are given $f(1) = 1$, $f(2) = 6$ and $f(3) = 1008$.


Find $S(10^4)$ and give your answer modulo $1\,000\,000\,033$.

"""


class Test(unittest.TestCase):
    def test(self):
        pass
