students = []
def add_student(id,name,age,gpa):
    student = {
       
    "id": id,
    "name": name,
    "age": age,
    "gpa": gpa

    }
    students.append(student)
    
def show_students() :
    for student in students:
        print(student)

add_student(1, "Ali", 22, 3.8)
add_student(2, "Jerry", 21, 3.5)

show_students()






