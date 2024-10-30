import unittest
def is_palindrome(s):
    
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def get_user_input(is_palindrome):
    while True:
        user_input = input("Enter a word or phrase (type 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Exiting...")
            break

        if is_palindrome(user_input):
            print(f"palindrome: {user_input}")
        else:
            print(f"not a palindrome: {user_input}")


class TestPalindrome(unittest.TestCase):
    
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
    
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome("Madam"))


    


if __name__ == '__main__':
    get_user_input(is_palindrome)
    unittest.main()
    



