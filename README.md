# 🚀 Employee Task Manager

A lightweight **Employee Task Management** web application developed using **Flask** and **MySQL**. It provides a secure authentication system and enables users to create and manage employee tasks through an intuitive interface.

---

## ✨ Highlights

- 🔑 User Registration & Authentication
- 🔒 Password Encryption using Werkzeug
- 📋 Create Employee Tasks
- 📂 Predefined Task Categories
- ✔️ Track Task Completion Status
- 💽 MySQL Database Integration
- 🎨 Clean and User-Friendly Interface

---

## 👨‍💻 Developer

**Name:** Nigam Prasad Lenka

**Application No:** IN26011682

---

# 🛠 Technology Stack

## Frontend
- HTML5
- CSS3

## Backend
- Python
- Flask

## Database
- MySQL

## Python Packages

- Flask
- mysql-connector-python
- Werkzeug

---

# 📁 Project Directory

```text
TaskManagement/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── Register/
│   │   └── index.html
│   ├── Login/
│   │   └── index.html
│   └── Task/
│       └── index.html
│
└── README.md
```

---

# 🗃 Database Design

## users

| Field | Data Type |
|------|-----------|
| id | INT (PK) |
| username | VARCHAR(100) |
| email | VARCHAR(100) |
| password | VARCHAR(255) |

### Description

Stores all registered user credentials securely.

---

## tasks

| Field | Data Type |
|------|-----------|
| id | INT (PK) |
| emp_name | VARCHAR(100) |
| task_title | VARCHAR(100) |
| completed | BOOLEAN |

### Description

Maintains employee task information and completion status.

---

# ⚙️ Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/your-username/TaskManagement.git
```

## 2. Navigate into Project

```bash
cd TaskManagement
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# 🛢 Database Configuration

Create a MySQL database.

```sql
CREATE DATABASE user_db;
```

### Create User Table

```sql
CREATE TABLE user1(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
```

### Create Task Table

```sql
CREATE TABLE tasks(
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100),
    task_title VARCHAR(100),
    completed BOOLEAN
);
```

Update the database credentials in **app.py**

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

# ▶️ Launch Application

Run the Flask application.

```bash
python app.py
```

Visit the application in your browser.

```
http://127.0.0.1:5000
```

---

# 🔄 Application Flow

```text
Register
     │
     ▼
Login
     │
     ▼
Add Employee Details
     │
     ▼
Select Task
     │
     ▼
Choose Status
     │
     ▼
Save to Database
```

---

# 🔐 Security Features

- Password hashing with Werkzeug
- Unique email validation
- MySQL-based data storage
- Secure authentication process

---

# 🌱 Possible Enhancements

- ✏️ Update Existing Tasks
- ❌ Delete Tasks
- 🔍 Search Functionality
- 📊 Dashboard & Analytics
- 👤 User Profiles
- 🔓 Logout System
- 📱 Bootstrap Responsive UI
- 📅 Task Due Dates

---

# 📄 License

This project is developed for educational and learning purposes.
