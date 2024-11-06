import random
from dinosaurs import dinosaurs
from adventures_locations import * 



class DinosaurParty:
    def __init__(self):
        self.party = []
        self.max_size = 3
    
    def add_dinosaur(self, dino_name):
        if len(self.party) < self.max_size and dino_name in dinosaurs and dino_name not in self.party:
            self.party.append(dino_name)
            return f"{dinosaurs[dino_name]['name']} has been added to your party."
        elif len(self.party) >= self.max_size:
            return "Your party is full."
        else:
            return f"{dino_name} is already in your party or not found."
    
    def view_party(self):
        if not self.party:
            return "Your party is currently empty."
        return "\n".join([dinosaurs[dino]['name'] for dino in self.party if dino in dinosaurs])
    

    def level_up(self, dino_name):
        if dino_name in dinosaurs:
            dino = dinosaurs[dino_name]
            dino['level'] += 1  # Increase the level
            dino['health'] += 20  # Increase health with each level
            dino['attack'] += 5  # Increase attack with each level
            dino['defense'] += 3  # Increase defense with each level
            dino['speed'] += 1  # Increase speed with each level
            return f"{dino['name']} leveled up to Level {dino['level']}! Stats improved!"
        else:
            return f"{dino_name} not found in the dinosaur dictionary."


class AdventureGame:
    def __init__(self, dinosaur_party):
        self.dinosaur_party = dinosaur_party
    
    def start_adventure(self):
        if len(self.dinosaur_party.party) == 0:
            print("Your party is currently empty. You can't start an adventure!")
        else:
            self.adventure()
    
    def adventure(self):
        while True:
            print("\nYou gather your Dinosaurs and set out on your journey!")
            print("To your left stretches a field of bones leading into a lake of fire.")
            print("To your right lays a calm stream next to a meadow of frolicking lambs.")
            choice = input("left or right?: ")
            
            if choice.lower() == "left":
                field_of_bones(self.dinosaur_party.party, party)  # Pass the player's party
            elif choice.lower() == "right":
                flowers_and_meadows(self.dinosaur_party.party, party)  # Pass the player's party
            else:
                print("Invalid choice.")
                break

# Initialize the party and the game
party = DinosaurParty()
game = AdventureGame(party)

def display_menu():
    while True:
        print("\nDinosaur Information Menu")
        print("1. Add a dinosaur to your party")
        print("2. View your party")
        print("3. Start your adventure")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            dino_name = input("Enter the name of a dinosaur to add: ")
            print(party.add_dinosaur(dino_name))
        elif choice == '2':
            print(party.view_party())
        elif choice == '3':
            game.start_adventure()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

display_menu()