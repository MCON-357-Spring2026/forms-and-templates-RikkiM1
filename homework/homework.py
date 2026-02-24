from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        if not name:
            error = "Name cannot be empty."

        elif not grade.isdigit():
            error = "Grade must be a number."

        elif not (0 <= int(grade) <= 100):
            error = "Grade must be between 0 and 100."

        if not error:
            students.append({"name": name, "grade": int(grade)})
            return redirect(url_for("students"))

    return render_template("add.html", error=error)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    # TODO:
    # Calculate:
    # - total students
    # - average grade
    # - highest grade
    # - lowest gra


    # Check if there are any students
    if len(students) == 0:
        return render_template("summary.html", message="No students available.")

    # Calculate total number of students
    total_students = len(students)

    # Calculate average grade
    total_grade = sum(student['grade'] for student in students)
    average_grade = total_grade / total_students if total_students > 0 else 0

    # Calculate highest grade
    highest_grade = max(student['grade'] for student in students)

    # Calculate lowest grade
    lowest_grade = min(student['grade'] for student in students)

    # Render the summary page with calculated values
    return render_template(
        "summary.html",
        total_students=total_students,
        average_grade=average_grade,
        highest_grade=highest_grade,
        lowest_grade=lowest_grade
    )

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
