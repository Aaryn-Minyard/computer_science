import time
import matplotlib.pyplot as plt
import mplcursors

# Sample Dinosaur class and data
class Dinosaur:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"{self.name} ({self.weight} tons)"

sample_dinosaurs = [
    Dinosaur("Tyrannosaurus", 8),
    Dinosaur("Parasaurolophus", 2.5),
    Dinosaur("Stegosaurus", 3.1),
    Dinosaur("Triceratops", 6),
    Dinosaur("Brachiosaurus", 50),
    Dinosaur("Ankylosaurus", 6),
    Dinosaur("Spinosaurus", 7),
    Dinosaur("Allosaurus", 2.2),
    Dinosaur("Iguanodon", 3.5),
]

# Sorting Algorithms
def bubble_sort(dinos):
    dinos = dinos.copy()
    n = len(dinos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dinos[j].weight > dinos[j + 1].weight:
                dinos[j], dinos[j + 1] = dinos[j + 1], dinos[j]
    return dinos

def selection_sort(dinos):
    dinos = dinos.copy()
    n = len(dinos)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if dinos[j].weight < dinos[min_idx].weight:
                min_idx = j
        dinos[i], dinos[min_idx] = dinos[min_idx], dinos[i]
    return dinos

# Time and sort
def time_sort(sort_func, dinos):
    start = time.perf_counter()
    sorted_dinos = sort_func(dinos)
    duration = time.perf_counter() - start
    return sorted_dinos, duration

# Graph plotting
def plot_dinosaurs(dinos, title):
    weights = [d.weight for d in dinos]
    labels = [d.name for d in dinos]
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(dinos)), weights)

    ax.set_title(title)
    ax.set_xlabel("Dinosaurs")
    ax.set_ylabel("Weight (kg)")
    ax.set_xticks(range(len(dinos)))
    ax.set_xticklabels([""] * len(dinos))  # Hide labels for clarity

    # Hover interaction
    cursor = mplcursors.cursor(bars, hover=True)
    @cursor.connect("add")
    def on_hover(sel):
        idx = sel.index
        sel.annotation.set_text(f"{labels[idx]}\n{weights[idx]} kg")

    plt.show()

# Compare and visualize
bubble_sorted, bubble_time = time_sort(bubble_sort, sample_dinosaurs)
selection_sorted, selection_time = time_sort(selection_sort, sample_dinosaurs)

print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Selection Sort Time: {selection_time:.6f} seconds")

plot_dinosaurs(bubble_sorted, "Bubble Sort - Dinosaurs by Weight")
plot_dinosaurs(selection_sorted, "Selection Sort - Dinosaurs by Weight")
