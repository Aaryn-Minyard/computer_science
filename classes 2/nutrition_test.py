import unittest
from unittest.mock import patch
from nutrition import FoodItem
import io

class TestFoodItem(unittest.TestCase):

    def test_default_initialization(self):
        food_item = FoodItem()
        self.assertEqual(food_item.name, 'Water')
        self.assertEqual(food_item.fat, 0.0)
        self.assertEqual(food_item.carbs, 0.0)
        self.assertEqual(food_item.protein, 0.0)

    def test_custom_initialization(self):
        food_item = FoodItem('Apple', 0.2, 25.0, 0.5)
        self.assertEqual(food_item.name, 'Apple')
        self.assertEqual(food_item.fat, 0.2)
        self.assertEqual(food_item.carbs, 25.0)
        self.assertEqual(food_item.protein, 0.5)

    def test_get_calories(self):
        food_item = FoodItem('Apple', 0.2, 25.0, 0.5)
        self.assertAlmostEqual(food_item.get_calories(1), 105.8)
        self.assertAlmostEqual(food_item.get_calories(2), 211.6)

    def test_print_info(self):
        food_item = FoodItem('Apple', 0.2, 25.0, 0.5)
        expected_output = (
            'Nutritional information per serving of Apple:\n'
            '    Fat: 0.2 g\n'
            '    Carbohydrates: 25.0 g\n'
            '    Protein: 0.5 g\n'
            '    Total calories: 105.8\n'
        )
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            food_item.print_info()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()