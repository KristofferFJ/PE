import unittest
from typing import List
from sympy import isprime

from library.primes import Primes

"""
Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 2643 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""


def _get_diagonals(n, current_diagonal) -> List[int]:
    side_length = n * 2 - 1
    max_value = side_length ** 2
    current_diagonal.append(max_value - 3 * (side_length - 1))
    current_diagonal.append(max_value - 2 * (side_length - 1))
    current_diagonal.append(max_value - (side_length - 1))
    current_diagonal.append(max_value)
    return current_diagonal


class Test(unittest.TestCase):
    def test_get_diagonals(self):
        assert _get_diagonals(2, [1]) == [1, 3, 5, 7, 9]
        assert _get_diagonals(3, [1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9, 13, 17, 21, 25]
        assert _get_diagonals(4, [1, 3, 5, 7, 9, 13, 17, 21, 25]) == [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]

    def test_find_diagonal_prime_ratio_under_10(self):
        i = 2
        diagonals = 1
        diagonal_primes = 0
        while True:
            diagonals += 4
            diagonal_primes += sum([1 for j in range(1, 4) if isprime((2 * i - 1) ** 2 - (i - 1) * 2 * j)])
            frequency = diagonal_primes / diagonals
            if frequency < 0.1:
                print(str(2 * i - 1))
                break
            i += 1
