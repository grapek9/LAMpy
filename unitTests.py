import unittest
from LAM import *
#print("Unit Testing class for LAMpy lib")


class TestArrayFunctions(unittest.TestCase):

    def test_firstShouldPass(self):
        self.assertEqual(first([0, 1, 2, 3]), 0)
        self.assertEqual(first("abc"), "a")
        self.assertEqual(first([0, 1, 2, 3, 4], 10), [0, 1, 2, 3, 4])

    def test_initialShouldPass(self):
        self.assertEqual(initial([0]), 0)
        self.assertEqual(initial([0, 1]), [0])
        self.assertEqual(initial([0, 1, 2, 3]), [0, 1, 2])
        self.assertEqual(initial([0, 1, 2, 3], 2), [0, 1])
        self.assertEqual(initial([0, 1, 2, 3], 10), None)
        self.assertEqual(initial([0, 1, 2, 3], 4), None)
        self.assertEqual(initial("abc"), ["a", "b"])
        self.assertEqual(initial("abc", 3), None)

    def test_restShouldPass(self):
        self.assertEqual(rest([5, 4, 3, 2, 1]), [5, 4, 3, 2, 1])
        self.assertEqual(rest([5, 4, 3, 2, 1], 1), [4, 3, 2, 1])
        self.assertEqual(rest("abc", 1), ["b", "c"])
        self.assertEqual(rest("abc", 5), None)

    def test_compactShouldPass(self):
        self.assertEqual(compact([0, None, 1]), 1)
        self.assertEqual(compact([0, None, 1, 2, 3]), [1, 2, 3])
        self.assertEqual(compact([0, None, 1], [0, 1]), None)

    def test_withoutShouldPass(self):
        self.assertEqual(without([0, 1, 2, 3, 4, 5], 0, 2, 5), [1, 3, 4])
        self.assertEqual(without([0, 1, 2, 3, 4, 5], 4, 0, 3, 2, 1, 5), None)


if __name__ == '__main__':
    unittest.main()
