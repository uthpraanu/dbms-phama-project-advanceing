import mysql.connector
import tkinter  as tk 
import pymysql
from tkinter import *
from PIL import Image,ImageTk

my_w = tk.Tk()
ig=ImageTk.PhotoImage(file="images\ic.jpg")
       
root.iconphoto(False, ig)
my_w.geometry("400x250") 
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="123456789",
  database="testdb"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM medicine ")
i=0 
for student in my_conn: 
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1
my_w.mainloop()