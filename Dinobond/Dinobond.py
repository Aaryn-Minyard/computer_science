import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os
from dinosaur_library import Dinosaur, dinosaur_library
from adventure_logic import *

# ================== SAVE/LOAD FUNCTIONS ==================
SAVE_FILE = "savegame.json"

def save_game(dino):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(dino.to_dict(), f)
        messagebox.showinfo("Saved", f"{dino.name} was saved successfully!")
    except Exception as e:
        messagebox.showerror("Save Error", str(e))

def load_game():
    if not os.path.exists(SAVE_FILE):
        return None
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return Dinosaur.from_dict(data)
    except Exception as e:
        messagebox.showerror("Load Error", str(e))
        return None

# ================== BATTLE SYSTEM FUNCTIONS ==================
def get_random_opponent():
    diet = random.choice(list(dinosaur_library.keys()))
    size = random.choice(list(dinosaur_library[diet].keys()))
    name, base_dino = random.choice(list(dinosaur_library[diet][size].items()))
    boost = random.uniform(1.05, 1.5)
    boosted_dino = Dinosaur(
        name,
        int(base_dino.max_health * boost),
        base_dino.level,
        int(base_dino.attack * boost),
        int(base_dino.defense * boost),
        int(base_dino.speed * boost),
        base_dino.special_move,
        getattr(base_dino, "mode", "Sandbox")
    )
    return boosted_dino

def maybe_trigger_battle(dino, parent_window, return_callback):
    if random.random() < 0.25:  # 25% chance to trigger a battle
        opponent = get_random_opponent()
        BattleScreen(parent_window, dino, opponent, return_callback)
        return True
    return False

def recursive_walk(dino, text_widget, depth=0, parent_window=None, return_callback=None):
    if dino.health <= 0:
        text_widget.insert(tk.END, f"\nCritical: {dino.name} has run out of health and collapsed! Please feed immediately!")
        return
    if dino.attachment <= 0:
        text_widget.insert(tk.END, f"\nWarning: {dino.name} has lost all attachment and is wandering aimlessly!")
    if depth > 2:
        text_widget.insert(tk.END, f"\n{dino.name} finally came back from the adventure!")
        return
    if parent_window and return_callback and maybe_trigger_battle(dino, parent_window, return_callback):
        return  # Exit walk if a battle starts
    response = dino.walk()
    text_widget.insert(tk.END, "\n" + response)
    if dino.health <= 0:
        text_widget.insert(tk.END, f"\nCritical: {dino.name} has run out of health!")
        return
    if dino.attachment <= 0:
        text_widget.insert(tk.END, f"\nWarning: {dino.name} has lost all attachment!")
    if random.choice([True, False]):
        text_widget.insert(tk.END, f"\n{dino.name} seems eager to keep exploring...")
        recursive_walk(dino, text_widget, depth + 1, parent_window, return_callback)
    else:
        text_widget.insert(tk.END, f"\n{dino.name} returns contentedly.")

# ================== BATTLE SCREEN CLASS ==================
class BattleScreen:
    def __init__(self, master, player_dino, opponent, return_callback):
        self.top = tk.Toplevel(master)
        self.top.title("Battle!")
        self.top.geometry("600x400")
        self.top.configure(bg="#fff3e0")
        self.player_dino = player_dino
        self.opponent = opponent
        self.return_callback = return_callback
        self.create_widgets()

    def create_widgets(self):
        self.log = tk.Text(self.top, height=15, width=70, font=("Courier", 10), wrap="word", bg="#fffde7")
        self.log.pack(pady=10)
        self.log.insert(tk.END, f"A wild {self.opponent.name} appears!\n")
        button_frame = tk.Frame(self.top, bg="#fff3e0")
        button_frame.pack()
        tk.Button(button_frame, text="Attack", font=("Helvetica", 14), bg="#ff8a65", command=self.attack).pack(side="left", padx=10)
        tk.Button(button_frame, text="Run", font=("Helvetica", 14), bg="#90a4ae", command=self.run_away).pack(side="right", padx=10)

    def attack(self):
        player_damage = max(1, self.player_dino.attack - self.opponent.defense)
        opponent_damage = max(1, self.opponent.attack - self.player_dino.defense)
        self.opponent.health -= player_damage
        self.log.insert(tk.END, f"\n{self.player_dino.name} attacks {self.opponent.name} for {player_damage} damage!")
        if self.opponent.health <= 0:
            self.log.insert(tk.END, f"\n{self.opponent.name} is defeated! You win!")
            self.end_battle(won=True)
            return
        self.player_dino.health -= opponent_damage
        self.log.insert(tk.END, f"\n{self.opponent.name} strikes back for {opponent_damage} damage!")
        if self.player_dino.health <= 0:
            self.log.insert(tk.END, f"\n{self.player_dino.name} has fainted... You lose!")
            self.player_dino.attachment = max(0, self.player_dino.attachment - 20)
            self.end_battle(won=False)

    def run_away(self):
        self.log.insert(tk.END, "\nYou ran away safely!")
        self.end_battle(won=None)

    def end_battle(self, won):
        if won is True:
            self.player_dino.attachment += 5
        elif won is False:
            self.player_dino.attachment = max(0, self.player_dino.attachment - 20)
        self.top.after(1500, self.close_battle)

    def close_battle(self):
        self.top.destroy()
        if self.return_callback:
            self.return_callback()

# ================== DIET SELECTION SCREEN ==================
class DinoSelectionScreen:
    def __init__(self, master, mode="Sandbox"):
        self.master = master
        self.mode = mode
        master.title("DinoBond: Select Your Dinosaur")
        master.geometry("600x300")
        master.configure(bg="#e3f2e1")
        self.frame = tk.Frame(master, bg="#e3f2e1")
        self.frame.pack(expand=True)
        tk.Label(self.frame, text="Select Diet:", font=("Helvetica", 14), bg="#e3f2e1").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.diet_var = tk.StringVar()
        self.diet_combobox = ttk.Combobox(self.frame, textvariable=self.diet_var, state="readonly", font=("Helvetica", 12))
        self.diet_combobox['values'] = list(dinosaur_library.keys())
        self.diet_combobox.bind("<<ComboboxSelected>>", self.update_dino_names)
        self.diet_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        tk.Label(self.frame, text="Select Size:", font=("Helvetica", 14), bg="#e3f2e1").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.size_var = tk.StringVar()
        self.size_combobox = ttk.Combobox(self.frame, textvariable=self.size_var, state="readonly", font=("Helvetica", 12))
        self.size_combobox['values'] = ["Large", "Medium", "Small"]
        self.size_combobox.bind("<<ComboboxSelected>>", self.update_dino_names)
        self.size_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        tk.Label(self.frame, text="Select Dinosaur:", font=("Helvetica", 14), bg="#e3f2e1").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.dino_var = tk.StringVar()
        self.dinosaur_combobox = ttk.Combobox(self.frame, textvariable=self.dino_var, state="readonly", font=("Helvetica", 12))
        self.dinosaur_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.select_button = tk.Button(self.frame, text="Select", command=self.select_dino, font=("Helvetica", 14), bg="#4caf50", fg="white")
        self.select_button.grid(row=3, column=0, columnspan=2, pady=20)

    def update_dino_names(self, event=None):
        diet = self.diet_var.get()
        size = self.size_var.get()
        if diet and size:
            try:
                names = list(dinosaur_library[diet][size].keys())
            except KeyError:
                names = []
        else:
            names = []
        self.dinosaur_combobox['values'] = names
        self.dino_var.set('')

    def select_dino(self):
        diet = self.diet_var.get()
        size = self.size_var.get()
        dino_name = self.dino_var.get()
        if not (diet and size and dino_name):
            messagebox.showerror("Selection Error", "Please select a diet, size, and dinosaur.")
            return

        selected_dino = dinosaur_library[diet][size][dino_name]
        selected_dino.mode = self.mode
        self.frame.destroy()

        if self.mode == "Sandbox":
            DinoGameGUI(self.master, selected_dino)
        else:
            AdventureMode(self.master, selected_dino)  # Make sure AdventureMode is defined!


# ================== MAIN GAME SCREEN ==================
class DinoGameGUI:
    def __init__(self, master, player_dino):
        self.master = master
        self.player_dino = player_dino
        master.title("DinoBond: Walks & Whiskers")
        master.configure(bg="#e3f2e1")
        master.geometry("1000x700")
        master.minsize(800, 600)
        self.create_game_screen()

    def create_game_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.master.configure(bg="#e3f2e1")
        self.stats_label = tk.Label(self.master, text=str(self.player_dino), font=("Helvetica", 14), bg="#c8e6c9", wraplength=900, justify="left")
        self.stats_label.pack(pady=20, fill=tk.X, padx=20)
        button_frame = tk.Frame(self.master, bg="#e3f2e1")
        button_frame.pack(pady=10)
        buttons = [
            ("Feed", self.feed_dino),
            ("Pet", self.pet_dino),
            ("Walk", self.walk_dino),
            ("Save Game", self.save_current_game),
            ("Quit", self.master.quit)
        ]
        for idx, (text, command) in enumerate(buttons):
            tk.Button(button_frame, text=text, command=command, font=("Helvetica", 14), bg="#4caf50", fg="white", width=15, padx=10, pady=5).grid(row=0, column=idx, padx=10)
        self.text_area = tk.Text(self.master, height=20, width=100, font=("Courier New", 12), bg="#f1f8e9", wrap="word")
        self.text_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.text_area.insert(tk.END, f"Welcome, Trainer! You're now bonding with {self.player_dino.name} in {self.player_dino.mode} mode.\n")
        self.update_stats()

    def update_stats(self):
        self.stats_label.config(text=str(self.player_dino))

    def feed_dino(self):
        self.text_area.delete(1.0, tk.END)
        result = self.player_dino.feed()
        self.text_area.insert(tk.END, f"You fed {self.player_dino.name}.\n{result}")
        self.update_stats()

    def pet_dino(self):
        self.text_area.delete(1.0, tk.END)
        result = self.player_dino.pet()
        self.text_area.insert(tk.END, f"You pet {self.player_dino.name}.\n{result}")
        self.update_stats()

    def walk_dino(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"{self.player_dino.name} starts walking...\n")
        recursive_walk(self.player_dino, self.text_area, parent_window=self.master, return_callback=self.create_game_screen)
        self.update_stats()

    def save_current_game(self):
        save_game(self.player_dino)

# ================== MAIN MENU & MODE SELECTOR ==================
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dinobond - Main Menu")
        self.configure(bg="black")
        self.geometry("400x300")
        title = tk.Label(self, text="Welcome to Dinobond", font=("Arial", 20), fg="red", bg="black")
        title.pack(pady=20)
        tk.Button(self, text="Load Previous Game", command=self.load_game, font=("Arial", 14), fg="red", bg="black", width=25).pack(pady=10)
        tk.Button(self, text="Start New Game", command=self.select_mode, font=("Arial", 14), fg="red", bg="black", width=25).pack(pady=10)
        self.mainloop()

    def load_game(self):
        dino = load_game()
        if dino:
            messagebox.showinfo("Loaded", f"Welcome back, {dino.name} in {dino.mode} mode!")
            self.destroy()
            new_root = tk.Tk()
            DinoGameGUI(new_root, dino)
            new_root.mainloop()
        else:
            messagebox.showwarning("No Save Found", "No saved game was found.")

    def select_mode(self):
        self.destroy()
        ModeSelector()

class ModeSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Choose Game Mode")
        self.configure(bg="black")
        self.geometry("400x250")

        prompt = tk.Label(self, text="Choose Game Mode:", fg="red", bg="black", font=("Arial", 14))
        prompt.pack(pady=10)

        tk.Button(self, text="Sandbox", command=lambda: self.start_new_game("Sandbox"),
                  fg="red", bg="black", font=("Arial", 14)).pack(pady=5)

        tk.Button(self, text="Adventure", command=lambda: self.start_new_game("Adventure"),
                  fg="red", bg="black", font=("Arial", 14)).pack(pady=5)

        self.mainloop()

    def start_new_game(self, mode):
        self.destroy()
        new_root = tk.Tk()
        new_root.title("Dinobond: Diet Selection")
        new_root.geometry("600x300")
        new_root.configure(bg="#e3f2e1")
        DinoSelectionScreen(new_root, mode)
        new_root.mainloop()


# ================== LAUNCH THE GAME ==================
if __name__ == "__main__":
    MainMenu()
