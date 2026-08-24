
students = []


# Add a student
def add_student(id, name, age, gpa):
    student = {
        "id": id,
        "name": name,
        "age": age,
        "gpa": gpa
    }

    students.append(student)


# Show all students
def show_students():
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
            print(student)
            return

    print("Student not found.")


# Delete a student
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted.")
            return

    print("Student not found.")


# Add students
add_student(1, "Ali", 22, 3.8)
add_student(2, "Jerry", 21, 3.5)
add_student(3, "Ahmed", 23, 3.2)


# Show students
print("ALL STUDENTS")
show_students()


# Search
print("SEARCH RESULT")
search_student(2)


# Delete
print("DELETE")
delete_student(3)


# Show again
print("STUDENTS AFTER DELETE")
show_students()





