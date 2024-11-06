import pygame
import random
import copy
import sys
from enum import Enum
from collections.abc import Iterable
from typing import Generator

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Terra Rex")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("arial", 20)

# Define the Room class
class Room:
    def __init__(self, name, description, has_battle=False, x=0, y=0):
        self.name = name
        self.description = description
        self.connected_rooms = {}
        self.has_battle = has_battle
        self.battle_fought = False  # Tracks if a battle has been fought here
        self.x = x  # X-coordinate for graphical map
        self.y = y  # Y-coordinate for graphical map

    def connect(self, direction, room):
        self.connected_rooms[direction] = room

    def describe(self):
        return f"You are in {self.name}. {self.description}"

# Define the Party and Dinosaur classes (as per your original code)
class Dinosaur:
    def __init__(self, name, health, level, attack, defense, special_move):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.special_move = special_move

    def use_special_move(self, opponent):
        damage = self.attack * 1.5 - opponent.defense
        damage = max(1, damage)  # Ensure at least 1 damage
        opponent.health -= damage
        return f"{self.name} used {self.special_move}! It dealt {damage} damage."

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has fainted!"
        else:
            return f"{self.name} took {damage} damage, {self.health} health remaining."

    def level_up(self):
        self.health += 10
        self.level += 1
        self.attack += 5
        self.defense += 5
        return f"{self.name} leveled up! Level {self.level}"

    def __str__(self):
        return f"{self.name} (Lv: {self.level}, HP: {self.health}, ATK: {self.attack}, DEF: {self.defense}, Special: {self.special_move})"

class Party:
    def __init__(self):
        self.dinosaurs = []

    def add_dinosaur(self, dino_name):
        if dino_name in dinosaur_library:
            dinosaur = copy.deepcopy(dinosaur_library[dino_name])
            self.dinosaurs.append(dinosaur)
            return f"{dinosaur.name} has been added to your party!"
        else:
            return f"Sorry, {dino_name} is not available."

    def view_party(self):
        if not self.dinosaurs:
            return "Your party is empty."
        return "\n".join([str(dino) for dino in self.dinosaurs])

# Define the dinosaur library
dinosaur_library = {
    "Tyrannosaurus": Dinosaur("Tyrannosaurus Rex", 100, 1, 60, 20, "Tail Swipe"),
    "Triceratops": Dinosaur("Triceratops", 90, 1, 25, 30, "Horn Charge"),
    "Velociraptor": Dinosaur("Velociraptor", 80, 1, 35, 15, "Claw Strike"),
    "Brachiosaurus": Dinosaur("Brachiosaurus", 150, 1, 20, 40, "Stomp"),
    "Stegosaurus": Dinosaur("Stegosaurus", 110, 1, 25, 35, "Tail Whip"),
    "Ankylosaurus": Dinosaur("Ankylosaurus", 130, 1, 20, 50, "Club Tail"),
    "Pteranodon": Dinosaur("Pteranodon", 70, 1, 40, 10, "Sky Dive"),
    "Spinosaurus": Dinosaur("Spinosaurus", 100, 1, 40, 20, "Water Slash"),
    # Add more dinosaurs here
}

# Initialize the party
party = Party()

# Define the render_map function
def render_map(current_room, all_rooms):
    screen.fill(WHITE)

    # Draw connections between rooms
    for room in all_rooms:
        for direction, connected_room in room.connected_rooms.items():
            pygame.draw.line(screen, BLACK, (room.x, room.y), (connected_room.x, connected_room.y), 2)

    # Draw rooms
    for room in all_rooms:
        # Highlight current room
        if room == current_room:
            pygame.draw.circle(screen, YELLOW, (room.x, room.y), 20)
        else:
            pygame.draw.circle(screen, GREEN, (room.x, room.y), 15)
        
        # Draw room name
        text = font.render(room.name, True, BLACK)
        text_rect = text.get_rect(center=(room.x, room.y - 30))
        screen.blit(text, text_rect)

    pygame.display.flip()


def render_party():
    screen.fill(WHITE)
    y_offset = 50
    text = font.render("Your Party:", True, BLACK)
    screen.blit(text, (50, y_offset))

    for idx, dino in enumerate(party.dinosaurs):
        dino_text = font.render(f"{idx + 1}. {dino.name}: HP: {dino.health} | ATK: {dino.attack} | DEF: {dino.defense}", True, BLACK)
        screen.blit(dino_text, (50, y_offset + 30 * (idx + 1)))

    pygame.display.flip()

def render_battle(player_dino, opponent_dino):
    screen.fill(WHITE)

    # Display player dinosaur
    player_text = font.render(f"{player_dino.name}: HP: {player_dino.health}", True, BLACK)
    screen.blit(player_text, (100, 150))

    # Display opponent dinosaur
    opponent_text = font.render(f"{opponent_dino.name}: HP: {opponent_dino.health}", True, BLACK)
    screen.blit(opponent_text, (500, 150))

    # Render battle messages
    battle_msg = font.render("Fight!", True, RED)
    screen.blit(battle_msg, (350, 300))

    pygame.display.flip()

# Define the battle function
def battle(dino1, dino2):
    print(f"{dino1.name} vs {dino2.name}! Battle start!")

    while dino1.health > 0 and dino2.health > 0:
        # Dino 1 attacks
        attack_verb = input("Describe your attack (e.g., bite, chomp, slap): ")
        damage = dino1.attack * 2.5 - dino2.defense
        damage = max(1, damage)  # Ensure at least 1 damage
        print(f"{dino1.name} uses {attack_verb} and deals {damage} damage!")
        dino2.health -= damage
        if dino2.health <= 0:
            print(f"{dino2.name} has fainted!")
            level_up_message = dino1.level_up()  # Level up after victory
            return f"\n{dino1.name} wins and {level_up_message}!"
        
        # Dino 2 attacks
        damage = dino2.attack * 2.5 - dino1.defense
        damage = max(1, damage)
        print(f"{dino2.name} retaliates and deals {damage} damage!")
        dino1.health -= damage
        if dino1.health <= 0:
            print(f"{dino2.name} wins!")
            return f"{dino2.name} wins!"

# Define the move function
def move(current_room, direction, all_rooms):
    if direction in current_room.connected_rooms:
        new_room = current_room.connected_rooms[direction]
        print(new_room.describe())

        if new_room.has_battle and not new_room.battle_fought:
            print("A battle is about to start!")
            new_room.battle_fought = True
            opponent_name = random.choice(list(dinosaur_library.keys()))
            opponent_dinosaur = copy.deepcopy(dinosaur_library[opponent_name])

            if not party.dinosaurs:
                print("You have no dinosaurs to battle!")
                return new_room

            print("\nChoose a dinosaur from your party to battle:")
            for idx, dino in enumerate(party.dinosaurs):
                print(f"{idx + 1}. {dino.name} (HP: {dino.health}, Attack: {dino.attack}, Defense: {dino.defense})")

            while True:
                try:
                    choice = int(input("Enter the number of the dinosaur you want to use: ")) - 1
                    if 0 <= choice < len(party.dinosaurs):
                        player_dinosaur = party.dinosaurs[choice]
                        print(f"\nYou chose {player_dinosaur.name} for battle!")
                        break
                    else:
                        print("Invalid selection. Please choose a valid dinosaur.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            result = battle(player_dinosaur, opponent_dinosaur)
            print(result)

        return new_room
    else:
        print(f"You can't move {direction} from here.")
        return current_room
        

# Define the controller (for command-line input)
def controller():
    while True:
        yield input("What would you like to do? ")

# Define the model
def model(user_inputs: Iterable[str], current_room: Room, all_rooms: list) -> list:
    outputs = []
    for user_input in user_inputs:
        try:
            command = Command(user_input.upper())
        except ValueError:
            error_msg = f"{user_input} is not a valid command. Valid commands are (N), (S), (E), (W), (M), and (P)."
            outputs.append(error_msg)
            continue
        
        if command in [Command.NORTH, Command.SOUTH, Command.EAST, Command.WEST]:
            direction = command.name.lower()
            next_room = move(current_room, direction, all_rooms)  # Move to the next room
            
            if isinstance(next_room, Room):
                current_room = next_room  # Move to the next room
                render_map(current_room, all_rooms)
                outputs.append(f"You move {direction} to {current_room.name}.")
                # Trigger battle if the room has one
                if current_room.has_battle:
                    # Battle logic handled in move
                    pass
            else:
                outputs.append(next_room)  # Output the error message if movement is invalid
        
        elif command == Command.OPEN_MAP:
            # Display party and map
            print("IT PASSES")
            
            # Render map visually using Pygame
            render_map(current_room, all_rooms)
           
        
        elif command == Command.CHECK_PARTY:
            outputs.append(party.view_party())  # Access party directly

    return outputs

# Define the view
def view(to_print: Iterable[str], all_rooms: list, current_room: Room):
    for s in to_print:
        print(s)  # Keeping console output for debugging or text-based messages

# Define the Command enum
class Command(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    OPEN_MAP = "M"
    CHECK_PARTY = "P"

def mvc(current_room, all_rooms):
    print(current_room.describe())
    print(party.view_party())
    
    user_inputs = controller()
    processed = model(user_inputs=user_inputs, current_room=current_room, all_rooms=all_rooms)  # Now passing all_rooms
    view(processed)
    current_room = controller(processed)


def get_dino_name_input():
        input_box = pygame.Rect(50, 400, 400, 40)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        dino_name = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked inside the input box
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                            return dino_name
                        elif event.key == pygame.K_BACKSPACE:
                            dino_name = dino_name[:-1]
                        else:
                            dino_name += event.unicode

            screen.fill(BLACK)
            display_message("Enter the name of a dinosaur to add (e.g., Tyrannosaurus):")
            txt_surface = font.render(dino_name, True, WHITE)
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()

# Display menu to add dinosaurs
def display_menu(starting_room: Room, all_rooms: list):
    options = [
        "1. Add a dinosaur to your party",
        "2. View your party",
        "3. Start your adventure",
        "4. Exit"
    ]
    
    while True:
        screen.fill(BLACK)
        y_offset = 50  # Starting position for text
        display_message("Dinosaur Information Menu")
        
        for option in options:
            display_message(option, y_offset)
            y_offset += 30  # Increment offset for each option
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    dino_name = get_dino_name_input()  # Get dinosaur name from Pygame input
                    add_message = party.add_dinosaur(dino_name)
                    display_message(add_message)
                    pygame.display.flip()
                    pygame.time.delay(1000)  # Delay to show the message before returning to the menu
                elif event.key == pygame.K_2:
                    party_message = party.view_party()
                    display_message(party_message)
                    pygame.display.flip()
                    pygame.time.delay(2000)  # Delay to view the party before returning to the menu
                elif event.key == pygame.K_3:
                    print("Starting adventure...")
                    mvc(starting_room, all_rooms)  # Start the game with MVC system
                elif event.key == pygame.K_4:
                    print("Exiting program. Goodbye!")
                    pygame.quit()
                    exit()

def display_message(message, y_offset=0):
    text = font.render(message, True, WHITE)
    screen.blit(text, (50, y_offset))  # Adjust position as needed

# Setting up rooms and connections
def setup_rooms_with_all():
    entrance = Room("Entrance", "You are at the entrance of a cave.", x=100, y=300)
    hallway = Room("Hallway", "A dark, narrow hallway.", x=300, y=300)
    n_hallway1 = Room("Hallway1", "A dark, narrow hallway.", x=500, y=300)
    n_hallway2 = Room("Hallway2", "A dark, narrow hallway.", x=700, y=300)
    n_hallway3 = Room("Hallway3", "A dark, narrow hallway.", x=900, y=300)
    treasure_room = Room("Treasure Room", "A room filled with ancient treasure.", has_battle=True, x=300, y=100)
    antechamber = Room("Antechamber", "A small room leading to bigger things.", has_battle=True, x=300, y=500)
    bedroom = Room("Bedroom", "A large bed sits in the center of the room, shackles lie nearby...freaky...", has_battle=True, x=500, y=500)

    # Connecting rooms (bi-directional)
    entrance.connect("east", hallway)
    hallway.connect("west", entrance)
    hallway.connect("east", n_hallway1)
    n_hallway1.connect("west", hallway)
    hallway.connect("north", treasure_room)
    treasure_room.connect("south", hallway)
    hallway.connect("south", antechamber)
    antechamber.connect("south", hallway)
    antechamber.connect("east", n_hallway1)
    n_hallway1.connect("west", antechamber)
    n_hallway1.connect("east", n_hallway2)
    n_hallway2.connect("west", n_hallway1)
    n_hallway2.connect("east", n_hallway3)
    n_hallway3.connect("west", n_hallway2)
    n_hallway1.connect("north", bedroom)
    bedroom.connect("south", n_hallway1)

    all_rooms = [entrance, hallway, n_hallway1, n_hallway2, n_hallway3, treasure_room, antechamber, bedroom]
    return entrance, all_rooms

party = None

# Main function to tie everything together
def main():
    global party
    party = Party()
    starting_room, all_rooms = setup_rooms_with_all()
    display_menu(starting_room, all_rooms)

if __name__ == "__main__":
    main()
