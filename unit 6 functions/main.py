import unittest

def kilo_to_pounds(kilos):
    # This statement intentionally has an error.
    return (kilos / 2.204)

# Main part of the program starts here. Do not remove the line below.
if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')


# Unit tests
class TestKiloToPounds(unittest.TestCase):

    def test_zero(self):
        self.assertAlmostEqual(kilo_to_pounds(0), 0.0)

    def test_ten(self):
        self.assertAlmostEqual(kilo_to_pounds(10), 22.040)

    def test_small_value(self):
        self.assertAlmostEqual(kilo_to_pounds(1), 2.204)

    def test_large_value(self):
        self.assertAlmostEqual(kilo_to_pounds(100), 220.400)

if __name__ == '__main__':
    # Run the unit tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
