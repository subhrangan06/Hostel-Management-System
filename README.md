# 🏠 Hostel Management System

A web-based **Hostel Management System** developed using **Python, Flask, MySQL, HTML, CSS, and JavaScript** to simplify and digitize common hostel management activities.

The system provides an admin dashboard for managing students, hostel rooms, fees, and complaints through a centralized database.

---

## 📌 Project Overview

Managing hostel information manually can be time-consuming and difficult to maintain. This project provides a simple web-based solution where hostel administrators can manage important hostel records from a single application.

The system currently focuses on:

* Student management
* Room management
* Hostel fee records
* Complaint management
* Dashboard statistics
* Student search
* Admin authentication

---

## ✨ Features

### 🔐 Admin Authentication

* Secure admin login
* Password hashing using Werkzeug
* Session-based authentication
* Logout functionality

### 👨‍🎓 Student Management

* Add new students
* View student records
* Search students
* Edit student information
* Delete student records

### 🏠 Room Management

* Add hostel rooms
* View room information
* Track room capacity
* Track occupied beds
* Display available beds
* Display room status

### 💰 Fee Management

* View hostel fee records
* Track payment status
* View due dates
* View payment dates
* View payment methods

### 📝 Complaint Management

* View student complaints
* View complaint type and description
* Track complaint status
* Update complaint status

### 📊 Dashboard

The dashboard displays:

* Total students
* Total rooms
* Available rooms
* Pending complaints
* Pending fees

### 🔎 Search

Students can be searched using:

* Student ID
* Student name
* Phone number

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* MySQL

### Python Libraries

* Flask
* mysql-connector-python
* Werkzeug

### Development Tools

* Visual Studio Code
* MySQL Workbench
* Git
* GitHub

---

## 🏗️ Project Architecture

```text
                  ┌─────────────────────┐
                  │       User          │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ HTML / CSS / JS     │
                  │     Frontend        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │      Flask          │
                  │   Python Backend    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │       MySQL         │
                  │      Database       │
                  └─────────────────────┘
```

---

## 📂 Project Structure

```text
hostel-management-system/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── database/
│   └── hostel_management.sql
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   ├── edit_student.html
│   ├── rooms.html
│   ├── add_room.html
│   ├── complaints.html
│   └── fees.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js
```

---

## 🗄️ Database

The project uses **MySQL** as its database.

### Main Tables

```text
users
students
rooms
complaints
fees
```

### Users

Stores administrator login information.

### Students

Stores student details such as:

* Student ID
* Name
* Email
* Phone
* Gender
* Course
* Year
* Department
* Address
* Room number

### Rooms

Stores:

* Room number
* Block
* Floor
* Capacity
* Occupied beds
* Status

### Complaints

Stores:

* Student ID
* Complaint type
* Description
* Status
* Creation date

### Fees

Stores:

* Student ID
* Amount
* Due date
* Payment date
* Payment status
* Payment method

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hostel-management-system.git
```

Move into the project directory:

```bash
cd hostel-management-system
```

---

## 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure MySQL

Make sure **MySQL Server** is installed and running.

Open **MySQL Workbench** and run:

```text
database/hostel_management.sql
```

This will create the required database and tables.

---

## 5. Configure Database Connection

Open `app.py` and update the MySQL credentials:

```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="hostel_management"
    )
```

Replace:

```text
YOUR_MYSQL_PASSWORD
```

with your actual MySQL password.

---

## 6. Create Admin Account

Create an admin account using the provided admin creation script.

Example credentials:

```text
Username: admin
Password: admin123
```

For security, do not upload files containing real passwords or credentials to GitHub.

---

## 7. Run the Application

Start the Flask server:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open the URL in your web browser.

---

# 🔑 Login

Use the administrator credentials created during setup.

```text
Username: admin
Password: admin123
```

**For a real deployment, change the default password immediately.**

---

# 📸 Screenshots

Add screenshots of your application here after running the project.

Example:

```markdown
## 📸 Screenshots

### Login Page

![Login Page](screenshots/login.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Student Management

![Students](screenshots/students.png)

### Room Management

![Rooms](screenshots/rooms.png)

### Complaint Management

![Complaints](screenshots/complaints.png)
```

Recommended screenshots:

1. Login page
2. Dashboard
3. Student management
4. Add student page
5. Room management
6. Complaint management
7. Fee management

---

# 🔄 Application Workflow

```text
Admin
  │
  ▼
Login
  │
  ▼
Dashboard
  │
  ├──► Student Management
  │       ├── Add Student
  │       ├── Search Student
  │       ├── Edit Student
  │       └── Delete Student
  │
  ├──► Room Management
  │       ├── Add Room
  │       └── View Room Status
  │
  ├──► Fee Management
  │       └── View Fee Records
  │
  └──► Complaint Management
          └── Update Complaint Status
```

---

# 🔐 Security

The project implements basic security practices including:

* Password hashing
* Session-based authentication
* Login protection
* Parameterized SQL queries
* `.gitignore` for sensitive/local files

For production use, additional security measures would be required.

---

# 🚧 Future Improvements

The following features can be added in future versions:

* [ ] Student login system
* [ ] Role-based access control
* [ ] Automatic room allocation
* [ ] Room vacating functionality
* [ ] Student complaint submission
* [ ] Add and update fee records
* [ ] Visitor management
* [ ] Email notifications
* [ ] Online fee payment
* [ ] Dashboard charts
* [ ] Student profile page
* [ ] REST API
* [ ] Cloud deployment
* [ ] Mobile application
* [ ] QR-based visitor management

---

# 🎯 Learning Objectives

This project was developed to gain practical experience with:

* Python programming
* Flask web framework
* HTML and CSS
* JavaScript
* MySQL database management
* CRUD operations
* SQL queries
* Authentication
* Backend development
* Frontend-backend communication
* Git and GitHub

---

# 📚 Concepts Demonstrated

The project demonstrates several important Computer Science concepts:

```text
Python
   ↓
Object & Data Handling
   ↓
Flask
   ↓
Routing
   ↓
HTML Forms
   ↓
CRUD Operations
   ↓
SQL
   ↓
MySQL Database
   ↓
Authentication
   ↓
Web Application
```

---

# 👨‍💻 Author

**Subhrangan Dhar**

* GitHub: [subhrangan06](https://github.com/subhrangan06)
* LinkedIn: [Subhrangan Dhar](https://www.linkedin.com/in/subhrangandhar56)

---

# 📄 License

This project is created for **educational and academic purposes**.

You are free to study, modify, and improve the project for learning purposes.

---

## ⭐ If you found this project useful

Give the repository a ⭐ on GitHub and feel free to explore or improve the project.
