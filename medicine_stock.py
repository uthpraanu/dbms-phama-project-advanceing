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

trv = ttk.Treeview(root ,columns=(1,2,3,4),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.config(command=trv.xview)
scroll_y.config(command=trv.yview)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

trv.heading(1 , text="Medecine_Name")
trv.heading(2 , text="Medecine_Company")
trv.heading(3 , text="Medecine_Price")
trv.heading(4 , text="Medecine_Stock")
trv['show']='headings'
trv.pack(fill=BOTH,expand=1)

query1 = "select m.medicine_name, c.company_name, m.medicine_price, s.med_quantity from medicine as m, company as c,stock as s where s.medicine_id = m.medicine_id and c.company_id = s.company_id order by c.company_name;"
curser.execute(query1)
rows=curser.fetchall()
update(rows)

root.title("My Medicine ---(78.py)")

ig=ImageTk.PhotoImage(file="images\ic.jpg")
       
root.iconphoto(False, ig)

root.geometry("800x400")
root.mainloop()
