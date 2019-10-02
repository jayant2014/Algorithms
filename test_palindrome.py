import palindrome
import unittest

class TestPalindrome(unittest.TestCase):

    def test_palindrome_1(self):
        self.assertEqual(palindrome.is_palindrome("a"), True)

    def test_palindrome_2(self):
        self.assertEqual(palindrome.is_palindrome("ab"), False)

    def test_palindrome_3(self):
        self.assertEqual(palindrome.is_palindrome("aba"), True)

    def test_palindrome_4(self):
        self.assertEqual(palindrome.is_palindrome("abb"), False)

    def test_palindrome_5(self):
        self.assertEqual(palindrome.is_palindrome("abba"), True)

    def test_palindrome_6(self):
        self.assertEqual(palindrome.is_palindrome("abcdcba"), True)

    def test_palindrome_7(self):
        self.assertEqual(palindrome.is_palindrome("abcdefghhgfedcba"), True)

    def test_palindrome_8(self):
        self.assertEqual(palindrome.is_palindrome("abcdefghihgfedcba"), True)

    def test_palindrome_9(self):
        self.assertEqual(palindrome.is_palindrome("abcdefghihgfeddcba"), False)

    def test_palindrome_10(self):
        self.assertEqual(palindrome.is_palindrome("abc12321cba"), True)

if __name__ == "__main__":
    unittest.main()
