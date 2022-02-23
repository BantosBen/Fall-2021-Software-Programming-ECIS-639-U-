import unittest
from ex_1_0 import in_range


class TestInRange(unittest.TestCase):
    def test_in_range_1(self):
        self.assertEqual(in_range(30, 15, 40), True)

    def test_not_in_range(self):
        self.assertEqual(in_range(50, 74, 33), False)

    def test_in_range(self):
        self.assertEqual(in_range(1287, 1178, 4563), True)

    if __name__ == "__main__":
        unittest.main()
