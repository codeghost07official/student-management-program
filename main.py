import mysql.connector 
from tabulate import tabulate
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=3306
)

cursor = db.cursor()

def enter_student_records():
    name = input("Enter student's name: ") 
    s_class = input("Enter student's class: ")
    cursor.execute("insert into student(name, class) values(%s,%s)", (name, s_class))
    db.commit()
    cursor.execute("select * from student")
    student_data = cursor.fetchall()
    print(tabulate(student_data, headers=["ID", "Name", "Class"], tablefmt="grid"))
    print("Record entered successfully! ")

def enter_student_record_loop(): 
    while True: 
        user_input = input("Do you want to enter student records(Y/n) = ").lower()
        if user_input != "n": 
            enter_student_records()
        else: 
            break 

enter_student_record_loop()


        
