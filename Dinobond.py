import tkinter as tk
from tkinter import messagebox
import random
from dinosaur_library import Dinosaur, dinosaur_library



# (Dinosaur class and library go here — unchanged)

def recursive_walk(dino, text_widget, depth=0):
    # Before each recursive call, check for critical conditions.
    if dino.health <= 0:
        text_widget.insert(tk.END, f"\nCritical: {dino.name} has run out of health and collapsed! Please feed immediately!")
        return
    if dino.attachment <= 0:
        text_widget.insert(tk.END, f"\nWarning: {dino.name} has lost all attachment and is wandering aimlessly!")
    
    # Limit recursion depth to prevent infinite loops.
    if depth > 2:
        text_widget.insert(tk.END, f"\n{dino.name} finally came back from the adventure!")
        return
    
    response = dino.walk()
    text_widget.insert(tk.END, "\n" + response)
    
    # Check immediately after walking, and call out if health or attachment is critically low.
    if dino.health <= 0:
        text_widget.insert(tk.END, f"\nCritical: {dino.name} has run out of health and collapsed!")
        return
    if dino.attachment <= 0:
        text_widget.insert(tk.END, f"\nWarning: {dino.name} has lost all attachment and is feeling very alone!")
    
    # 50% chance to trigger another mini-walk recursively.
    if random.choice([True, False]):
        text_widget.insert(tk.END, f"\n{dino.name} seems eager to keep exploring...")
        recursive_walk(dino, text_widget, depth + 1)
    else:
        text_widget.insert(tk.END, f"\n{dino.name} seems satisfied and trots back happily.")

# --- Enhanced Tkinter GUI Game Class ---
class DinoGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("DinoBond: Walks & Whiskers")
        master.configure(bg="#e3f2e1")
        master.geometry("1000x700")
        master.minsize(800, 600)
        self.create_start_screen()

    def create_start_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        label = tk.Label(self.master, text="Choose your dinosaur", font=("Helvetica", 20, "bold"), bg="#e3f2e1")
        label.pack(pady=20)
        self.dino_listbox = tk.Listbox(self.master, height=8, width=40, font=("Helvetica", 14))
        for dino_name in dinosaur_library.keys():
            self.dino_listbox.insert(tk.END, dino_name)
        self.dino_listbox.pack(pady=10)
        select_button = tk.Button(self.master, text="Select", command=self.select_dino, font=("Helvetica", 14), bg="#4caf50", fg="white", padx=10, pady=5)
        select_button.pack(pady=10)

    def select_dino(self):
        try:
            selection = self.dino_listbox.curselection()
            dino_name = self.dino_listbox.get(selection)
        except Exception:
            messagebox.showerror("Error", "Please select a dinosaur.")
            return
        self.player_dino = dinosaur_library[dino_name]
        self.create_game_screen()

    def create_game_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.master.configure(bg="#e3f2e1")

        # Display dinosaur stats at the top.
        self.stats_label = tk.Label(self.master, text=str(self.player_dino), font=("Helvetica", 14), bg="#c8e6c9", wraplength=900, justify="left")
        self.stats_label.pack(pady=20, fill=tk.X, padx=20)

        # Frame for game buttons.
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

        # Expanded Text Area for event logs.
        self.text_area = tk.Text(self.master, height=20, width=100, font=("Courier New", 12), bg="#f1f8e9", wrap="word")
        self.text_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.text_area.insert(tk.END, f"Welcome, Trainer! You're now bonding with {self.player_dino.name}.\n")
        self.update_stats()

    def update_stats(self):
        self.stats_label.config(text=str(self.player_dino))

    def feed_dino(self):
        result = self.player_dino.feed()
        self.text_area.insert(tk.END, "\n" + result)
        self.update_stats()

    def pet_dino(self):
        result = self.player_dino.pet()
        self.text_area.insert(tk.END, "\n" + result)
        self.update_stats()

    def walk_dino(self):
        recursive_walk(self.player_dino, self.text_area)
        self.update_stats()

# --- Running the Enhanced GUI Game ---
if __name__ == "__main__":
    root = tk.Tk()
    game = DinoGameGUI(root)
    root.mainloop()