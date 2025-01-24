def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    """Return the Fibonacci sequence up to the nth number."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Unit tests for the Fibonacci function
import unittest

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0, "Fibonacci(0) should be 0")
        self.assertEqual(fibonacci(1), 1, "Fibonacci(1) should be 1")

    def test_recursive_cases(self):
        self.assertEqual(fibonacci(2), 1, "Fibonacci(2) should be 1")
        self.assertEqual(fibonacci(3), 2, "Fibonacci(3) should be 2")
        self.assertEqual(fibonacci(4), 3, "Fibonacci(4) should be 3")
        self.assertEqual(fibonacci(5), 5, "Fibonacci(5) should be 5")
        self.assertEqual(fibonacci(10), 55, "Fibonacci(10) should be 55")

    def test_large_numbers(self):
        self.assertEqual(fibonacci(20), 6765, "Fibonacci(20) should be 6765")
        self.assertEqual(fibonacci(30), 832040, "Fibonacci(30) should be 832040")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == "__main__":
    user_input = int(input("Put your Number in:"))  # Replace this with user input if needed
    if user_input > 40:
        print(fibonacci(user_input))
    else:
        print(fibonacci_sequence(user_input))
    unittest.main()