import unittest

class TestResults(unittest.TestCase):
    def setUp(self) -> None:
        from b_chemistry import can_form_palindrome
        self.can_form_palindrome = can_form_palindrome
        return super().setUp()
    
    def test_provided(self):
        self.assertEqual(self.can_form_palindrome("a", 0), "YES")
        self.assertEqual(self.can_form_palindrome("ab", 0), "NO")
        self.assertEqual(self.can_form_palindrome("ba", 1), "YES")
        self.assertEqual(self.can_form_palindrome("abb", 1), "YES")
        self.assertEqual(self.can_form_palindrome("abc", 2), "YES")
        self.assertEqual(self.can_form_palindrome("bacacd", 2), "YES")
        self.assertEqual(self.can_form_palindrome("fagbza", 2), "NO")
        self.assertEqual(self.can_form_palindrome("zwaafa", 2), "NO")
        self.assertEqual(self.can_form_palindrome("taagaak", 2), "YES")
        self.assertEqual(self.can_form_palindrome("ttrraakkttoorr", 3), "YES")
        self.assertEqual(self.can_form_palindrome("debdb", 3), "YES")
        self.assertEqual(self.can_form_palindrome("ecadc", 4), "YES")
        self.assertEqual(self.can_form_palindrome("debca", 3), "NO")
        self.assertEqual(self.can_form_palindrome("abaac", 3), "YES")


if __name__ == '__main__':
    unittest.main()
