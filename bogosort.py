import random

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogosort(arr):
    tries = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        tries += 1
    print("Number of tries:", tries)
    return arr

arr = [3, 2, 5, 1, 4]
arr2 = [3, 2, 5, 1, 4]
arr3 = [3, 2, 5, 1, 4, 7, 6, 9, 8, 10, 12, 11, 14, 13, 15]
print("Unsorted array:", arr)
print("Sorted array:", bogosort(arr)) 

def modified_bogosort(arr2):
    tries = 0
    while not is_sorted(arr2):
        var1 = random.randint(0, len(arr2) - 1)
        var2 = random.randint(0, len(arr2) - 1)
        #var1, var2 = random.sample(range(len(arr2)), 2)
        arr2[var1], arr2[var2] = arr2[var2], arr2[var1]
        tries += 1
    print("Number of tries (modified):", tries)
    return arr2

print("Unsorted array:", arr2)
print("Sorted array (modified):", modified_bogosort(arr2))


def bubble_sort(arr3):
    n = len(arr3)
    tries = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            tries += 1
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
    print("Number of comparisons (bubble):", tries)
    return arr3


# Example run

print("Bubble sort result:", bubble_sort(arr3))
print("Unsorted array:", arr3)