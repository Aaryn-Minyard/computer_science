#Please write a code that sets the random seed as 15 and then prints off the 1st 50 numbers then create another code that also sets the random seed as 15 and prints off the 1st 15 numbers repeat this process three different times using the same random seed of 15 and show that the three different numbers all match
import random

# Initialize three lists to store the random numbers
list1 = []
list2 = []
list3 = []

# Generate the first list of 50 numbers
random.seed(15)
for i in range(50):
    list1.append(random.randint(0, 1000))

# Generate the second list of 15 numbers
random.seed(15)
for i in range(15):
    list2.append(random.randint(0, 1000))

# Generate the third list of 15 numbers
random.seed(15)
for i in range(15):
    list3.append(random.randint(0, 1000))

# Print the lists in parallel
print("List 1 (50 numbers):", list1)
print("List 2 (15 numbers):", list2)
print("List 3 (15 numbers):", list3)