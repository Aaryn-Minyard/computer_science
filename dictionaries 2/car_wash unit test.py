import unittest
from unittest.mock import patch
from car_waash import carwash

class TestCarwash(unittest.TestCase):

    @patch('builtins.input', side_effect=['wax,tire shine'])
    @patch('builtins.print')
    def test_valid_services(self, mock_print, mock_input):
        carwash()
        mock_print.assert_any_call("You have selected:", ['wax', 'tire shine'])
        mock_print.assert_any_call("total price: 17")

    @patch('builtins.input', side_effect=['wax, invalid service', 'wax, tire shine'])  # Add a valid retry
    @patch('builtins.print')
    def test_invalid_service(self, mock_print, mock_input):
        carwash()
        mock_print.assert_any_call("Invalid service entered. Please choose from:", "wax, tire shine, underbody wash, mat wash")

    @patch('builtins.input', side_effect=['wax, tire shine, underbody wash', 'wax, tire shine'])  # Add a valid retry
    @patch('builtins.print')
    def test_too_many_services(self, mock_print, mock_input):
        carwash()
        mock_print.assert_any_call("Please select only two additional services.")

    @patch('builtins.input', side_effect=['none'])
    @patch('builtins.print')
    def test_no_additional_services(self, mock_print, mock_input):
        carwash()
        mock_print.assert_any_call("No additional services selected.")
        mock_print.assert_any_call("You have selected:", [])
        mock_print.assert_any_call("total price: 10")

if __name__ == '__main__':
    unittest.main()
