import random
import time
import matplotlib.pyplot as plt

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogosort(arr):
    tries = 0
    start = time.time()
    while not is_sorted(arr):
        random.shuffle(arr)
        tries += 1
        if tries % 1000 == 0:
            print(f"😵 Still shuffling... ({tries} tries)")
    end = time.time()
    return tries, end - start

def modified_bogosort(arr):
    tries = 0
    start = time.time()
    while not is_sorted(arr):
        var1, var2 = random.sample(range(len(arr)), 2)
        arr[var1], arr[var2] = arr[var2], arr[var1]
        tries += 1
        if tries % 100000 == 0:
            print(f"🤯 Swapping madness... {tries} swaps so far")
    end = time.time()
    return tries, end - start

def bubble_sort(arr):
    n = len(arr)
    tries = 0
    start = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            tries += 1
            print(f"⚔️ Comparing {arr[j]} vs {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"🔄 Swapping {arr[j]} <-> {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = time.time()
    print(f"🏆 Bubble sort finished in {tries} comparisons ({end - start:.4f} seconds)")
    return tries, end - start


# Example arrays (use same input for fairness)
arr = [3, 2, 5, 1, 4, 7, 6, 9, 8, 10]

# Run all algorithms
results = {}
results["Bogosort"] = bogosort(arr.copy())
results["Modified Bogosort"] = modified_bogosort(arr.copy())
results["Bubble Sort"] = bubble_sort(arr.copy())

# Print results
for algo, (tries, duration) in results.items():
    print(f"{algo}: {tries} steps in {duration:.4f} sec")

# Plot results
algorithms = list(results.keys())
tries = [results[a][0] for a in algorithms]
times = [results[a][1] for a in algorithms]

plt.figure(figsize=(10,5))

# Left chart: number of tries
plt.subplot(1,2,1)
plt.bar(algorithms, tries)
plt.title("Number of Steps/Tries")
plt.ylabel("Steps")

# Right chart: execution time
plt.subplot(1,2,2)
plt.bar(algorithms, times)
plt.title("Execution Time (seconds)")
plt.ylabel("Seconds")

plt.tight_layout()
plt.show()
