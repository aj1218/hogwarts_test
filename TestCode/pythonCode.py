import sys

print("路劲为:", sys.path)
sys.path.append(r"D:\pythonProject\hogwarts_test")
from Testcase.testcode import Dome1
import unittest


class TestDome(unittest.TestCase):
    def test_dome(self):
        self.dome = Dome1()
        result = self.dome.add(1, 2)
        print(result)
        self.assertEqual(3, result)

    def test_11(self):
        self.dome = Dome1()
        result = self.dome.add(1, 2)
        print(result)
        self.assertEqual(3, result)

    def test_22(self):
        self.dome = Dome1()
        result = self.dome.add(1, 2)
        print(result)
        self.assertEqual(3, result)

    def case_a(self):
        print("qwdewdedededed")


if __name__ == '__main__':
    unittest.main()
