import random

class Dinosaur:
    def __init__(self, name, health, level, attack, defense, special_move):
        self.name = name
        self.max_health = health
        self.health = health
        self.level = level
        self.attack = attack
        self.defense = defense
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