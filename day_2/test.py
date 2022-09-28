import main
import unittest


class TestChar(unittest.TestCase):
    def test_letters(self):
        self.assertEqual(main.count_letters("4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"), 13)
    
    def test_digits(self):
        self.assertEqual(main.count_digits("4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^"), 7)

    def test_custom(self):
        self.assertEqual(main.count_custom("4$$E&95KPfjT$%TJ7#6T2%tcnS#3$^", "^"), 1)

if __name__ == "__main__":
    unittest.main()
