# nutrition.py

class FoodItem:
    def __init__(self, name="Water", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, servings):
        """
        Returns the total calories for the given number of servings.
        The formula used is:
            calories per serving = (fat * 9) + (carbs * 4) + (protein * 4) + 2
        """
        per_serving = (self.fat * 9) + (self.carbs * 4) + (self.protein * 4) + 2
        return per_serving * servings

    def print_info(self):
        """
        Prints the nutritional information per serving.
        """
        # Use the same calculation as in get_calories for one serving.
        calories = (self.fat * 9) + (self.carbs * 4) + (self.protein * 4) + 2
        print(f"Nutritional information per serving of {self.name}:")
        print(f"    Fat: {self.fat} g")
        print(f"    Carbohydrates: {self.carbs} g")
        print(f"    Protein: {self.protein} g")
        print(f"    Total calories: {calories}")


if __name__ == '__main__':
    # Default food item
    food1 = FoodItem()
    food1.print_info()

    # Custom food item (interactive)
    name = input("Enter food item name: ")
    fat = float(input("Enter fat content (in grams): "))
    carbs = float(input("Enter carbohydrate content (in grams): "))
    protein = float(input("Enter protein content (in grams): "))
    food2 = FoodItem(name, fat, carbs, protein)
    food2.print_info()
