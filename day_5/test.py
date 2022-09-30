import main
import unittest


class TestValidCard(unittest.TestCase):

    def test_valid_cards(self):
        message = "Is not a valid card number"
        unittest.TestCase.assertTrue(
            main.is_valid_card("5387 0772 9033 3855"),
            message
        )

        unittest.TestCase.assertTrue(
            main.is_valid_card("4282 2935 3025 2693"),
            message
        )

        unittest.TestCase.assertTrue(
            main.is_valid_card("4888 3785 5051 4326"),
            message
        )

        unittest.TestCase.assertTrue(
            not main.is_valid_card("5387 0772 9033"),
            message
        )

        unittest.TestCase.assertTrue(
            not main.is_valid_card("4282 2935 3025 2692"),
            message
        )

        unittest.TestCase.assertTrue(
            not main.is_valid_card("4888 3785 5051 4322"),
            message
        )

    def test_luhn(self):
        pass


if __name__ == "__main__":
    unittest.main()
