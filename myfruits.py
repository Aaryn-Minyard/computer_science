def get_fruits():
    my_fruit1 = input("Fruit 1: ")
    my_fruit2 = input("Fruit 2: ")
    my_fruit3 = input("Fruit 3: ")

    your_fruit1 = input("Fruit 5: ")
    your_fruit2 = input("Fruit 6: ")

    their_fruit = input("Fruit 7: ")
    return my_fruit1,my_fruit2,my_fruit3,your_fruit1,your_fruit2,their_fruit

my_fruit1, my_fruit2, my_fruit3, your_fruit1, your_fruit2, their_fruit = get_fruits()

def sort_fruits(my_fruit1, my_fruit2, my_fruit3, your_fruit1, your_fruit2, their_fruit):
    fruits = [my_fruit1, my_fruit2, my_fruit3]
    print(sorted(fruits))
    fruits.append(your_fruit1)
    print(sorted(fruits))
    fruits.append(your_fruit2)
    print(sorted(fruits))
    fruits.append(their_fruit)
    print(sorted(fruits))
    fruits.remove(my_fruit1)
    print(sorted(fruits))

sort_fruits(my_fruit1, my_fruit2, my_fruit3, your_fruit1, your_fruit2, their_fruit)

