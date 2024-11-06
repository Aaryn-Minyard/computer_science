import unittest
from step_counter import feet_to_steps

class TestStepCounter(unittest.TestCase):
    
    def test_feet_to_steps(self):
        self.assertEqual(feet_to_steps(0), 0)
        self.assertEqual(feet_to_steps(2.5), 1)
        self.assertEqual(feet_to_steps(5), 2)
        self.assertEqual(feet_to_steps(10), 4)
        self.assertEqual(feet_to_steps(12.5), 5)
        self.assertEqual(feet_to_steps(25), 10)
        self.assertEqual(feet_to_steps(100), 40)
        
    def test_feet_to_steps_with_floats(self):
        self.assertEqual(feet_to_steps(2.4), 0)
        self.assertEqual(feet_to_steps(2.6), 1)
        self.assertEqual(feet_to_steps(7.5), 3)
        self.assertEqual(feet_to_steps(9.9), 3)
        self.assertEqual(feet_to_steps(10.1), 4)

if __name__ == '__main__':
    unittest.main()