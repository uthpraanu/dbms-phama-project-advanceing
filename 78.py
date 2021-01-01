from tkinter import *
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows :
        trv.insert('' ,'end' ,values=i)

mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
curser = mydb.cursor()


root = Tk()

trv = ttk.Treeview(root ,columns=(1,2) ,show = "headings" , height = "6")
trv.pack()

trv.heading(1 , text="Medecine_Name")
trv.heading(2 , text="Medecine_Price")

query1 = "select medicine_name,medicine_price from medicine "
curser.execute(query1)
rows=curser.fetchall()
update(rows)

root.title("My Medicine ---(78.py)")
root.geometry("500x500")
root.mainloop()
