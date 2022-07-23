import unittest

# Randomly Decaying Sequence
""" 
Given a fixed real number $c$, define a random sequence $(X_n)_{n\ge 0}$ by the following random process:
If we desire there to be precisely a 25% probability that $X_{100}<1$, then this can be arranged by fixing $c$ such that $\log_{10} c \approx 46.27$.
Suppose now that $c$ is set to a different value, so that there is precisely a 25% probability that $X_{10\,000\,000}<1$.
Find $\log_{10} c$ and give your answer rounded to two places after the decimal point.
""" 


class Test(unittest.TestCase):
    def test(self):
        pass
