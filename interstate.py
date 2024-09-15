def highway_info(highway_number):
    
    if highway_number <= 0 or highway_number > 999:
        return f"{highway_number} is not a valid interstate highway number."

    
    if highway_number >= 1 and highway_number <= 99:
        direction = "north/south" if highway_number % 2 != 0 else "east/west"
        return f"I-{highway_number} is primary, going {direction}."

    
    if highway_number >= 100 and highway_number <= 999:
        primary_highway = highway_number % 100
        if primary_highway == 0:
            return f"{highway_number} is not a valid interstate highway number."
        direction = "north/south" if primary_highway % 2 != 0 else "east/west"
        return f"I-{highway_number} is auxiliary, serving I-{primary_highway}, going {direction}."


highway_number = int(input("Highway Number: "))
print(highway_info(highway_number))
