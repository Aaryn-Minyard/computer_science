import tkinter as tk
from tkinter import ttk, messagebox
import random
from dinosaur_library import Dinosaur, dinosaur_library
from gamegui import *
from battle_screen import *


def maybe_trigger_battle(dino, parent_window, return_callback):
    if random.random() < 0.25:  # 25% chance to trigger a battle
        opponent = get_random_opponent()

        BattleScreen(parent_window, dino, opponent, return_callback)
        return True
    return False

def get_random_opponent():
    diet = random.choice(list(dinosaur_library.keys()))
    size = random.choice(list(dinosaur_library[diet].keys()))
    name, base_dino = random.choice(list(dinosaur_library[diet][size].items()))

    # Apply a random stat multiplier for variety
    boost = random.uniform(1.05, 1.5)
    boosted_dino = Dinosaur(
        name,
        int(base_dino.max_health * boost),
        int(base_dino.attachment * boost),
        int(base_dino.attack * boost),
        int(base_dino.defense * boost),
        int(base_dino.speed * boost),
        base_dino.special_move
    )
    return boosted_dino

def recursive_walk(dino, text_widget, depth=0, parent_window=None, return_callback=None):
    if dino.health <= 0:
        text_widget.insert(tk.END, f"\nCritical: {dino.name} has run out of health and collapsed! Please feed immediately!")
        return
    if dino.attachment <= 0:
        text_widget.insert(tk.END, f"\nWarning: {dino.name} has lost all attachment and is wandering aimlessly!")
    if depth > 2:
        text_widget.insert(tk.END, f"\n{dino.name} finally came back from the adventure!")
        return

    # Check if battle is triggered
    if parent_window and return_callback and maybe_trigger_battle(dino, parent_window, return_callback):
        return  # Exit walk if a battle starts

    response = dino.walk()
    text_widget.insert(tk.END, "\n" + response)

    if dino.health <= 0:
        text_widget.insert(tk.END, f"\nCritical: {dino.name} has run out of health and collapsed!")
        return
    if dino.attachment <= 0:
        text_widget.insert(tk.END, f"\nWarning: {dino.name} has lost all attachment and is feeling very alone!")

    if random.choice([True, False]):
        text_widget.insert(tk.END, f"\n{dino.name} seems eager to keep exploring...")
        recursive_walk(dino, text_widget, depth + 1, parent_window, return_callback)
    else:
        text_widget.insert(tk.END, f"\n{dino.name} seems satisfied and trots back happily.")





if __name__ == "__main__":
    root = tk.Tk()
    app = DinoSelectionScreen(root)
    root.mainloop()
