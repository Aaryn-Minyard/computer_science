def create_caffeine_decay(caffeine):
    variables = {}
    
    variables["Hour 0"] = caffeine
    for i in range(1, 5):  
        variables[f"Hour {6 * i}"] = variables[f"Hour {6 * (i - 1)}"] / 2

    return variables

caffeine = float(input("How much caffeine did you drink: "))

caffeine_decay = create_caffeine_decay(caffeine)

print(f"Number of variables created: {len(caffeine_decay)}")
print("Caffeine decay over time:")
for var_name, var_value in caffeine_decay.items():
    print(f"{var_name} = {var_value}")
