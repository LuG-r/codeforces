import unittest

class TestResults(unittest.TestCase):
    def setUp(self) -> None:
        from d_inlove import update_multiset, calculate_intersection, multiset
        self.multiset = multiset
        self.update_multiset = update_multiset
        self.calculate_intersection = calculate_intersection
        return super().setUp()
    
    def test_provided(self):
        self.update_multiset("+", 1, 2)
        self.assertEqual(self.calculate_intersection(), "NO")
        self.update_multiset("+", 3, 4)
        self.assertEqual(self.calculate_intersection(), "YES")
        self.update_multiset("+", 2, 3)
        self.assertEqual(self.calculate_intersection(), "YES")
        self.update_multiset("+", 2, 2)
        self.assertEqual(self.calculate_intersection(), "YES")
        self.update_multiset("+", 3, 4)
        self.assertEqual(self.calculate_intersection(), "YES")
        self.update_multiset("-", 3, 4)
        self.assertEqual(self.calculate_intersection(), "YES")
        self.update_multiset("-", 3, 4)
        self.assertEqual(self.calculate_intersection(), "NO")
        self.update_multiset("-", 1, 2)
        self.assertEqual(self.calculate_intersection(), "NO")
        self.update_multiset("+", 3, 4)
        self.assertEqual(self.calculate_intersection(), "YES")
        self.update_multiset("-", 2, 2)
        self.assertEqual(self.calculate_intersection(), "NO")
        self.update_multiset("-", 2, 3)
        self.assertEqual(self.calculate_intersection(), "NO")
        self.update_multiset("-", 3, 4)
        self.assertEqual(self.calculate_intersection(), "NO")
        

if __name__ == '__main__':
    unittest.main()
