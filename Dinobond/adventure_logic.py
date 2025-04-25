import random
import tkinter as tk
from tkinter import messagebox
from battle_screen import BattleScreen
from Dinobond import get_random_opponent, save_game

class AdventureMode:
    def __init__(self, master, player_dino, width=4, height=4):
        self.master = tk.Toplevel(master)
        self.player_dino = player_dino
        self.width = width
        self.height = height
        self.position = (0, 0)  # start at top-left
        self.generate_dungeon()
        self.build_ui()
        self.update_stats()
        self.log_event("Your adventure begins!")

    def generate_dungeon(self):
        # create a grid of events
        events = ["battle"] * ((self.width * self.height)//4) \
               + ["treasure"] * ((self.width * self.height)//8) \
               + ["trap"] * ((self.width * self.height)//8)
        empty_count = self.width * self.height - len(events)
        events += ["empty"] * empty_count
        random.shuffle(events)
        # map coordinates to events
        self.map = {}
        idx = 0
        for y in range(self.height):
            for x in range(self.width):
                self.map[(x, y)] = events[idx]
                idx += 1

    def build_ui(self):
        self.master.title("Dinobond: Adventure Mode")
        self.master.configure(bg="#e3f2e1")
        # Top controls
        top_frame = tk.Frame(self.master, bg="#e3f2e1")
        top_frame.pack(fill=tk.X, pady=5)
        tk.Button(top_frame, text="Feed", command=self.feed, font=("Helvetica",14), bg="#4caf50").pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Pet",  command=self.pet,  font=("Helvetica",14), bg="#4caf50").pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Save", command=lambda: save_game(self.player_dino), font=("Helvetica",14), bg="#2196f3").pack(side=tk.LEFT, padx=5)
        self.stats_label = tk.Label(top_frame, text="", font=("Helvetica",14), bg="#c8e6c9")
        self.stats_label.pack(side=tk.RIGHT, padx=10)

        # Text log
        self.log = tk.Text(self.master, height=20, width=80, font=("Courier New",12), bg="#f1f8e9", wrap="word")
        self.log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Directional controls
        bot_frame = tk.Frame(self.master, bg="#e3f2e1")
        bot_frame.pack(pady=5)
        tk.Button(bot_frame, text="North", command=lambda: self.move(0,-1), font=("Helvetica",14)).grid(row=0, column=1)
        tk.Button(bot_frame, text="West",  command=lambda: self.move(-1,0), font=("Helvetica",14)).grid(row=1, column=0)
        tk.Button(bot_frame, text="East",  command=lambda: self.move(1,0),  font=("Helvetica",14)).grid(row=1, column=2)
        tk.Button(bot_frame, text="South", command=lambda: self.move(0,1),  font=("Helvetica",14)).grid(row=2, column=1)

    def log_event(self, text):
        self.log.insert(tk.END, f"\n{text}")
        self.log.see(tk.END)

    def update_stats(self):
        s = f"{self.player_dino.name} | HP: {self.player_dino.health}/{self.player_dino.max_health} | Attach: {self.player_dino.attachment}"
        self.stats_label.config(text=s)

    def feed(self):
        res = self.player_dino.feed()
        self.log_event(res)
        self.update_stats()

    def pet(self):
        res = self.player_dino.pet()
        self.log_event(res)
        self.update_stats()

    def move(self, dx, dy):
        x,y = self.position
        nx,ny = x+dx, y+dy
        if (nx,ny) not in self.map:
            self.log_event("You can't go that way.")
            return
        self.position = (nx,ny)
        event = self.map[(nx,ny)]
        self.handle_event(event)

    def handle_event(self, event):
        if event == "battle":
            self.log_event("A wild dinosaur appears!")
            opponent = get_random_opponent()
            BattleScreen(self.master, self.player_dino, opponent, return_callback=self.post_battle)
        elif event == "treasure":
            self.player_dino.health = min(self.player_dino.max_health, self.player_dino.health + 10)
            self.log_event("You find a healing fountain! +10 HP")
            self.update_stats()
        elif event == "trap":
            self.player_dino.health -= 10
            self.log_event("It's a trap! -10 HP")
            self.update_stats()
        else:
            self.log_event("The room is empty...")

    def post_battle(self):
        if self.player_dino.health <= 0:
            self.log_event("Your dinosaur has fallen. Adventure over.")
        else:
            self.log_event("You defeated the foe!")
            self.update_stats()