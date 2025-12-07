import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-32), 32, "Should be equal")

    def test_abs2(self):
        self.assertEqual(abs(-34), 32, "Should be equal")

if __name__ == "__main__":
    unittest.main()
        