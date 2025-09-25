import random
import time
import matplotlib as plt

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogosort(arr):
    print("\n🔥 Starting BOGOSORT (a.k.a pure chaos) 🔥")
    tries = 0
    start = time.time()
    while not is_sorted(arr):
        random.shuffle(arr)
        tries += 1
        if tries % 1000 == 0:
            print(f"😵 Still shuffling... ({tries} tries)")
    end = time.time()
    print(f"🎉 Sorted after {tries} shuffles in {end - start:.4f} seconds!")
    return tries, end - start

def modified_bogosort(arr):
    print("\n🎲 Starting MODIFIED BOGOSORT (random swaps edition) 🎲")
    tries = 0
    start = time.time()
    while not is_sorted(arr):
        var1, var2 = random.sample(range(len(arr)), 2)
        arr[var1], arr[var2] = arr[var2], arr[var1]
        tries += 1
        if tries % 1000 == 0:
            print(f"🤯 Swapping madness... {tries} swaps so far")
    end = time.time()
    print(f"✅ Sorted after {tries} swaps in {end - start:.4f} seconds!")
    return tries, end - start

def bubble_sort(arr):
    print("\n💨 Starting BUBBLE SORT (slow but steady) 💨")
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


# Example arrays
arr = [3, 2, 5, 1, 4, 7, 6, 9, 8, 10]
arr2 = arr.copy()
arr3 = [3, 2, 1, 5, 4]


results = {}
results['bogosort'] = bogosort(arr.copy())
results['modified_bogosort'] = modified_bogosort(arr2.copy())   
results['bubble_sort'] = bubble_sort(arr3.copy())

# Display results
for algo, (tries, duration) in results.items():
    print(f"\n{algo.upper()} took {tries} tries and {duration:.4f} seconds.")

algorithms = list(results.keys())
tries = [results[algo][0] for algo in algorithms]
durations = [results[algo][1] for algo in algorithms]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(algorithms, tries, color=['red', 'orange', 'blue'])
plt.title('Number of Tries/Comparisons')
plt.ylabel('Steps')

plt.subplot(1, 2, 2)
plt.bar(algorithms, durations, color=['red', 'orange', 'blue'])
plt.title('Time Taken (seconds)')
plt.ylabel('Time (s)')

plt.tight_layout()
plt.show()

print("Unsorted array:", arr)
print("Sorted array:", bogosort(arr.copy()))

print("Unsorted array:", arr2)
print("Sorted array (modified):", modified_bogosort(arr2.copy()))

print("Bubble sort result:", bubble_sort(arr3.copy()))
