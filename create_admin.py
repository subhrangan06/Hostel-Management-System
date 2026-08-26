import mysql.connector
from werkzeug.security import generate_password_hash


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="hostel_management"
)

cursor = connection.cursor()

username = "admin"
password = "admin123"

hashed_password = generate_password_hash(password)

cursor.execute(
    """
    INSERT INTO users
    (username, password, role)
    VALUES (%s, %s, %s)
    """,
    (
        username,
        hashed_password,
        "admin"
    )
)

connection.commit()

print("Admin account created successfully.")

cursor.close()
connection.close()