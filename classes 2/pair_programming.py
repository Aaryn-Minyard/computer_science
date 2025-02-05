class Room:
    """A generic room class."""
    def __init__(self, room_type, windows, doors, description=""):
        self.room_type = room_type  # e.g., "Bedroom", "Kitchen", etc.
        self.windows = windows
        self.doors = doors
        self.description = description

    def __str__(self):
        return (f"{self.room_type}: {self.windows} window(s), {self.doors} door(s).\n"
                f"Description: {self.description}")


# Example specialized room classes
class Bedroom(Room):
    def __init__(self, windows, doors, description="A cozy place to rest."):
        super().__init__("Bedroom", windows, doors, description)


class Kitchen(Room):
    def __init__(self, windows, doors, description="Where meals are prepared."):
        super().__init__("Kitchen", windows, doors, description)


class LivingRoom(Room):
    def __init__(self, windows, doors, description="A space for relaxation and gatherings."):
        super().__init__("Living Room", windows, doors, description)


class Building:
    def __init__(self, name, stories, materials):
        self.name = name
        self.stories = stories
        self.materials = list(materials)
        self.rooms = []  # List to store room instances

    def add_room(self, room):
        """Adds a room instance to the building."""
        self.rooms.append(room)

    def room_summary(self):
        """Prints total number of rooms and a breakdown by room type."""
        total_rooms = len(self.rooms)
        breakdown = {}
        for room in self.rooms:
            breakdown[room.room_type] = breakdown.get(room.room_type, 0) + 1

        print(f"\n{self.name} has a total of {total_rooms} room(s).")
        for room_type, count in breakdown.items():
            print(f"  {room_type}: {count}")

    def __str__(self):
        return (f"{self.name} is a {self.stories}-story building made of "
                f"{', '.join(self.materials)}.")

    def display_menu(self):
        """Displays a simple menu to navigate building room data."""
        while True:
            print("\n==== Building Menu ====")
            print("1. Show Building Overview")
            print("2. List All Rooms (by type)")
            print("3. Show Detailed Room Info")
            print("4. Room Summary (total and breakdown)")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print("\nBuilding Overview:")
                print(self)
            elif choice == "2":
                print("\nRooms by Index:")
                if not self.rooms:
                    print("No rooms have been added yet.")
                else:
                    for idx, room in enumerate(self.rooms, start=1):
                        print(f"{idx}. {room.room_type}")
            elif choice == "3":
                if not self.rooms:
                    print("No rooms available.")
                else:
                    try:
                        idx = int(input("Enter the room number for details: "))
                        if 1 <= idx <= len(self.rooms):
                            print("\nRoom Details:")
                            print(self.rooms[idx - 1])
                        else:
                            print("Invalid room number.")
                    except ValueError:
                        print("Please enter a valid number.")
            elif choice == "4":
                self.room_summary()
            elif choice == "5":
                print("Exiting menu.")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage:
if __name__ == "__main__":
    # Create a building instance
    materials = ["brick", "glass", "steel"]
    building = Building("Skyline Tower", 10, materials)
    
    # Add some rooms
    building.add_room(Bedroom(windows=2, doors=1))
    building.add_room(Kitchen(windows=1, doors=1))
    building.add_room(LivingRoom(windows=3, doors=2, description="Spacious and well-lit."))
    building.add_room(Bedroom(windows=1, doors=1, description="Master bedroom with an ensuite."))
    
    # Start the interactive menu
    building.display_menu()
