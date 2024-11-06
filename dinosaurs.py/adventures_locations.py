import random
from dinosaurs import dinosaurs



# Function for a simple battle system
def battle(dinosaur_party, opponent_dino_name, party):
    opponent_dino = dinosaurs[opponent_dino_name]
    opponent_health = opponent_dino.get('health', 100)

    print(f"A battle begins between your dinosaur party and {opponent_dino['name']}!")

    while opponent_health > 0 and dinosaur_party:
        print("\nYour current dinosaur party:")
        for dino_name in dinosaur_party:
            if dino_name in dinosaurs:
                print(f" - {dinosaurs[dino_name]['name']} (Level: {dinosaurs[dino_name]['level']})")
            else:
                print(f" - {dino_name} (Error: not found in dinosaurs dictionary)")

        player_dino_name = input("Which dinosaur will fight? (Enter dinosaur name): ").strip()

        if player_dino_name not in dinosaur_party:
            print(f"Invalid choice: {player_dino_name} is not in your party.")
            continue
        
        if player_dino_name not in dinosaurs:
            print(f"Error: {player_dino_name} is not found in the dinosaurs dictionary.")
            continue

        player_dino = dinosaurs[player_dino_name]
        player_health = player_dino.get('health', 100)
        
        print(f"\n{player_dino['name']} steps up to fight {opponent_dino['name']}!")
        
        while player_health > 0 and opponent_health > 0:
            attack_verb = input(f"What will {player_dino['name']} do? (input an attack verb, e.g., 'bite', 'charge'): ")
            player_attack = player_dino['attack'] + player_dino['speed'] - opponent_dino['defense']
            
            if player_attack < 0:
                player_attack = 0  # Ensure no negative damage
            
            opponent_health -= player_attack
            print(f"{player_dino['name']} uses {attack_verb} and deals {player_attack} damage!")
            print(f"{opponent_dino['name']} has {opponent_health} health left.\n")
            
            if opponent_health <= 0:
                print(f"{opponent_dino['name']} has been defeated!")
                party.level_up(player_dino_name)  # Level up the victorious dinosaur
                break

            opponent_attack = opponent_dino['attack'] + opponent_dino['speed'] - player_dino['defense']
            
            if opponent_attack < 0:
                opponent_attack = 0
            
            player_health -= opponent_attack
            print(f"{opponent_dino['name']} strikes back and deals {opponent_attack} damage!")
            print(f"{player_dino['name']} has {player_health} health left.\n")
            
            if player_health <= 0:
                print(f"{player_dino['name']} has been defeated!")
                dinosaur_party.remove(player_dino_name)
                break
        
        if opponent_health <= 0:
            print(f"Congratulations! Your party defeated {opponent_dino['name']}.")
            return
        if not dinosaur_party:
            print("Your entire party has been defeated. Game Over.")
            return



def field_of_bones(dinosaur_party, party):
    print("\nYou enter a vast field filled with dinosaur bones and fiery lakes.")
    print("but, as you walk through the field you realize that  the bones are novelty cakes")
    print("and the lake is actually red Kool-Aid")
    print("Your dinosaur(s) enjoy the cake and level up!")
    
     
    for dino_name in dinosaur_party:
        result = party.level_up(dino_name)  # Level up the dinosaur
        print(result)
    
    
    
    
    


def flowers_and_meadows(dinosaur_party, party):
    print("You walk through a peaceful meadow with a calm stream nearby.")
    
    opponent_dino_name = random.choice(list(dinosaurs.keys()))  
    print(f"The lambs scatter in terror as a {dinosaurs[opponent_dino_name]['name']} appears, itching for battle")
    
    if not dinosaur_party:
        print("You can't battle without a dinosaur in your party!")
        return
    
    # Choose a dinosaur from the player's party to battle
    print("Your party:", ", ".join(dinosaur_party))
    battle(dinosaur_party, opponent_dino_name, party)
