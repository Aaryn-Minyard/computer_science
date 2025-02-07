def carwash():
    services = {'wax': 5, 'tire shine': 2, 'underbody wash': 3, 'mat wash': 1}
    print(services)
    selected_services = []
    base_price = 10

    while True:
        user_input = input("Enter the services you would like to add to your car wash, separated by a comma: ").split(",")
        selected_services = [service.strip().lower() for service in user_input]  # Convert to lowercase for consistency

        if len(selected_services) > 2:
            print("Please select only two additional services.")
        elif "none" in selected_services:
            selected_services = []  # Reset selected services
            print("No additional services selected.")
            break  # Exit the loop
        elif any(service not in services for service in selected_services):
            print("Invalid service entered. Please choose from:", "wax, tire shine, underbody wash, mat wash")
        else:
            break  # Exit the loop if input is valid




    print("You have selected:", selected_services)

# The total price for the car wash
    total_price = base_price + sum([services[service] for service in selected_services])
    print(f"total price: {total_price}")


if __name__ == '__main__':
    carwash()
