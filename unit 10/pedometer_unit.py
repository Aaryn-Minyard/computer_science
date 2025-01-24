import unittest
from pedometer import StepConverter

class TestStepConverter(unittest.TestCase):
    def setUp(self):
        """
        Set up the StepConverter for testing. A new hero arises before each test.
        """
        self.converter = StepConverter()

    def test_feet_to_steps_standard(self):
        """
        Test the standard feet-to-steps conversion.
        """
        self.assertAlmostEqual(self.converter.feet_to_steps(150), 60.0)

    def test_feet_to_steps_zero(self):
        """
        Test converting zero feet to steps. Heroic patience for standing still!
        """
        self.assertEqual(self.converter.feet_to_steps(0), 0)

    def test_negative_feet(self):
        """
        Test that negative feet raise a valiant ValueError.
        """
        with self.assertRaises(ValueError):
            self.converter.feet_to_steps(-50)

    def test_custom_stride_length(self):
        """
        Test using a custom stride length in the noble journey.
        """
        custom_converter = StepConverter(stride_length=3.0)
        self.assertAlmostEqual(custom_converter.feet_to_steps(150), 50.0)

    def test_invalid_stride_length(self):
        """
        Test that an invalid stride length raises a righteous ValueError.
        """
        with self.assertRaises(ValueError):
            StepConverter(stride_length=0)

if __name__ == "__main__":
    unittest.main()