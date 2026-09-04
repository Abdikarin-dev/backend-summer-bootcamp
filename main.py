import json

students = []
FILE_PATH = "data/students.json"


# Load students from JSON
def load_students():
    global students

    try:
        with open(FILE_PATH, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


# Save students to JSON
def save_students():
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)


# Add a student
def add_student(id, name, age, gpa):
    student = {
        "id": id,
        "name": name,
        "age": age,
        "gpa": gpa
    }

    students.append(student)
    save_students()


# Show all students
def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"GPA: {student['gpa']}")
        print("-" * 20)


# Search for a student
def search_student(student_id):
    for student in students:
        if student["id"] == student_id:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"GPA: {student['gpa']}")
            return

    print("Student not found.")


# Delete a student
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students()
            print("Student deleted.")
            return

    print("Student not found.")


# Load existing students
load_students()


# Main menu
if __name__ == "__main__":

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Add student
        if choice == "1":

            # ID validation
            try:
                id = int(input("Enter student ID: "))
            except ValueError:
                print("ID must be a number.")
                continue

            # Name validation
            name = input("Enter student name: ")

            if not name.strip():
                print("Name cannot be empty.")
                continue

            # Age validation
            try:
                age = int(input("Enter student age: "))

                if age <= 0:
                    print("Age must be greater than 0.")
                    continue

            except ValueError:
                print("Age must be a number.")
                continue

            # GPA validation
            try:
                gpa = float(input("Enter student GPA: "))

                if gpa < 0 or gpa > 4:
                    print("GPA must be between 0 and 4.")
                    continue

            except ValueError:
                print("GPA must be a number.")
                continue

            add_student(id, name, age, gpa)
            print("Student added.")

        # Show students
        elif choice == "2":
            show_students()

        # Search student
        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
                search_student(student_id)
            except ValueError:
                print("ID must be a number.")

        # Delete student
        elif choice == "4":
            try:
                student_id = int(input("Enter student ID: "))
                delete_student(student_id)
            except ValueError:
                print("ID must be a number.")

        # Exit
        elif choice == "5":
            print("Goodbye!")
            break

        # Invalid menu option
        else:
            print("Invalid choice.")