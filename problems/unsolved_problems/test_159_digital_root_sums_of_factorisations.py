import unittest

"""
Digital root sums of factorisations

A composite number can be factored many different ways.  
For instance, not including multiplication by one, 24 can be factored in 7 distinct ways:
Recall that the digital root of a number, in base 10, is found by adding together the digits of that number, 
and repeating that process until a number is arrived at that is less than 10.  
Thus the digital root of 467 is 8.
We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.
 The chart below demonstrates all of the DRS values for 24.
The maximum Digital Root Sum  of 24 is 11.
The function mdrs(n) gives the maximum Digital Root Sum of n. So  mdrs(24)=11.
Find ∑ mdrs(n) for 1 < n < 1,000,000.
"""


class Test(unittest.TestCase):
    def test(self):
        pass
