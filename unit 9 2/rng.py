from random import randint

class RandomNumbers:
    def __init__(self):
            self.var1 = 0
            self.var2 = 0
            self.var3 = 0

    def set_random_values(self, low, high):
        self.var1 = randint(low, high)
        self.var2 = randint(low, high)
        self.var3 = randint(low, high)

    def get_random_values(self):
        print(f"Random values: {self.var1} {self.var2} {self.var3}")

    #set_random_values( ) - accepts a low and high integer values as parameters, and sets var1, var2, and var3 to random numbers within the range of the low and high input values (inclusive).
#   get_random_values( ) - prints out the 3 random numbers in the format: "Random values: var1 var2 var3"

    # Type your code here.

if __name__ == "__main__":
    low = int(input("Enter low: "))
    high = int(input("Enter high: "))

    numbers = RandomNumbers()
    numbers.set_random_values(low, high)
    numbers.get_random_values()