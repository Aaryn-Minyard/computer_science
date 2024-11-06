import csv

def write_to_csv():
    def data_function():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        phone_number = input("Enter your phone number: ")
        return f"{first_name},{last_name},{phone_number}"

    filename = input("Enter CSV file name: ")
    data = data_function()

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.split(','))  # Split the data and write it to CSV

    print("Data written to CSV file successfully!")

# Call the write_to_csv function to execute it
write_to_csv()
