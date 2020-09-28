#!/usr/bin/env python3
"""
test.py
=======

Beinhaltet Test-Fälle.
"""


class SimpleTest(unittest.TestCase):

    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_one_is_not_two(self):
        self.assertEqual(2, 2)


if __name__ == "__main__":
    unittest.main()
