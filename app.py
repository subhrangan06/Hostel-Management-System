from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "hostel_management_secret_key"


# ---------------- DATABASE CONNECTION ----------------

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="hostel_management"
    )


# ---------------- LOGIN REQUIRED ----------------

def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return function(*args, **kwargs)

    return wrapper


# ---------------- HOME ----------------

@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("dashboard"))

        flash("Invalid username or password.", "danger")

    return render_template("login.html")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
@login_required
def dashboard():

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM rooms")
    total_rooms = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM rooms WHERE status = 'Available'"
    )
    available_rooms = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM complaints WHERE status = 'Pending'"
    )
    pending_complaints = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM fees WHERE status = 'Pending'"
    )
    pending_fees = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        total_rooms=total_rooms,
        available_rooms=available_rooms,
        pending_complaints=pending_complaints,
        pending_fees=pending_fees
    )


# ---------------- STUDENTS ----------------

@app.route("/students")
@login_required
def students():

    search = request.args.get("search", "")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if search:

        query = """
        SELECT * FROM students
        WHERE student_id LIKE %s
        OR name LIKE %s
        OR phone LIKE %s
        """

        search_value = "%" + search + "%"

        cursor.execute(
            query,
            (search_value, search_value, search_value)
        )

    else:

        cursor.execute(
            "SELECT * FROM students ORDER BY id DESC"
        )

    students_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "students.html",
        students=students_data
    )


# ---------------- ADD STUDENT ----------------

@app.route("/students/add", methods=["GET", "POST"])
@login_required
def add_student():

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        gender = request.form["gender"]
        course = request.form["course"]
        year = request.form["year"]
        department = request.form["department"]
        address = request.form["address"]

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO students
                (student_id, name, email, phone, gender,
                 course, year, department, address)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    student_id,
                    name,
                    email,
                    phone,
                    gender,
                    course,
                    year,
                    department,
                    address
                )
            )

            connection.commit()

            flash("Student added successfully.", "success")

        except mysql.connector.Error as error:

            connection.rollback()

            flash(
                "Error adding student: " + str(error),
                "danger"
            )

        cursor.close()
        connection.close()

        return redirect(url_for("students"))

    return render_template("add_student.html")


# ---------------- EDIT STUDENT ----------------

@app.route("/students/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_student(id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        gender = request.form["gender"]
        course = request.form["course"]
        year = request.form["year"]
        department = request.form["department"]
        address = request.form["address"]

        cursor.execute(
            """
            UPDATE students
            SET name=%s,
                email=%s,
                phone=%s,
                gender=%s,
                course=%s,
                year=%s,
                department=%s,
                address=%s
            WHERE id=%s
            """,
            (
                name,
                email,
                phone,
                gender,
                course,
                year,
                department,
                address,
                id
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

        flash("Student updated successfully.", "success")

        return redirect(url_for("students"))

    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (id,)
    )

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template(
        "edit_student.html",
        student=student
    )


# ---------------- DELETE STUDENT ----------------

@app.route("/students/delete/<int:id>")
@login_required
def delete_student(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    flash("Student deleted successfully.", "success")

    return redirect(url_for("students"))


# ---------------- ROOMS ----------------

@app.route("/rooms")
@login_required
def rooms():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM rooms ORDER BY room_number"
    )

    rooms_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "rooms.html",
        rooms=rooms_data
    )


# ---------------- ADD ROOM ----------------

@app.route("/rooms/add", methods=["GET", "POST"])
@login_required
def add_room():

    if request.method == "POST":

        room_number = request.form["room_number"]
        block = request.form["block"]
        floor = request.form["floor"]
        capacity = request.form["capacity"]

        connection = get_db_connection()
        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO rooms
                (room_number, block, floor, capacity)
                VALUES (%s,%s,%s,%s)
                """,
                (
                    room_number,
                    block,
                    floor,
                    capacity
                )
            )

            connection.commit()

            flash("Room added successfully.", "success")

        except mysql.connector.Error as error:

            connection.rollback()

            flash(
                "Error adding room: " + str(error),
                "danger"
            )

        cursor.close()
        connection.close()

        return redirect(url_for("rooms"))

    return render_template("add_room.html")


# ---------------- COMPLAINTS ----------------

@app.route("/complaints")
@login_required
def complaints():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM complaints ORDER BY created_at DESC"
    )

    complaints_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "complaints.html",
        complaints=complaints_data
    )


# ---------------- UPDATE COMPLAINT ----------------

@app.route("/complaints/update/<int:id>", methods=["POST"])
@login_required
def update_complaint(id):

    status = request.form["status"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE complaints
        SET status=%s
        WHERE id=%s
        """,
        (status, id)
    )

    connection.commit()

    cursor.close()
    connection.close()

    flash("Complaint status updated.", "success")

    return redirect(url_for("complaints"))


# ---------------- FEES ----------------

@app.route("/fees")
@login_required
def fees():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM fees ORDER BY id DESC"
    )

    fees_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "fees.html",
        fees=fees_data
    )


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)j