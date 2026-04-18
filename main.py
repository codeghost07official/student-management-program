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
    # cursor.execute("select * from student")
    # student_data = cursor.fetchall()
    # print(tabulate(student_data, headers=["ID", "Name", "Class"], tablefmt="grid"))
    print("Record entered successfully! ")

def enter_student_record_loop(): 
    while True: 
        user_input = input("Do you want to enter student records(Y/n) = ").lower()
        if user_input != "n": 
            enter_student_records()
        else: 
            break 

def view_student_table(): 
    cursor.execute("select * from student")
    student_table = cursor.fetchall()
    print(tabulate(student_table, headers=["ID", "Name", "Class"], tablefmt="grid"))


def enter_marks(): 

    s_id = int(input("Enter Student's ID: "))
    marks = float(input("Enter marks of the student: "))
    cursor.execute("insert into marks(s_id, marks) values(%s,%s)", (s_id,marks))
    db.commit()
    print("Record Entered Successfully! ")

def view_marks_table(): 
    cursor.execute("select * from marks")
    marks_table = cursor.fetchall()
    print(tabulate(marks_table, headers=["Student-ID", "Marks"], tablefmt="grid"))

options_list = [[1, "Enter Student Records"], [2, "Enter Marks Record"], [3, "View Student's Table"], [4, "View Marks Table"]]

while True: 
    print("---------------------------------------------------------------------------------------------------------")
    print(tabulate(options_list, headers=["S.No.", "Option"], tablefmt="grid"))
    user_input = input("Select among the above options (Enter the ID of the Task you want to do) --> ").lower()
    print("To Exit, Enter 'Z' ")
    if user_input == "1": 
        enter_student_record_loop()
    elif user_input == "2": 
        enter_marks()
    elif user_input == "3": 
        view_student_table()
    elif user_input == "4": 
        view_marks_table()
    elif user_input == "z": 
        break
    else: 
        print("Incorrect Option!")
    


        
