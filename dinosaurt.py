import random
import time
import matplotlib.pyplot as plt

# Dinosaur list 🦕
dinosaurs = [
    "Tyrannosaurus", "Velociraptor", "Stegosaurus",
    "Triceratops", "Brachiosaurus", "Allosaurus",
    "Spinosaurus", "Ankylosaurus", "Dilophosaurus", "Pachycephalosaurus"
]

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogosort(arr):
    tries = 0
    start = time.time()
    while not is_sorted(arr):
        random.shuffle(arr)
        tries += 1
        if tries > 50000:  # Safety break so it doesn’t run forever
            break
    end = time.time()
    return tries, end - start, arr

def modified_bogosort(arr):
    tries = 0
    start = time.time()
    while not is_sorted(arr):
        var1, var2 = random.sample(range(len(arr)), 2)
        arr[var1], arr[var2] = arr[var2], arr[var1]
        tries += 1
        if tries > 50000:
            break
    end = time.time()
    return tries, end - start, arr

def bubble_sort(arr):
    n = len(arr)
    tries = 0
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            tries += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = time.time()
    return tries, end - start, arr


# Shuffle the dinos to start
random.shuffle(dinosaurs)

print("Unsorted dinosaurs:", dinosaurs)

# Run each algorithm
results = {}
results["Bogosort"] = bogosort(dinosaurs.copy())
results["Modified Bogosort"] = modified_bogosort(dinosaurs.copy())
results["Bubble Sort"] = bubble_sort(dinosaurs.copy())

# Print results
for algo, (tries, duration, sorted_list) in results.items():
    print(f"\n{algo}:")
    print(f"  Steps: {tries}, Time: {duration:.4f}s")
    print(f"  Sorted dinos: {sorted_list}")

# Chart results
algorithms = list(results.keys())
tries = [results[a][0] for a in algorithms]
times = [results[a][1] for a in algorithms]

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.bar(algorithms, tries)
plt.title("Steps Taken")
plt.ylabel("Steps")

plt.subplot(1,2,2)
plt.bar(algorithms, times)
plt.title("Execution Time")
plt.ylabel("Seconds")

plt.tight_layout()
plt.show()
