# 30 - Digit fifth powers
# FUN FACT fra projecteuler.net: Hvis vi kigger på forskellige potenser (under 20) har
# 11 flest løsninger til dette problem.
import unittest


class Test(unittest.TestCase):
    def test_run(self):
        numbers = []
        for i in range(2, 354294):
            num = i
            s = 0
            for j in range(len(str(i))):
                s += (num % 10) ** 5
                num = num // 10
            if s == i:
                numbers.append(i)


if __name__ == '__main__':
    unittest.main()
