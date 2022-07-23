import unittest

# Quadtree encoding (a simple compression algorithm)
"""
The quadtree encoding allows us to describe a 2N×2N  black and white image as a sequence of bits (0 and 1). Those sequences are to be read from left to right like this:

Consider the following 4×4 image (colored marks denote places where a split can occur):
This image can be described by several sequences, for example :
"001010101001011111011010101010", of length 30, or
"0100101111101110", of length 16, which is the minimal sequence for this image.
For a positive integer N, define DN as the 2N×2N image with the following coloring scheme:

What is the length of the minimal sequence describing D24 ?
"""


class Test(unittest.TestCase):
    def test(self):
        pass
