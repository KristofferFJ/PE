import unittest

# Power digit sum
from library.common import Common

""" 
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
""" 


class Test(unittest.TestCase):
    def test(self):
        print(Common.sum_of_digits(2**1000))
