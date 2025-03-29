import tkinter as tk
import random
import copy

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
    def __init__(self, party, starting_room, adventure_info):
        self.party = party  # List of user's chosen dinosaurs
        self.current_room = starting_room
        self.adventure_info = adventure_info
        
        self.setup_direction_input()
        self.display_room_description()

    def setup_direction_input(self):
        # Setup for moving between rooms
        direction_label = tk.Label(self.adventure_info, text="Enter direction (north, south, east, west):")
        direction_label.pack()
        self.direction_entry = tk.Entry(self.adventure_info)
        self.direction_entry.pack()
        direction_button = tk.Button(self.adventure_info, text="Go", command=self.handle_direction)
        direction_button.pack()
        self.direction_entry.bind("<Return>", self.handle_direction)

    def display_room_description(self):
        # Display the current room description
        self.adventure_text.insert(tk.END, f"{self.current_room.description}\n")

    def handle_direction(self, event=None):
        # Get direction input and move
        direction = self.direction_entry.get().lower()
        self.move(direction)
        self.direction_entry.delete(0, tk.END)

    def move(self, direction):
        # Handle room transition and battles
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            self.adventure_text.insert(tk.END, f"\n{self.current_room.description}\n")

            if self.current_room.has_battle and not self.current_room.battle_fought:
                opponent = self.get_random_opponent()
                self.start_battle(self.party[0], opponent)
        else:
            self.adventure_text.insert(tk.END, "\nYou can't go that way!\n")

    def start_battle(self, dino1, dino2):
        self.current_room.battle_fought = True
        self.adventure_text.insert(tk.END, f"{dino1.name} vs {dino2.name}! Battle start!\n")
        self.setup_attack_input(dino1, dino2)

    def setup_attack_input(self, dino1, dino2):
        # Setup for player attack input
        attack_label = tk.Label(self.adventure_info, text="Enter your attack move:")
        attack_label.pack()
        self.attack_entry = tk.Entry(self.adventure_info)
        self.attack_entry.pack()
        attack_button = tk.Button(self.adventure_info, text="Attack", command=lambda: self.player_attack(dino1, dino2))
        attack_button.pack()
        self.attack_entry.bind("<Return>", lambda event: self.player_attack(dino1, dino2))

    def player_attack(self, dino1, dino2):
        attack_verb = self.attack_entry.get().strip() or "attack"
        damage = max(1, dino1.attack * 2.5 - dino2.defense)
        self.adventure_text.insert(tk.END, f"{dino1.name} uses {attack_verb} and deals {damage} damage!\n")
        dino2.health -= damage

        if dino2.health <= 0:
            self.adventure_text.insert(tk.END, f"{dino2.name} has fainted!\n")
            level_up_message = dino1.level_up()
            self.adventure_text.insert(tk.END, f"{dino1.name} wins and {level_up_message}!\n")
            return
        self.opponent_attack(dino1, dino2)

    def opponent_attack(self, dino1, dino2):
        damage = max(1, dino2.attack * 2.5 - dino1.defense)
        self.adventure_text.insert(tk.END, f"{dino2.name} retaliates and deals {damage} damage!\n")
        dino1.health -= damage
        if dino1.health <= 0:
            self.adventure_text.insert(tk.END, f"{dino2.name} wins!\n")

    def get_random_opponent(self):
        # Copy a random dinosaur from the library as the opponent
        opponent_name = random.choice(list(dinosaur_library.keys()))
        opponent = copy.deepcopy(dinosaur_library[opponent_name])
        return opponent

def choose_party():
    # Select up to 3 dinosaurs from the library to form the player's party
    adventure_text.insert("Choose up to 3 dinosaurs for your party:")
    party = []
    for _ in range(3):
        choice = tk.Entry(adventure_info)
        choice.pack()
        if choice in dinosaur_library:
            party.append(copy.deepcopy(dinosaur_library[choice]))
            attack_button = tk.Button(adventure_info, text="Add to Party", command=lambda: party.append(dinosaur_library[choice]))
            attack_button.pack()
            adventure_text.insert(f"{choice} added to your party.")
        elif not choice:
            break
        else:
            adventure_text.insert("Dinosaur not found. Try again.")
    return party


# Sample room setup for testing
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


adventure_text = tk.Text(adventure_info, height=20, width=40)
adventure_text.pack()

# Create sample dinosaurs and rooms
party = choose_party()
entrance = Room("Entrance", "You are at the entrance of a dungeon.")
hallway = Room("Hallway", "A dark, narrow hallway.")
n_hallway1 = Room("Hallway", "A dark, narrow hallway.")
treasure_room = Room("Treasure Room", "A room filled with ancient treasure.", has_battle=True)
antechamber = Room("Antechamber", "A small room leading to larger to bigger things", has_battle=True) 
bedroom = Room("Bedroom", "A large bed sits in the center of the room, shackles lie nearby...freaky...", has_battle=True)

    # Connecting rooms (bi-directional)
entrance.connect("north", hallway)
hallway.connect("south", entrance)
hallway.connect("north", antechamber)
antechamber.connect("north", n_hallway1)
antechamber.connect("south", hallway)
n_hallway1.connect("north", bedroom)
bedroom.connect("south", n_hallway1) 
hallway.connect("east", treasure_room)
treasure_room.connect("west", hallway)


# Start the adventure
adventure = Adventure(party, entrance, adventure_info)
root.mainloop()
