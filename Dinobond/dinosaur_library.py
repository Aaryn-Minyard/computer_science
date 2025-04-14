import random

class Dinosaur:
    def __init__(self, name, health, level, attack, defense, speed, special_move):
        self.name = name
        self.max_health = health
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special_move = special_move
        self.hunger = 0  # 0 = full, higher = more hungry
        self.attachment = 5  # Start with a moderate attachment level

    def feed(self):
        if self.health >= self.max_health:
            return f"{self.name} is already at full health and doesn't need food!"
        self.health = min(self.health + 20, self.max_health)
        # Feeding restores some attachment too.
        self.attachment += 1
        return f"You fed {self.name}. Health is now {self.health}."

    def pet(self):
        self.attachment += 2  # Petting boosts attachment more
        return f"You pet {self.name}. Attachment level is now {self.attachment}."

    def walk(self):
        # Expanded list of events with more randomness and complexity
        events = [
            ("ran into a patch of wildflowers and frolicked happily!", +5, +3),
            ("found a shiny rock and became momentarily distracted.", 0, +2),
            ("tripped over a log and hurt a bit.", -10, -1),
            ("chased a butterfly, having an unexpected burst of joy.", +0, +4),
            ("stumbled upon a hidden meadow and took a refreshing nap.", +10, +1),
            ("got caught in a sudden storm, leaving it soaked and shivering.", -15, -2),
            ("encountered a wild boar and had to retreat hastily.", -10, -3),
            ("discovered a secret path in the forest, igniting its adventurous spirit.", +5, +2),
            ("ran along a brook and got a bit tired.", -5, +0),
            ("tried imitating bird calls and amused a flock nearby.", 0, +3),
            ("ate some strange berries and felt weird effects.", -20, 0),
            ("found a delicious herb patch and regained some energy.", +15, +1),
            ("ventured too far and got lost briefly in the woods.", -5, -1)
        ]
        event = random.choice(events)
        health_change, attachment_change = event[1], event[2]
        self.health = max(self.health + health_change, 0)
        self.attachment = max(self.attachment + attachment_change, 0)

        response = f"On your walk, {self.name} {event[0]}"
        if health_change < 0:
            response += f" Lost {abs(health_change)} health."
        elif health_change > 0:
            response += f" Gained {health_change} health."
        if attachment_change < 0:
            response += f" Lost {abs(attachment_change)} attachment."
        elif attachment_change > 0:
            response += f" Gained {attachment_change} attachment."

        return response

    def __str__(self):
        return (f"{self.name} (Lv: {self.level}, HP: {self.health}/{self.max_health}, "
                f"ATK: {self.attack}, DEF: {self.defense}, Special: {self.special_move}, "
                f"Attachment: {self.attachment})")

dinosaur_library = {
    "Herbivore": {
        "Large": {
            "Diplodocus": Dinosaur("Diplodocus", 160, 1, 15, 20, 50, "Tail Whip"),
            "Brachiosaurus": Dinosaur("Brachiosaurus", 150, 1, 20, 40, 50, "Stomp"),
            "Apatosaurus": Dinosaur("Apatosaurus", 155, 1, 18, 25, 45, "Tail Slam"),
            "Argentinosaurus": Dinosaur("Argentinosaurus", 170, 1, 12, 30, 55, "Earthquake Step"),
            "Patagotitan": Dinosaur("Patagotitan", 165, 1, 14, 28, 52, "Ground Pound"),
            "Dreadnoughtus": Dinosaur("Dreadnoughtus", 168, 1, 13, 27, 53, "Heavy Stomp"),
            "Mamenchisaurus": Dinosaur("Mamenchisaurus", 158, 1, 16, 22, 48, "Neck Swing"),
            "Camarasaurus": Dinosaur("Camarasaurus", 152, 1, 17, 24, 47, "Body Slam"),
            "Brontosaurus": Dinosaur("Brontosaurus", 154, 1, 19, 26, 46, "Thunder Tail"),
            "Supersaurus": Dinosaur("Supersaurus", 169, 1, 11, 29, 54, "Mega Stomp")
        },
        "Medium": {
            "Triceratops": Dinosaur("Triceratops", 90, 1, 25, 30, 35, "Horn Charge"),
            "Stegosaurus": Dinosaur("Stegosaurus", 110, 1, 25, 35, 40, "Tail Whip"),
            "Ankylosaurus": Dinosaur("Ankylosaurus", 130, 1, 20, 50, 45, "Club Tail"),
            "Pachyrhinosaurus": Dinosaur("Pachyrhinosaurus", 95, 1, 27, 32, 38, "Nose Bash"),
            "Iguanodon": Dinosaur("Iguanodon", 100, 1, 30, 28, 36, "Thumb Spike"),
            "Lanzhousaurus": Dinosaur("Lanzhousaurus", 98, 1, 29, 29, 37, "Tail Slam"),
            "Lambeosaurus": Dinosaur("Lambeosaurus", 92, 1, 31, 27, 34, "Crest Bash"),
            "Ouranosaurus": Dinosaur("Ouranosaurus", 94, 1, 32, 26, 33, "Sail Swipe"),
            "Maiasaura": Dinosaur("Maiasaura", 96, 1, 28, 30, 35, "Mother's Charge"),
            "Therizinosaurus": Dinosaur("Therizinosaurus", 90, 1, 33, 25, 32, "Spinning Slash")
        },
        "Small": {
            "Gallimimus": Dinosaur("Gallimimus", 80, 1, 35, 15, 20, "Speed Dash"),
            "Hypsilophodon": Dinosaur("Hypsilophodon", 78, 1, 36, 14, 19, "Quick Nibble"),
            "Dryosaurus": Dinosaur("Dryosaurus", 76, 1, 37, 13, 18, "Tail Flick"),
            "Othnielia": Dinosaur("Othnielia", 74, 1, 38, 12, 17, "Nose Bump"),
            "Parksosaurus": Dinosaur("Parksosaurus", 72, 1, 39, 11, 16, "Leg Sweep"),
            "Thescelosaurus": Dinosaur("Thescelosaurus", 70, 1, 40, 10, 15, "Body Slam"),
            "Heterodontosaurus": Dinosaur("Heterodontosaurus", 68, 1, 41, 9, 14, "Tooth Jab"),
            "Lesothosaurus": Dinosaur("Lesothosaurus", 66, 1, 42, 8, 13, "Quick Bite"),
            "Minmi": Dinosaur("Minmi", 64, 1, 43, 7, 12, "Armor Roll"),
            "Scutellosaurus": Dinosaur("Scutellosaurus", 62, 1, 44, 6, 11, "Tail Swipe")
        }
    },

"Carnivore": {
        "Large": {
            "Tyrannosaurus": Dinosaur("Tyrannosaurus Rex", 100, 1, 60, 20, 30, "Tyrant's Roar"),
            "Spinosaurus": Dinosaur("Spinosaurus", 100, 1, 40, 20, 30, "Water Slash"),
            "Giganotosaurus": Dinosaur("Giganotosaurus", 102, 1, 58, 22, 32, "Giant's Fury"),
            "Carcharodontosaurus": Dinosaur("Carcharodontosaurus", 104, 1, 56, 24, 34, "Shark Bite"),
            "Mapusaurus": Dinosaur("Mapusaurus", 106, 1, 54, 26, 36, "Pack Hunt"),
            "Acrocanthosaurus": Dinosaur("Acrocanthosaurus", 108, 1, 52, 28, 38, "Back Slash"),
            "Tarbosaurus": Dinosaur("Tarbosaurus", 110, 1, 50, 30, 40, "Roar Blast"),
            "Saurophaganax": Dinosaur("Saurophaganax", 112, 1, 48, 32, 42, "Tail Slam"),
            "Tyrannotitan": Dinosaur("Tyrannotitan", 114, 1, 46, 34, 44, "Titan Crush"),
            "Megalosaurus": Dinosaur("Megalosaurus", 116, 1, 44, 36, 46, "Stealth Bite")
        },
        "Medium": {
            "Allosaurus": Dinosaur("Allosaurus", 98, 1, 45, 25, 30, "Claw Slash"),
            "Ceratosaurus": Dinosaur("Ceratosaurus", 96, 1, 42, 23, 28, "Horn Jab"),
            "Baryonyx": Dinosaur("Baryonyx", 94, 1, 40, 21, 26, "Water Grip"),
            "Yangchuanosaurus": Dinosaur("Yangchuanosaurus", 92, 1, 38, 20, 24, "Neck Bite"),
            "Majungasaurus": Dinosaur("Majungasaurus", 90, 1, 36, 19, 22, "Crushing Maw"),
            "Metriacanthosaurus": Dinosaur("Metriacanthosaurus", 88, 1, 34, 18, 20, "Spine Charge"),
            "Afrovenator": Dinosaur("Afrovenator", 86, 1, 32, 17, 18, "Rapid Slash"),
            "Torvosaurus": Dinosaur("Torvosaurus", 84, 1, 30, 16, 16, "Savage Rend"),
            "Neovenator": Dinosaur("Neovenator", 82, 1, 28, 15, 14, "Speed Jab"),
            "Fukuiraptor": Dinosaur("Fukuiraptor", 80, 1, 26, 14, 12, "Blade Claw")
        },
        "Small": {
            "Velociraptor": Dinosaur("Velociraptor", 80, 1, 35, 15, 20, "Claw Strike"),
            "Compsognathus": Dinosaur("Compsognathus", 60, 1, 20, 10, 18, "Swarm Peck"),
            "Troodon": Dinosaur("Troodon", 65, 1, 22, 12, 20, "Venom Fang"),
            "Microraptor": Dinosaur("Microraptor", 62, 1, 21, 13, 19, "Wing Slash"),
            "Ornitholestes": Dinosaur("Ornitholestes", 67, 1, 24, 14, 21, "Ambush Leap"),
            "Sinosauropteryx": Dinosaur("Sinosauropteryx", 63, 1, 23, 11, 18, "Tail Feint"),
            "Pyroraptor": Dinosaur("Pyroraptor", 70, 1, 26, 13, 22, "Fire Dash"),
            "Eoraptor": Dinosaur("Eoraptor", 66, 1, 25, 12, 20, "Darting Fang"),
            "Herrerasaurus": Dinosaur("Herrerasaurus", 68, 1, 27, 14, 23, "Savage Bite"),
            "Bambiraptor": Dinosaur("Bambiraptor", 69, 1, 28, 15, 24, "Frenzy Claws")
        }
    }
}