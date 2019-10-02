import fibonacci
import unittest

class TestNthFibonacci(unittest.TestCase):
    def test_fib_1(self):
        self.assertEqual(fibonacci.get_nthfib(1), 0)
    
    def test_fib_2(self):
        self.assertEqual(fibonacci.get_nthfib(2), 1)

    def test_fib_3(self):
        self.assertEqual(fibonacci.get_nthfib(3), 1)

    def test_fib_4(self):
        self.assertEqual(fibonacci.get_nthfib(4), 2)

    def test_fib_5(self):
        self.assertEqual(fibonacci.get_nthfib(5), 3)

    def test_fib_10(self):
        self.assertEqual(fibonacci.get_nthfib(10), 34)

if __name__ == "__main__":
    unittest.main()
