import tkinter as tk
import pygame
import sys

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

class Room:
    def __init__(self, name, description, has_battle=False, x=0, y=0):
        self.name = name
        self.description = description
        self.has_battle = has_battle
        self.x = x
        self.y = y
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

# Initialize rooms with coordinates
entrance = Room("Entrance", "You are at the entrance of a cave.", x=100, y=300)
hallway = Room("Hallway", "A dark, narrow hallway.", x=300, y=300)
n_hallway1 = Room("Hallway1", "A dark, narrow hallway.", x=500, y=300)
n_hallway2 = Room("Hallway2", "A dark, narrow hallway.", x=700, y=300)
n_hallway3 = Room("Hallway3", "A dark, narrow hallway.", x=900, y=300)
treasure_room = Room("Treasure Room", "A room filled with ancient treasure.", has_battle=True, x=300, y=100)
antechamber = Room("Antechamber", "A small room leading to bigger things.", has_battle=True, x=300, y=500)
bedroom = Room("Bedroom", "A large bed sits in the center of the room, shackles lie nearby...freaky...", has_battle=True, x=500, y=500)

# Connect rooms
entrance.connect("east", hallway)
hallway.connect("west", entrance)
hallway.connect("east", n_hallway1)
n_hallway1.connect("west", hallway)
hallway.connect("north", treasure_room)
treasure_room.connect("south", hallway)
hallway.connect("south", antechamber)
antechamber.connect("north", hallway)
antechamber.connect("east", n_hallway1)
n_hallway1.connect("west", antechamber)
n_hallway1.connect("east", n_hallway2)
n_hallway2.connect("west", n_hallway1)
n_hallway2.connect("east", n_hallway3)
n_hallway3.connect("west", n_hallway2)
n_hallway1.connect("south", bedroom)
bedroom.connect("north", n_hallway1)

rooms = [entrance, hallway, n_hallway1, n_hallway2, n_hallway3, treasure_room, antechamber, bedroom]


current_room = entrance

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
    
    # Create a new window for the adventure
    adventure_window = tk.Toplevel(root)
    adventure_window.title("Adventure")
    
    # Text box to display adventure progress
    adventure_text = tk.Text(adventure_info, height=20, width=40)
    adventure_text.pack()

    # Function to move between rooms
    def move(direction):
        global current_room
        if direction in current_room.connections:
            current_room = current_room.connections[direction]
            adventure_text.insert(tk.END, f"\n{current_room.description}\n")
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
    def handle_direction():
        direction = direction_entry.get().lower()
        move(direction)
        direction_entry.delete(0, tk.END)

    # Button to confirm direction
    direction_button = tk.Button(adventure_info, text="Go", command=handle_direction)
    direction_button.pack()

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

# Menu frame (left side)
menu_frame = tk.Frame(root, width=200, height=480, padx=10, pady=10)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 16))
menu_label.pack(pady=10)

menu_options = [
    "1. Add a dinosaur to your party",
    "2. View your party",
    "3. Start your adventure",
    "4. Exit"
]

menu_listbox = tk.Listbox(menu_frame, height=10)
for option in menu_options:
    menu_listbox.insert(tk.END, option)
menu_listbox.pack(pady=10)

menu_button = tk.Button(menu_frame, text="Select", command=lambda: handle_menu_selection(menu_listbox.get(tk.ACTIVE)))
menu_button.pack(pady=5)

# Pygame frame (center)
frame = tk.Frame(root, width=400, height=480)
frame.pack(side=tk.LEFT)

canvas = tk.Canvas(frame, width=400, height=480)
canvas.pack()

# Frame for controls and info (right side)
control_frame = tk.Frame(root)
control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)

info_frame = tk.Frame(control_frame, width=400, height=480, padx=10, pady=10)
info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

# Subframe for map display (left of adventure_info)
map_canvas = tk.Canvas(info_frame, width=180, height=200, bg="white")
map_canvas.pack(side=tk.LEFT, padx=10, expand=False)
map_canvas.pack_propagate(False)

adventure_info = tk.Text(info_frame, height=15, width=15)
adventure_info.pack(side=tk.LEFT, padx=10, expand=False)
adventure_info.pack_propagate(False)

party_info = tk.Text(control_frame, height=15, width=15)
party_info.pack(side=tk.RIGHT, expand=False)
party_info.pack_propagate(False)

entry_label = tk.Label(control_frame, text="Add Dinosaur to Party:")
entry_label.pack()

entry = tk.Entry(control_frame)
entry.pack()

add_button = tk.Button(control_frame, text="Add Dinosaur", command=add_dinosaur)
add_button.pack()

def draw_room(room):
    room_radius = 10
    x, y = room.x / 5, room.y / 5  # Scaling down for the map display
    color = "red" if room.has_battle else "lightblue"
    map_canvas.create_oval(x - room_radius, y - room_radius, x + room_radius, y + room_radius, fill=color)
    map_canvas.create_text(x, y, text=room.name, font=("Arial", 6))

def draw_connections():
    for room in rooms:
        for direction, connected_room in room.connections.items():
            x1, y1 = room.x / 5, room.y / 5
            x2, y2 = connected_room.x / 5, connected_room.y / 5
            map_canvas.create_line(x1, y1, x2, y2, fill="black")

def update_map():
    map_canvas.delete("all")
    for room in rooms:
        draw_room(room)
    draw_connections()

update_map()

root.after(100, run_pygame, canvas, root)
root.mainloop()
