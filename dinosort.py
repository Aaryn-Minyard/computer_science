import time
import matplotlib.pyplot as plt
import mplcursors

# ─── Dinosaur class & data ────────────────────────────────────────────────────
class Dinosaur:
    def __init__(self, name, weight_tons):
        self.name = name
        self.weight = weight_tons
    def __repr__(self):
        return f"{self.name} ({self.weight} tons)"

sample_dinosaurs = [
    Dinosaur("Tyrannosaurus rex",      8.4),
    Dinosaur("Spinosaurus aegyptiacus",10.2),
    Dinosaur("Giganotosaurus carolinii",8.0),
    Dinosaur("Carcharodontosaurus saharicus",7.5),
    Dinosaur("Therizinosaurus cheloniformis",6.2),
    Dinosaur("Tarbosaurus bataar",     6.0),
    Dinosaur("Epanterias amplexus",     4.5),
    Dinosaur("Mapusaurus roseae",       4.8),
    Dinosaur("Edmarka rex",             4.0),
    Dinosaur("Suchomimus tenerensis",    3.9),
    Dinosaur("Shantungosaurus giganteus",16.0),
    Dinosaur("Triceratops horridus",   12.0),
    Dinosaur("Eotriceratops xerinsularis",12.0),
    Dinosaur("Stegosaurus stenops",     6.0),
    Dinosaur("Ankylosaurus magniventris",6.0),
    Dinosaur("Iguanodon bernissartensis",3.5),
    Dinosaur("Parasaurolophus walkeri", 2.5),
    Dinosaur("Allosaurus fragilis",     2.2),
]

# ─── Sorting implementations ──────────────────────────────────────────────────
def bubble_sort(dinos):
    a = dinos.copy()
    n = len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j].weight > a[j+1].weight:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(dinos):
    a = dinos.copy()
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if a[j].weight < a[min_i].weight:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a

def quick_sort(dinos):
    if len(dinos) <= 1:
        return dinos.copy()
    pivot = dinos[len(dinos)//2].weight
    left  = [d for d in dinos if d.weight <  pivot]
    mid   = [d for d in dinos if d.weight == pivot]
    right = [d for d in dinos if d.weight >  pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(dinos):
    if len(dinos) <= 1:
        return dinos.copy()
    mid = len(dinos)//2
    left = merge_sort(dinos[:mid])
    right= merge_sort(dinos[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].weight <= right[j].weight:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:] or right[j:])
    return merged

# ─── Timing helper ───────────────────────────────────────────────────────────
def time_sort(func, dinos):
    start = time.perf_counter()
    sorted_list = func(dinos)
    elapsed = time.perf_counter() - start
    return sorted_list, elapsed

# ─── Run all sorts ───────────────────────────────────────────────────────────
algos = {
    "Bubble Sort":    bubble_sort,
    "Selection Sort": selection_sort,
    "Quick Sort":     quick_sort,
    "Merge Sort":     merge_sort,
}

results = {}
for name, fn in algos.items():
    sorted_dinos, t = time_sort(fn, sample_dinosaurs)
    results[name] = (sorted_dinos, t)

# ─── Plotting ────────────────────────────────────────────────────────────────
colors = ["#6b8e23", "#8b4513"]  # olive‐green & saddle‐brown
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for idx, (name, (sorted_dinos, t)) in enumerate(results.items()):
    ax = axes[idx]
    weights = [d.weight for d in sorted_dinos]
    bars = ax.bar(range(len(weights)), weights,
                  color=colors[idx % len(colors)])
    ax.set_title(f"{name}  (t = {t:.6f}s)")
    ax.set_ylabel("Weight (tons)")
    ax.set_xticks([])
    # interactive hover
    cursor = mplcursors.cursor(bars, hover=True)
    @cursor.connect("add")
    def _(sel):
        d = sorted_dinos[sel.index]
        sel.annotation.set_text(f"{d.name}\n{d.weight} tons")

plt.tight_layout()
plt.show()
