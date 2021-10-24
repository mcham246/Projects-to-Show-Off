import unittest
from solution import longestString

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(3, longestString("abcabcbb"))

    def test2(self):
        self.assertEqual(1,longestString("bbbbb"))

    def test3(self):
        self.assertEqual(3, longestString("pwwkew"))

    def test4(self):
        self.assertEqual(2, longestString("hahaha"))

if __name__ == "__main__":
    unittest.main()
