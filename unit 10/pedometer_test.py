import unittest
from pedometer import StepConverter

class TestStepConverter(unittest.TestCase):

    def test_default_stride_length(self):
        converter = StepConverter()
        self.assertEqual(converter.stride_length, 2.5)

    def test_custom_stride_length(self):
        converter = StepConverter(3.0)
        self.assertEqual(converter.stride_length, 3.0)

    def test_invalid_stride_length(self):
        with self.assertRaises(ValueError):
            StepConverter(0)
        with self.assertRaises(ValueError):
            StepConverter(-1)

    def test_feet_to_steps(self):
        converter = StepConverter()
        self.assertAlmostEqual(converter.feet_to_steps(150), 60.0)
        self.assertAlmostEqual(converter.feet_to_steps(0), 0.0)

    def test_feet_to_steps_custom_stride(self):
        converter = StepConverter(3.0)
        self.assertAlmostEqual(converter.feet_to_steps(150), 50.0)

    def test_negative_feet(self):
        converter = StepConverter()
        with self.assertRaises(ValueError):
            converter.feet_to_steps(-10)

if __name__ == '__main__':
    unittest.main()