# 📋 Task Management System

A simple **Task Management System** built using **Flask, MySQL, HTML, and CSS**. The application allows users to register, log in securely, and manage employee tasks.

## 🚀 Features

- 👤 User Registration
- 🔐 Secure Login with Password Hashing
- 📝 Add Employee Tasks
- 📌 Select Task Title from Dropdown
- ✅ Mark Task Status (Completed: True/False)
- 💾 Store User and Task Data in MySQL
- 🎨 Simple and Responsive User Interface
# Name : Nigam Prasad Lenka
# Application no : IN26011682
---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3 (Inline Styling)

### Backend
- Python
- Flask

### Database
- MySQL

### Libraries Used

- Flask
- mysql-connector-python
- Werkzeug

---

## 📂 Project Structure

```
TaskManagement/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── Register/
│   │      index.html
│   │
│   ├── Login/
│   │      index.html
│   │
│   └── Task/
│          index.html
│
└── README.md
```

---

## 🗄️ Database Schema

### User Table

| Column | Type |
|----------|----------|
| id | INT (Primary Key) |
| username | VARCHAR(100) |
| email | VARCHAR(100) |
| password | VARCHAR(255) |

### Task Table

| Column | Type |
|----------|----------|
| id | INT (Primary Key) |
| emp_name | VARCHAR(100) |
| task_title | VARCHAR(100) |
| completed | BOOLEAN |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/TaskManagement.git
```

### Move into the project

```bash
cd TaskManagement
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configure MySQL

Create a database named:

```sql
CREATE DATABASE user_db;
```

Create the following tables.

### User Table

```sql
CREATE TABLE user1(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
```

### Task Table

```sql
CREATE TABLE tasks(
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100),
    task_title VARCHAR(100),
    completed BOOLEAN
);
```

Update the MySQL configuration inside **app.py**.

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "user_db",
    "port": 3306
}
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📸 Application Workflow

1. Register a new user.
2. Login using registered credentials.
3. Enter Employee Name.
4. Select Task Title.
5. Choose Task Completion Status.
6. Save the task to the MySQL database.

---

## 🔒 Security

- Passwords are securely stored using **Werkzeug Password Hashing**.
- Duplicate email registration is prevented using a **UNIQUE** constraint.

---

## 📌 Future Improvements

- Edit Task
- Delete Task
- Task Search
- Task Filters
- User Sessions
- Logout Functionality
- Dashboard with Task Statistics
- Responsive UI using Bootstrap

---

## 👨‍💻 Author

**Ashish Modhawala**

B.Tech CSE Student

---

## 📜 License

This project is developed for educational and learning purposes.
