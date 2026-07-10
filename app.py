from flask import Flask, render_template, request, redirect, url_for
import os

from dotenv import load_dotenv
load_dotenv()

import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

#DB connection

# db_config = {
#     "host": os.getenv("DB_HOST"),
#     "user": os.getenv("DB_USER"),
#     "password": os.getenv("DB_PASSWORD"),
#     "database": os.getenv("DB_NAME"),
#     "port": int(os.getenv("DB_PORT"))
# }

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        ssl_ca="isrgrootx1.pem"
    )
#Route

@app.route('/')
def home():
  return render_template("Register/index.html")

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM user1 WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and check_password_hash(user['password'],password):
      return redirect(url_for('task'))
    
    return "Invalid Email or Password! <a href='/login'>Try Again</a>"
  
  return render_template("Login/index.html")

@app.route('/task')
def task():
  return render_template("Task/index.html")

@app.route('/add_task', methods=['POST'])
def add_task():
  emp_name = request.form['emp_name']
  task_title = request.form['task_title']
  completed = request.form['completed']

  conn = get_db_connection()
  cursor = conn.cursor()

  try:
    query = "INSERT INTO tasks(emp_name,task_title,completed) VALUES(%s,%s,%s)"

    cursor.execute(query,(emp_name,task_title,completed))
    conn.commit()
    return 'Task Added Successfully.! <a href="/task">Go Back</a>'
  except mysql.connector.Error as err:
    return f"Error:{err.msg}. <a href='/task'>Try again</a>"
  finally:
      cursor.close()
      conn.close()



@app.route("/register",methods=['POST','GET'])
def register():
  if request.method == 'POST':
    # 1. Grab the data from the HTML form
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # 2. Hash the password
    hashed_password = generate_password_hash(password)
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
      #Insert user data into db
      query = "INSERT INTO user1(username,email,password) VALUES(%s,%s,%s)"
      cursor.execute(query,(username,email,hashed_password))
      conn.commit()
      return redirect(url_for('login'))
    except mysql.connector.Error as err:
      #Handling duplicate email
      return f"Error:{err.msg}. <a href='/'>Try again</a>"
    finally:
      cursor.close()
      conn.close()



if __name__ == "__main__":
  app.run(debug=True)
