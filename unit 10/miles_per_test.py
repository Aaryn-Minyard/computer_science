import unittest
from miles_per_project import driving_cost
from io import StringIO
import sys

class TestDrivingCost(unittest.TestCase):

    def test_driving_cost_10_miles(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        driving_cost(20, 3.1599, 10)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Your trip will cost you $1.58.")

    def test_driving_cost_50_miles(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        driving_cost(20, 3.1599, 50)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Your trip will cost you $7.90.")

    def test_driving_cost_400_miles(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        driving_cost(20, 3.1599, 400)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Your trip will cost you $63.20.")

if __name__ == '__main__':
    unittest.main()