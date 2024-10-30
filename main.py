import unittest
from unittest.mock import patch
from palindrome import get_user_input, is_palindrome

class TestPalindrome(unittest.TestCase):

    @patch('builtins.input', side_effect=['racecar', 'hello', 'madam', 'world', 'level', 'stop', 'quit'])
    @patch('builtins.print')
    def test_get_user_input(self, mock_print, mock_input):
        get_user_input(is_palindrome)
        print("get_user_input function called")
        
        expected_calls = [
            unittest.mock.call('palindrome: racecar'),
            unittest.mock.call('not a palindrome: hello'),
            unittest.mock.call('palindrome: madam'),
            unittest.mock.call('not a palindrome: world'),
            unittest.mock.call('palindrome: level'),
            unittest.mock.call('not a palindrome: stop'),
            unittest.mock.call('Exiting...')
        ]
        
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()
    TestPalindrome(unittest.TestCase)
    
