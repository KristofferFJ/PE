# MULTIPLES AF 3 og 5
import unittest

n = 3
m = 5
num = 100
s = 0


class Test(unittest.TestCase):
    def test(self):
        s = 0
        for i in range(1, num):
            if n * i % m and n * i < num:
                s += n * i
            if m * i < num:
                s += m * i
        print(s)
