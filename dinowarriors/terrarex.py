import random
import pickle
from enum import Enum
from collections.abc import Iterable
from typing import Generator
import copy

class Command(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    OPEN_MAP = "M"
    CHECK_PARTY = "P"

class Dinosaur:
    def __init__(self, name, health, level, attack, defense, special_move):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.special_move = special_move
    
    def use_special_move(self, opponent):
        # Logic for special move
        damage = self.attack * 1.5 - opponent.defense
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




class Party:
    def __init__(self):
        self.dinosaurs = []

    def add_dinosaur(self, dino_name):
        if dino_name in dinosaur_library:
            dinosaur = dinosaur_library[dino_name]
            self.dinosaurs.append(dinosaur)
            return f"{dinosaur.name} has been added to your party!"
        else:
            return f"Sorry, {dino_name} is not available."

    def view_party(self):
        if not self.dinosaurs:
            return "Your party is empty."
        return "\n".join([__str__(dino) for dino in self.dinosaurs])


# Example party management
class Room:
    def __init__(self, name, description, has_battle=False):
        self.name = name
        self.description = description
        self.connected_rooms = {}
        self.has_battle = has_battle
        self.battle_fought = False  # New attribute to track if a battle has been fought here

    def connect(self, direction, room):
        self.connected_rooms[direction] = room

    def describe(self):
        return f"You are in {self.name}. {self.description}"

    def battle_in_room(self):
        if self.battle_fought:
            print("You've already fought the battle in this room.")
            return

        # Mark battle as fought to prevent repeating it
        self.battle_fought = True

        # Choose a random dinosaur from the library as the opponent
        opponent_name = random.choice(list(dinosaur_library.keys()))
        opponent_dinosaur = copy.deepcopy(dinosaur_library[opponent_name])

        # Let the user pick a dinosaur from their party
        if not party.dinosaurs:
            print("You have no dinosaurs to battle!")
            return "No battle."

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

        # Call the battle function with the player's chosen dinosaur and the opponent dinosaur
        result = battle(player_dinosaur, opponent_dinosaur)
        print(result)

# Example battle
def battle(dino1, dino2):
    print(f"{dino1.name} vs {dino2.name}! Battle start!")

    while dino1.health > 0 and dino2.health > 0:
        # Dino 1 attacks
        attack_verb = input("Describe your attack (e.g., bite, chomp, slap): ")
        damage = dino1.attack * 2.5 - dino2.defense
        damage = max(1, damage)  # Ensure there's always at least 1 damage dealt
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

        



def move(current_room, direction):
    if direction in current_room.connected_rooms:
        new_room = current_room.connected_rooms[direction]
        print(new_room.describe())

        # Check if the room triggers a battle
        if new_room.has_battle:
            print("A battle is about to start!")
            new_room.battle_in_room()

        return new_room
    else:
        print(f"You can't move {direction} from here.")
        return current_room

# Model to process commands
def model(user_inputs: Iterable[str], current_room: Room) -> Generator[str, None, None]:
    for user_input in user_inputs:
        try:
            command = Command(user_input.upper())
        except ValueError:
            error_msg = f"{user_input} is not a valid command. Valid commands are (N), (S), (E), (W), (M), and (P)."
            yield error_msg
            continue
        
        if command in [Command.NORTH, Command.SOUTH, Command.EAST, Command.WEST]:
            direction = command.name.lower()
            next_room = move(current_room, direction)  # No need to pass party
            if isinstance(next_room, Room):
                current_room = next_room  # Move to the next room
                yield f"You move {direction} to {current_room.name}."
                # Trigger battle if the room has one
                if current_room.has_battle:
                    current_room.battle_in_room()
            else:
                yield next_room  # Output the error message if movement is invalid
        
        elif command == Command.OPEN_MAP:
            yield "Map opened! (Implement map viewing logic here)"
        
        elif command == Command.CHECK_PARTY:
            yield party.view_party()  # Access party directly


# View to display model outputs
def view(to_print: Iterable[str]):
    for s in to_print:
        print(s)

# Controller to get user inputs
def controller():
    while True:
        yield input("What would you like to do? ")

# Main function to tie MVC together
def mvc(current_room: Room):
    user_inputs = controller()
    processed = model(user_inputs=user_inputs, current_room=current_room)  # No need to pass party explicitly
    view(to_print=processed)


    


# Display menu to add dinosaurs
def display_menu(starting_room: Room):
    while True:
        print("\nDinosaur Information Menu")
        print("1. Add a dinosaur to your party")
        print("2. View your party")
        print("3. Start your adventure")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            
            dino_name = input("Enter the name of a dinosaur to add (e.g., Tyrannosaurus): ")
            print(party.add_dinosaur(dino_name))
            
        elif choice == '2':
            print(party.view_party())
            
        elif choice == '3':
            print("Starting adventure...")
            mvc(starting_room)  # Start the game with MVC system
            
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose again.")



# Setting up rooms and connections
def setup_rooms():
    entrance = Room("Entrance", "You are at the entrance of a cave.")
    hallway = Room("Hallway", "A dark, narrow hallway.")
    n_hallway1 = Room("Hallway", "A dark, narrow hallway.")
    n_hallway2 = Room("Hallway", "A dark, narrow hallway.")
    n_hallway3 = Room("Hallway", "A dark, narrow hallway.")
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

# Initialize the game
if __name__ == "__main__":
    party = Party()
    
    starting_room = setup_rooms()
    display_menu(starting_room)

# Create a party and call the menu
party = Party()
with open('party.pkl', 'wb') as f:
    pickle.dump(party, f)

# Load party from file
with open('party.pkl', 'rb') as f:
    loaded_party = pickle.load(f)
#display_menu(party)  
    


#battle(dino1_name="Tyrannosaurus", dino2_name="Spinosaurus")