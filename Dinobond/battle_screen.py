import tkinter as tk
from tkinter import messagebox
import random
from dinosaur_library import dinosaur_library, Dinosaur

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
        attack_bonus = self.player_dino.attachment // 10  # Bonus based on attachment
        player_damage = max(1, self.player_dino.attack + attack_bonus - self.opponent.defense)
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
        self.log.insert(tk.END, f"\nYou ran away safely!")
        self.end_battle(won=None)

    def end_battle(self, won):
        def close_and_return():
            self.top.destroy()
            self.return_callback()

        self.top.after(1500, close_and_return)
        
        if won is True:
            self.player_dino.attachment += 5
        elif won is False:
            self.player_dino.attachment = max(0, self.player_dino.attachment - 20)

# Example usage:
# from battle_screen import BattleScreen
# BattleScreen(master_window, player_dino, return_to_main_callback)
