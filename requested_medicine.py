from tkinter import *
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows :
        trv.insert('' ,'end' ,values=i)

mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
curser = mydb.cursor()


root = Tk()

scroll_x=Scrollbar(root,orient=HORIZONTAL) 
scroll_y=Scrollbar(root,orient=VERTICAL) 
trv = ttk.Treeview(root ,columns=(1) ,show = "headings" , height = "6")
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=trv.xview)
scroll_y.config(command=trv.yview)

trv.heading(1 , text="Medecine_Name")
trv['show']='headings'

trv.column(1,width=30)

trv.pack(fill=BOTH,expand=1)

query1 = "select medicine_name from medicine "
curser.execute(query1)
rows=curser.fetchall()
update(rows)

root.title("Requested Medicine ---(requested_medicine.p)")
ig=ImageTk.PhotoImage(file="images\ic.jpg")
       
root.iconphoto(False, ig)

ig=ImageTk.PhotoImage(file="images\ic.jpg")
       
root.iconphoto(False, ig)

root.geometry("500x300")
root.mainloop()
