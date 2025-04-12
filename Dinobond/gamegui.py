import tkinter as tk
from tkinter import ttk, messagebox
import random
from dinosaur_library import Dinosaur, dinosaur_library
from Dinobond import recursive_walk

class DinoSelectionScreen:
    def __init__(self, master):
        self.master = master
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
        self.frame.destroy()
        DinoGameGUI(self.master, selected_dino)


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
            ("Quit", self.master.quit)
        ]
        for idx, (text, command) in enumerate(buttons):
            tk.Button(button_frame, text=text, command=command,
                      font=("Helvetica", 14), bg="#4caf50", fg="white", width=15,
                      padx=10, pady=5).grid(row=0, column=idx, padx=10)

        self.text_area = tk.Text(self.master, height=20, width=100, font=("Courier New", 12), bg="#f1f8e9", wrap="word")
        self.text_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.text_area.insert(tk.END, f"Welcome, Trainer! You're now bonding with {self.player_dino.name}.\n")
        self.update_stats()

    def update_stats(self):
        self.stats_label.config(text=str(self.player_dino))

    def feed_dino(self):
        self.text_area.delete(1.0, tk.END)  # Clear previous text
        result = self.player_dino.feed()
        self.text_area.insert(tk.END, f"You fed {self.player_dino.name}.\n{result}")
        self.update_stats()

    def pet_dino(self):
        self.text_area.delete(1.0, tk.END)  # Clear previous text
        result = self.player_dino.pet()
        self.text_area.insert(tk.END, f"You pet {self.player_dino.name}.\n{result}")
        self.update_stats()

    def walk_dino(self):
        self.text_area.delete(1.0, tk.END)  # Clear previous text
        self.text_area.insert(tk.END, f"{self.player_dino.name} starts walking...\n")
        recursive_walk(self.player_dino, self.text_area, parent_window=self.master, return_callback=self.create_game_screen)
        self.update_stats()