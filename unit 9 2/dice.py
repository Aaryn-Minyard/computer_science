import random
import time

class GVDie:  
   def __init__(self):      
      # set default values
      self.my_value = random.randint(1, 6)
      self.rand = random.Random()

   def roll(self):
       self.my_value = self.rand.randint(1, 6)  
      
   # set the random number generator seed for testing
   def set_seed(self, seed):
       self.rand.seed(seed)
   
   # allows dice to be compared if necessary
   def compare_to(self, other):
       return self.my_value - other.my_value

def roll_total(die, total):
    rolls = 0
    sum = 0
    while sum < total:
        die.roll()
        sum += die.my_value
        rolls += 1
    return rolls

if __name__ == "__main__":
    seed = seed = random.seed(time.time())
    die = GVDie()   # Create a GVDie object
    die.set_seed(seed)   # Set the GVDie object with seed value 15
          
    total = int(input("Enter the target total: "))  # Ask for user input
    rolls = roll_total(die, total)  # Get the number of rolls to reach the total
    print(f'Number of rolls to reach at least {total}: {rolls}')
