import main
import unittest


class TestFib(unittest.TestCase):
    def test_fib_mem(self):
        self.assertEqual(main.fib_memo(1), [1])
        self.assertEqual(main.fib_memo(2), [1, 1])
        self.assertEqual(main.fib_memo(3), [1, 1, 2])
        self.assertEqual(main.fib_memo(4), [1, 1, 2, 3])
        self.assertEqual(main.fib_memo(5), [1, 1, 2, 3, 5])
        self.assertEqual(main.fib_memo(6), [1, 1, 2, 3, 5, 8])
        self.assertEqual(main.fib_memo(7), [1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(main.fib_memo(8), [1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(main.fib_memo(9), [1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(main.fib_memo(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_nth_fib(self):
        self.assertEqual(main.nth_fib(1), 1)
        self.assertEqual(main.nth_fib(2), 1)
        self.assertEqual(main.nth_fib(3), 2)
        self.assertEqual(main.nth_fib(4), 3)
        self.assertEqual(main.nth_fib(5), 5)
        self.assertEqual(main.nth_fib(6), 8)
        self.assertEqual(main.nth_fib(7), 13)
        self.assertEqual(main.nth_fib(8), 21)
        self.assertEqual(main.nth_fib(9), 34)
        self.assertEqual(main.nth_fib(10), 55)

    def test_sum_fib(self):
        self.assertEqual(main.sum_fib(1), 1)
        self.assertEqual(main.sum_fib(2), 2)
        self.assertEqual(main.sum_fib(3), 4)
        self.assertEqual(main.sum_fib(4), 7)
        self.assertEqual(main.sum_fib(5), 12)
        self.assertEqual(main.sum_fib(6), 20)
        self.assertEqual(main.sum_fib(7), 33)
        self.assertEqual(main.sum_fib(8), 54)
        self.assertEqual(main.sum_fib(9), 88)
        self.assertEqual(main.sum_fib(10), 143)


if __name__ == "__main__":
    unittest.main()
