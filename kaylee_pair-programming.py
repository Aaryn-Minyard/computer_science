def get_age():
    while True:
        age_input = input("Enter your age: ")
        try:
            age = int(age_input)
        except ValueError:
            print("Invalid age.")
            continue  # Re-prompt the user
        if age < 18 or age > 75:
            print("Invalid age.")
            continue  # Re-prompt the user
        return age

def fat_burning_heart_rate(age):
    # Calculate 70% of the difference between 220 and age.
    return 0.70 * (220 - age)

if __name__ == "__main__":
    age = get_age()
    rate = fat_burning_heart_rate(age)
    print("Fat-burning heart rate:", rate)
