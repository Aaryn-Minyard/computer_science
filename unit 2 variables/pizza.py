import math
import random
def pizza_party():
    while True:
        people = int(input("How many people: "))
        if people <= 0:
            print("There can't be negative people!")
        else:
            pizza = math.ceil((people * 2) / 12)
            cost = pizza * 14.95
            print(f"{people} people are coming")
            print(f"We'll need {pizza} pizzas!")
            print(f"That'll cost ${cost:,.2f} dollars!")


            slices_eaten = random.randint(people * 1, people * 4)
            print(f"The people actually ate {slices_eaten}, slices of pizza.")

                
            total_slices_ordered = pizza * 12
            if slices_eaten <= total_slices_ordered:
                print("Great! You ordered enough pizza!")
            else:
                print(f"Oops! You only ordered {total_slices_ordered}, you should have ordered more.")
        party = input("Plan another pizza party? ")
        if party.lower() != "yes":
            print("Enjoy your pizza!")
            break

pizza_party()       