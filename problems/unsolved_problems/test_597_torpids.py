import unittest

# Torpids
""" 

Suppose that, in a particular race, each boat $B_j$ rows at a steady speed $v_j = -$log$X_j$ metres per second, where the $X_j$ are chosen randomly (with uniform distribution) between 0 and 1, independently from one another. These speeds are relative to the riverbank: you may disregard the flow of the river.


Let $p(n,L)$ be the probability that the new order is an even permutation of the starting order, when there are $n$ boats in the division and $L$ is the course length.


For example, with $n=3$ and $L=160$, labelling the boats as $A$,$B$,$C$ in starting order with $C$ highest, the different possible outcomes of the race are as follows:


Therefore, $p(3,160) = 4/15 + 4/27 = 56/135$.


You are also given that $p(4,400)=0.5107843137$, rounded to 10 digits after the decimal point.


Find $p(13,1800)$ rounded to 10 digits after the decimal point.

""" 


class Test(unittest.TestCase):
    def test(self):
        pass
