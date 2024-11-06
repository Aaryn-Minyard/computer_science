import tkinter as tk

class Dinosaur:
    def __init__(self, name, health, level, attack, defense, special_move):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.special_move = special_move

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 5
        self.defense += 5
        return f"{self.name} leveled up to {self.level}!"

# Predefined library of dinosaurs
dinosaur_library = {
    "Tyrannosaurus": Dinosaur("Tyrannosaurus Rex", 100, 1, 60, 20, "Tail Swipe"),
    "Triceratops": Dinosaur("Triceratops", 90, 1, 25, 30, "Horn Charge"),
    "Velociraptor": Dinosaur("Velociraptor", 80, 1, 35, 15, "Claw Strike"),
    "Brachiosaurus": Dinosaur("Brachiosaurus", 150, 1, 20, 40, "Stomp"),
    "Stegosaurus": Dinosaur("Stegosaurus", 110, 1, 25, 35, "Tail Whip"),
    "Ankylosaurus": Dinosaur("Ankylosaurus", 130, 1, 20, 50, "Club Tail"),
    "Pteranodon": Dinosaur("Pteranodon", 70, 1, 40, 10, "Sky Dive"),
    "Spinosaurus": Dinosaur("Spinosaurus", 100, 1, 40, 20, "Water Slash"),
    "Allosaurus": Dinosaur("Allosaurus", 100, 1, 40, 20, "Wild Bite"),
}

class Adventure:
    def __init__(self, dino1, dino2, starting_room, adventure_info):
        self.dino1 = dino1
        self.dino2 = dino2
        self.current_room = starting_room
        self.adventure_info = adventure_info

        # Text box to display adventure progress
        self.adventure_text = tk.Text(adventure_info, height=20, width=40)
        self.adventure_text.pack()

        # Set up user input for direction entry
        self.setup_direction_input()

        # Display the current room description
        self.display_room_description()

    def setup_direction_input(self):
        # Entry box for the user to type directions
        direction_label = tk.Label(self.adventure_info, text="Enter direction (north, south, east, west):")
        direction_label.pack()

        self.direction_entry = tk.Entry(self.adventure_info)
        self.direction_entry.pack()

        # Button to confirm direction
        direction_button = tk.Button(self.adventure_info, text="Go", command=self.handle_direction)
        direction_button.pack()
        self.direction_entry.bind("<Return>", self.handle_direction)

    def display_room_description(self):
        # Display the current room's description
        self.adventure_text.insert(tk.END, f"{self.current_room.description}\n")

    def handle_direction(self, event=None):
        # Get direction input and move in that direction
        direction = self.direction_entry.get().lower()
        self.move(direction)
        self.direction_entry.delete(0, tk.END)

    def move(self, direction):
        # Move between rooms and trigger battle if necessary
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            self.adventure_text.insert(tk.END, f"\n{self.current_room.description}\n")

            if self.current_room.has_battle and not self.current_room.battle_fought:
                self.start_battle()
        else:
            self.adventure_text.insert(tk.END, "\nYou can't go that way!\n")

    def start_battle(self):
        # Mark battle as fought and initiate battle sequence
        self.current_room.battle_fought = True
        self.adventure_text.insert(tk.END, f"{self.dino1.name} vs {self.dino2.name}! Battle start!\n")
        
        # Setup for attack input
        self.setup_attack_input()

    def setup_attack_input(self):
        # Entry box and button for entering attack names
        attack_label = tk.Label(self.adventure_info, text="Enter your attack move:")
        attack_label.pack()

        self.attack_entry = tk.Entry(self.adventure_info)
        self.attack_entry.pack()

        attack_button = tk.Button(self.adventure_info, text="Attack", command=self.player_attack)
        attack_button.pack()
        self.attack_entry.bind("<Return>", lambda event: self.player_attack())

    def player_attack(self):
        # Get the attack verb from the entry widget and perform attack
        attack_verb = self.attack_entry.get().strip() or "attack"
        damage = max(1, self.dino1.attack * 2.5 - self.dino2.defense)
        self.adventure_text.insert(tk.END, f"{self.dino1.name} uses {attack_verb} and deals {damage} damage!\n")
        self.dino2.health -= damage

        if self.dino2.health <= 0:
            self.adventure_text.insert(tk.END, f"{self.dino2.name} has fainted!\n")
            level_up_message = self.dino1.level_up()  # Example level-up method
            self.adventure_text.insert(tk.END, f"{self.dino1.name} wins and {level_up_message}!\n")
            return

        # Dino 2's turn to attack
        self.opponent_attack()

    def opponent_attack(self):
        # Opponent's turn to attack
        damage = max(1, self.dino2.attack * 2.5 - self.dino1.defense)
        self.adventure_text.insert(tk.END, f"{self.dino2.name} retaliates and deals {damage} damage!\n")
        self.dino1.health -= damage

        if self.dino1.health <= 0:
            self.adventure_text.insert(tk.END, f"{self.dino2.name} wins!\n")
            return
# Sample room, dinosaur, and Tkinter setup for testing


class Room:
    def __init__(self, name, description, has_battle=False):
        self.name = name
        self.description = description
        self.has_battle = has_battle
        self.battle_fought = False
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

# Initialize the root window and adventure_info frame
root = tk.Tk()
adventure_info = tk.Frame(root)
adventure_info.pack()

# Create sample dinosaurs and rooms
dino1 = Dinosaur("Tyrannosaurus", 100, 20, 10)
dino2 = Dinosaur("Velociraptor", 80, 15, 8)
starting_room = Room("Starting Room", "A dimly lit room with exits to the north and east.", has_battle=False)
battle_room = Room("Battle Room", "A dark cave where a fierce enemy awaits.", has_battle=True)
starting_room.connect("north", battle_room)

# Start the adventure
adventure = Adventure(dino1, dino2, starting_room, adventure_info)
root.mainloop()
