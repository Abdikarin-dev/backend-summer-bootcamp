from flask import Flask, jsonify
import main

app = Flask(__name__)


@app.route("/")
def home():
    return "Student Management System API is running!"


@app.route("/students")
def get_students():
    main.load_students()
    return jsonify(main.students)


@app.route("/students/<int:student_id>")
def get_student(student_id):
    main.load_students()

    for student in main.students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"message": "Student not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)