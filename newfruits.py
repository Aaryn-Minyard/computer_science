
fruit_names = ["Fruit 1", "Fruit 2", "Fruit 3", "Fruit 5", "Fruit 6", "Fruit 7"]
fruits = [input(f"{name}: ") for name in fruit_names]


my_fruits = fruits[:3]
your_fruits = fruits[3:5]
their_fruit = fruits[5]


fruits = my_fruits[:]


print(sorted(fruits))
fruits.extend(your_fruits)
print(sorted(fruits))
fruits.append(their_fruit)
print(sorted(fruits))


fruits.remove(my_fruits[0])
print(sorted(fruits))
