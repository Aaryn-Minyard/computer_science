# Define the custom exception type
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Function to find student ID by name
def find_ID(student_name, student_dict):
    if student_name in student_dict:
        return student_dict[student_name]
    else:
        raise StudentInfoError(f"Student ID not found for {student_name}")

# Function to find student name by ID
def find_name(student_id, student_dict):
    # Reverse the dictionary to search by ID
    reversed_dict = {v: k for k, v in student_dict.items()}
    if student_id in reversed_dict:
        return reversed_dict[student_id]
    else:
        raise StudentInfoError(f"Student name not found for {student_id}")

def main():
    # Sample student dictionary with name as key and ID as value
    students = {
    "Aaryn": "aaminyard582",
    "Goku":  "gthompson764",
    "Vegeta": "vgriffin931",
    "Luffy":  "ljohnson427",
    "Zoro":   "zcarter358",
    "Nami":   "nroberts639",
    "Sanji":  "sallen823",
    "Chopper": "cwhite234",
    "Robin":  "rgreen567",
    "Franky": "fclark890",
    "Brook":  "bmartin123",
    "Usopp":  "ujackson456",
    "Jinbe":  "jlewis789",
    "Shanks": "swalker012",
    }
    
    # Ask the user to choose to find by ID or name
    while True:
        try:
            choice = int(input("Enter 0 to find ID by name or 1 to find name by ID: "))
            if choice not in [0, 1]:
                raise ValueError("Invalid choice. Please enter 0 or 1.")
                

            if choice == 0:  # Find ID by name
                name = input("Enter the student's name: ")
                print(f"The ID for {name} is {find_ID(name, students)}")

            elif choice == 1:  # Find name by ID
                student_id = input("Enter the student's ID: ")
                print(f"The name for student ID {student_id} is {find_name(student_id, students)}")

        except (ValueError, StudentInfoError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
