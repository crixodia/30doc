import unittest
import main


class TestAcronim(unittest.TestCase):
    def test_acronimo(self):
        unittest.TestCase.assertTrue(
            main.acronimo("Infrastructure as a service") == "IaaS", "IaaS"
        )
        unittest.TestCase.assertTrue(
            main.acronimo("One-Time Password as a service") == "OTPaaS", "OTPaaS"
        )
        unittest.TestCase.assertTrue(
            main.acronimo("Liquid-crystal display") == "LCD", "LCD"
        )


if __name__ == "__main__":
    unittest.main()
