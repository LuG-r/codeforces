import unittest

class TestResults(unittest.TestCase):
    def setUp(self) -> None:
        from a_morning import minimum_seconds_required
        self.minimum_seconds_required = minimum_seconds_required
        return super().setUp()
    
    def test_provided(self):
        self.assertEqual(self.minimum_seconds_required([1, 1, 1, 1]), 4)
        self.assertEqual(self.minimum_seconds_required([1, 2, 3, 6]), 9)
        self.assertEqual(self.minimum_seconds_required([1, 0, 1, 0]), 31)
        self.assertEqual(self.minimum_seconds_required([1, 9, 2, 0]), 27)
        self.assertEqual(self.minimum_seconds_required([9, 2, 7, 3]), 28)
        self.assertEqual(self.minimum_seconds_required([0, 0, 0, 0]), 13)
        self.assertEqual(self.minimum_seconds_required([7, 4, 9, 2]), 25)
        self.assertEqual(self.minimum_seconds_required([8, 5, 4, 3]), 16)
        self.assertEqual(self.minimum_seconds_required([0, 2, 9, 4]), 33)
        self.assertEqual(self.minimum_seconds_required([8, 3, 6, 1]), 24)

if __name__ == '__main__':
    unittest.main()
