import os, sys
import random
import unittest

class TestTandome(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_pass1(self):
        self.assertEqual(10, 7+3)

    def test_pass2(self):
        self.assertNotEqual(10, random.randint(0,9))

    #def test_fail(self):
    #    self.assertEqual(10, 7+4, "this is not equal")


if __name__ == "__main__":
    unittest.main()
