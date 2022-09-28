import math
import main
import unittest


class TestGeometria(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(main.distance([-1, 1], [0, 0]), math.sqrt(2))

    def test_opt_dist(self):
        self.assertEqual(main.optimal_order({
            "A": [-1, 1],
            "B": [4, 5],
            "C": [2, 7],
            "D": [-4, 4]
        },
            "D"
        ),
            ["D", "A", "B", "C"]
        )

    def test_opt_time(self):
        self.assertEqual(main.optimal_time({
            "A": 2.30,
            "B": 1.00,
            "C": 2.50,
            "D": 0.45
        }), ["C", "A", "B", "D"])


if __name__ == "__main__":
    unittest.main()
