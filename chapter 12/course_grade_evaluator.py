import csv

class Student:
    def __init__(self, first_name, last_name, grade, midterm, final):
        self.name = f"{first_name} {last_name}"  # Combine first and last name
        self.grade = [grade, midterm, final]

    def average(self):
        return sum(self.grade) / len(self.grade)
    
    def letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
        
    def __str__(self):
        return f"{self.name}: {self.letter_grade(self.average())}"

# Read the TSV file and create Student objects
students = []
filename = "chapter 12/StudentInfo.tsv"  # Make sure this is the correct file path!

print(f"Opening file: {filename}")

try:
    with open(filename, newline='', encoding="utf-8") as tsvfile:
        reader = csv.reader(tsvfile, delimiter=' ')  # Read as TSV
        for row in reader:
            print(f"Read row: {row}")  # Debugging: See what’s being read

            # Skip empty or malformed rows
            if not row or len(row) < 5:
                print("Skipping invalid row (empty or missing values)")
                continue

            first_name, last_name = row[0], row[1]
            try:
                grades = list(map(int, row[2:]))  # Convert grades to integers
                student = Student(first_name, last_name, *grades)
                students.append(student)
                print(f"Added student: {student}")  # Debugging: Confirm student creation
            except ValueError:
                print(f"Skipping row with invalid grade data: {row}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found. Check your path!")

# Print out each student's grade information
if students:
    print("\nFinal Student List:")
    for student in students:
        print(student)
else:
    print("\nNo valid students found in the file.")
