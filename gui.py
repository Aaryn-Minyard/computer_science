import tkinter as tk
import pygame
import sys
import random
import copy

# Dinosaur class from your Terra Rex game
class Dinosaur:
    def __init__(self, name, health, level, attack, defense, special_move):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.special_move = special_move

    def __str__(self):
        return f"{self.name} (Lv. {self.level}) - HP: {self.health} | ATK: {self.attack} | DEF: {self.defense}"

# Sample dinosaur library
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

# Sample party setup
party = [
    Dinosaur("Tyrannosaurus Rex", 100, 10, 50, 30, "Tail Swipe"),
    Dinosaur("Triceratops", 120, 8, 40, 50, "Horn Charge"),
]

def battle(dino1, dino2, adventure_text):
    current_room.battle_fought = True
    adventure_text.insert(f"{dino1.name} vs {dino2.name}! Battle start!")

    while dino1.health > 0 and dino2.health > 0:
        # Dino 1 attacks
        attack_verb = input("Describe your attack (e.g., bite, chomp, slap): ")
        damage = dino1.attack * 2.5 - dino2.defense
        damage = max(1, damage)  # Ensure at least 1 damage
        adventure_text.insert(f"{dino1.name} uses {attack_verb} and deals {damage} damage!")
        dino2.health -= damage
        if dino2.health <= 0:
            adventure_text.insert(f"{dino2.name} has fainted!")
            level_up_message = dino1.level_up()  # Level up after victory
            return adventure_text.insert(f"\n{dino1.name} wins and {level_up_message}!")
        
        # Dino 2 attacks
        damage = dino2.attack * 2.5 - dino1.defense
        damage = max(1, damage)
        adventure_text.insert(f"{dino2.name} retaliates and deals {damage} damage!")
        dino1.health -= damage
        if dino1.health <= 0:
            adventure_text.insert(f"{dino2.name} wins!")
            return adventure_text.insert(f"{dino2.name} wins!")


# Simple room class for adventure game
class Room:
    def __init__(self, name, description, has_battle=False):
        self.name = name
        self.description = description
        self.has_battle = has_battle
        self.battle_fought = False
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

# Create the rooms for the adventure
def create_dungeon():
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
    
    return entrance

# Start room for the adventure
current_room = create_dungeon()

# Initialize Pygame
pygame.init()

# Convert Pygame surface to a format that Tkinter can use (PhotoImage)
def pygame_to_tk(surface):
    width, height = surface.get_size()
    data = pygame.image.tostring(surface, "RGBA")
    image = tk.PhotoImage(width=width, height=height)
    image.put(data, (0, 0, width, height))
    return image

# Pygame setup
def run_pygame(canvas, tk_root):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    
    # Set up Pygame surface based on canvas size
    screen = pygame.Surface((width, height))

    # Game loop for Pygame
    while True:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the Pygame screen with color (e.g., green for the map)
        screen.fill((34, 177, 76))  # RGB for green
        
        # Convert Pygame surface to Tkinter-compatible image
        image = pygame_to_tk(screen)

        # Blit image onto Tkinter canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        tk_root.update_idletasks()

        # Update the Tkinter canvas
        canvas.update()

# Function to display party dinosaurs in Tkinter
def show_party():
    party_info.delete(1.0, tk.END)
    party_info.insert(tk.END, "Your Party:\n\n")
    for dino in party:
        party_info.insert(tk.END, str(dino) + "\n")

# Function to add a dinosaur to the party based on user input
def add_dinosaur():
    dino_name = entry.get().capitalize()  # Capitalize input to match dictionary keys
    if dino_name in dinosaur_library:
        party.append(dinosaur_library[dino_name])
        party_info.insert(tk.END, f"\n{dino_name} added to your party!\n")
        entry.delete(0, tk.END)  # Clear the entry box
    else:
        party_info.insert(tk.END, "\nDinosaur not found in the library.\n")

# Function to open adventure window and start the adventure
def start_adventure():
    global current_room
    global dino1
    global dino2
    
    # Text box to display adventure progress
    adventure_text = tk.Text(adventure_info, height=20, width=40)
    adventure_text.pack()

    # Function to move between rooms
    def move(direction):
        global current_room
        if direction in current_room.connections:
            current_room = current_room.connections[direction]
            adventure_text.insert(tk.END, f"\n{current_room.description}\n")

            if current_room.has_battle and not current_room.battle_fought:
                battle(dino1, dino2, adventure_text)
        else:
            adventure_text.insert(tk.END, "\nYou can't go that way!\n")

    # Display the current room description
    adventure_text.insert(tk.END, f"{current_room.description}\n")
    
    # Entry box for the user to type directions
    direction_label = tk.Label(adventure_info, text="Enter direction (north, south, east, west):")
    direction_label.pack()

    direction_entry = tk.Entry(adventure_info)
    direction_entry.pack()

    # Function to handle direction input
    def handle_direction(event=None):
        direction = direction_entry.get().lower()
        move(direction)
        direction_entry.delete(0, tk.END)

    # Button to confirm direction
    direction_button = tk.Button(adventure_info, text="Go", command=handle_direction)
    direction_button.pack()
    direction_entry.bind("<Return>", handle_direction)

    

# Function to handle menu actions
def handle_menu_selection(selection):
    if selection == "1. Add a dinosaur to your party":
        add_dinosaur()
    elif selection == "2. View your party":
        show_party()
    elif selection == "3. Start your adventure":
        start_adventure()
    elif selection == "4. Exit":
        root.quit()

# Tkinter setup
root = tk.Tk()
root.title("Terra Rex: Dinosaur Adventure")



# Frame for the menu (left side)
menu_frame = tk.Frame(root, width=200, height=480, padx=10, pady=10)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# Menu label
menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 16))
menu_label.pack(pady=10)

# Menu options list
menu_options = [
    "1. Add a dinosaur to your party",
    "2. View your party",
    "3. Start your adventure",
    "4. Exit"
]

# Listbox for the menu
menu_listbox = tk.Listbox(menu_frame, height=10)
for option in menu_options:
    menu_listbox.insert(tk.END, option)
menu_listbox.pack(pady=10)

# Button to confirm menu selection
menu_button = tk.Button(menu_frame, text="Select", command=lambda: handle_menu_selection(menu_listbox.get(tk.ACTIVE)))
menu_button.pack(pady=5)

# Frame for the Pygame canvas (center)
frame = tk.Frame(root, width=400, height=480)
frame.pack(side=tk.LEFT)

# Canvas to hold Pygame screen
canvas = tk.Canvas(frame, width=400, height=480)
canvas.pack()

# Frame for party and controls (right side)
control_frame = tk.Frame(root)
control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

info_frame = tk.Frame(root)  # Set a specific width for info_frame
info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

info_subframe = tk.Frame(info_frame)
info_subframe.pack(side=tk.TOP, fill=tk.X)  # Allow info_subframe to expand horizontally

# Text widget to display the player's party
party_info = tk.Text(control_frame, height=20, width=40)
party_info.pack()

adventure_info = tk.Text(info_subframe, height=20, width=40)
adventure_info.pack(side=tk.LEFT, padx=10, fill=tk.X)  # Allow adventure_info to expand horizontally

# Entry widget for inputting dinosaur name
entry_label = tk.Label(control_frame, text="Add Dinosaur to Party:")
entry_label.pack()

entry = tk.Entry(control_frame)
entry.pack()

# Button to add the dinosaur to the party
add_button = tk.Button(control_frame, text="Add Dinosaur", command=add_dinosaur)
add_button.pack()

# Call the function to run Pygame
root.after(100, run_pygame, canvas, root)

# Start Tkinter main loop
root.mainloop()

