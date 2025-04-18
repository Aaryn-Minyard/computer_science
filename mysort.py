import time
import matplotlib.pyplot as plt
import mplcursors

# ─── Dinosaur (or Generic) Item class ─────────────────────────────────────────
class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name} ({self.value})"

# ─── Helpers to get user data and colors ───────────────────────────────────────
def get_user_items():
    print("Enter items to sort. When done, leave name blank and press Enter.")
    items = []
    while True:
        name = input("  Name: ").strip()
        if not name:
            break
        try:
            val = float(input("  Value: ").strip())
        except ValueError:
            print("    ⚠️  Please enter a numeric value.")
            continue
        items.append(Item(name, val))
    if not items:
        print("No items entered, using default sample data.")
        return [
            Item("Tyrannosaurus rex",      8.4),
            Item("Spinosaurus aegyptiacus",10.2),
            Item("Giganotosaurus carolinii",8.0),
            Item("Carcharodontosaurus saharicus",7.5),
        ]
    return items

def get_colors():
    print("\nChoose two colors for the bars (e.g. 'green', '#8B4513', 'olive').")
    c1 = input("  First color: ").strip() or "green"
    c2 = input("  Second color: ").strip() or "brown"
    return [c1, c2]

# ─── Four Sorting Algorithms ─────────────────────────────────────────────────
def bubble_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j].value > a[j+1].value:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if a[j].value < a[min_i].value:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a

def quick_sort(a):
    if len(a) <= 1:
        return a.copy()
    pivot = a[len(a)//2].value
    left  = [x for x in a if x.value <  pivot]
    mid   = [x for x in a if x.value == pivot]
    right = [x for x in a if x.value >  pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(a):
    if len(a) <= 1:
        return a.copy()
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right= merge_sort(a[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].value <= right[j].value:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:] or right[j:])
    return merged

# ─── Timing wrapper ──────────────────────────────────────────────────────────
def time_sort(fn, data):
    start = time.perf_counter()
    sorted_list = fn(data)
    elapsed = time.perf_counter() - start
    return sorted_list, elapsed

# ─── Main routine ────────────────────────────────────────────────────────────
def main():
    # 1) Gather user items & colors
    items = get_user_items()
    colors = get_colors()

    # 2) Run all sorts
    algos = {
        "Bubble Sort":    bubble_sort,
        "Selection Sort": selection_sort,
        "Quick Sort":     quick_sort,
        "Merge Sort":     merge_sort,
    }
    results = {}
    for name, fn in algos.items():
        sorted_items, t = time_sort(fn, items)
        results[name] = (sorted_items, t)

    # 3) Plot in 2×2 panel
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()
    for idx, (name, (sorted_items, t)) in enumerate(results.items()):
        ax = axes[idx]
        values = [it.value for it in sorted_items]
        bars = ax.bar(range(len(values)), values,
                      color=colors[idx % len(colors)])
        ax.set_title(f"{name}  (t = {t:.6f}s)")
        ax.set_ylabel("Value")
        ax.set_xticks([])
        # hover tooltip
        cursor = mplcursors.cursor(bars, hover=True)
        @cursor.connect("add")
        def on_hover(sel):
            it = sorted_items[sel.index]
            sel.annotation.set_text(f"{it.name}\n{it.value}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
