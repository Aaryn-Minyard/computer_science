import time
import random

def time_func():

    random.seed(time.time())
        
    numbers = [random.randint(-1000, 1000) for _ in range(10)]
    numbers.sort()
    negatives = [num for num in numbers if num < 0]
    return numbers, negatives
    
    
#sorted_list, negative_list = time_func()
#print(f"Sorted list: {sorted_list}")
#print(f"Negative numbers: {negative_list}")



import time
import random

def time_func():
    timeList = []
    
    for i in range(10):
        random_time = random.randint(-1000, 1000)  # Generate a random number between -1000 and 1000
        timeList.append(random_time)
    
    timeList.sort()
    negatives = [num for num in timeList if num < 0]
    return timeList, negatives
    

sorted_list, negative_list = time_func()
print(f"Sorted list: {sorted_list}")
print(f"Negative numbers: {negative_list}")