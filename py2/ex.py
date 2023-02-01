import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import mysql.connector

#connection to db later
# def DbConnection():
#     try:
#      except:     
#gui

root= Tk()
mydb  = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="",
    database="ictprogramming"
)
# studentsid= input("Enter students id:")
# studentname= input("Enter students name:")
# Course= input("Enter students Course:")
# Fee= input("Enter students Fee:")
first_name=input("Enter students first_name:")
last_name=input("Enter students last_name:")
age=input("Enter students age: ")
Class=input("Enter students Class: ")
gender=input("Enter students gender: ")
student_image=input("Enter student_image: ")
cursor=  mydb.cursor()
cursor.execute("INSERT into student(first_name,last_name,age,class,gender,student_image) values(%s, %s,%s,%s,%s,s%s)")
mydb.commit()
cursor.execute("SELECT * FROM student")

output = cursor.fetchall()
for value in output:
    print (value)
# root.title("Student Registration System")
root.geometry("830x620")
# mt_tree= ttk.Treeview(root)
global e1
global e2
global e3
global e4

tk.Label(root, text="Students information" ,fg="black", font=(None, 30)).place(x=400, y=5)
tk.Label(root, text="Student ID").place(x=10, y=10)
tk.Label(root, text="Student name").place(x=10, y=48)
tk.Label(root, text="Course").place(x=10, y=70)
tk.Label(root, text="Fee").place(x=10, y=100)
e1=Entry(root)
e1.place(x=140, y=10)
e2=Entry(root)
e2.place(x=140, y=40)
e3=Entry(root)
e3.place(x=140, y=70)
e4=Entry(root)
e4.place(x=140, y=100)


Button(root, text="Add", command="Add", height=3, width=13,).place(x=30, y=130)
Button(root, text="Update", command="Update", height=3, width=13,).place(x=140, y=130)
Button(root, text="Delete", command="Delete", height=3, width=13,).place(x=250, y=130)
cols= ('id', 'stname', 'course', 'fee')
Listbox = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    Listbox.heading(col, text=col)
    Listbox.grid(row=1 ,column=0, columnspan=2)
    Listbox.place(x=10, y=200)

root.mainloop() 

#functions later


