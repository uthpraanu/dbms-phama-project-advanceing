from tkinter import *
from tkinter import Tk,ttk
from PIL import Image, ImageTk
import os
import mysql.connector

class Company_Page:
    def __init__(self,root):
        self.root = root 
        self.root.title(" Company_Page ---(2-comp2.py) ")
        self.root.geometry("2000x800+0+0")
        self.root.config(bg="white")

        # ----- Background Image --------------------------------------------------------

        self.bg_image = ImageTk.PhotoImage(file="images\Imj1.jpg") 
        bg = Label(self.root,image=self.bg_image).place(x=0,y=0,relwidth=1,relheight=1)

        
        #-------- FRAME 1 --------------------------------------------------------------------

        frame1 = Frame(self.root, bd = 2, relief = RIDGE, bg = "light blue")
        frame1.place(x= 120, y= 100, width =380 , height = 550)

        label_f1 = Label(frame1, text=" Choose Your Option", font = ("NEW TIMES ROMAN", 25, "bold"),bg = "light blue",fg ="black").place(x=25, y=32)

        #--------- button --------------
        
        self.bt1 = Button(frame1 ,text="Add new Medicine",font=("TIMES NEW ROMAN", 22 ,"bold"),bg="grey",fg="black",cursor="hand2",command=self.new).place(x=50 ,y=150, height = 70 ,width = 280)
        
        self.bt2 = Button(frame1 ,text="Increase Stock",font=("TIMES NEW ROMAN", 22 ,"bold"),bg="grey",fg="black",cursor="hand2",command=self.existing).place(x=50 ,y=270, height = 70 ,width = 280)

        self.bt3 = Button(frame1 ,text="Requested Medicine",font=("TIMES NEW ROMAN", 22 ,"bold"),bg="grey",fg="black",cursor="hand2",command=self.request).place(x=50 ,y=390, height = 70 ,width = 280)


        #--------------------frame 2 -----------------------------------------------------------

        frame2 = Frame(self.root, bd = 2, relief = RIDGE, bg = "light blue")
        frame2.place(x= 540, y= 100, width =880 , height = 550)

        label_f2 = Label(frame2, text=" Your Stock", font = ("NEW TIMES ROMAN", 25, "bold"),bg = "light blue",fg ="black").place(x=350, y=32)


        
        Display_Frame=Frame(frame2,bd=4,relief=RIDGE,bg="white")
        Display_Frame.place(x=-1,y=120,width=877,height=427)

    
        scroll_x=Scrollbar(Display_Frame,orient=HORIZONTAL) 
        scroll_y=Scrollbar(Display_Frame,orient=VERTICAL) 
        self.display_table=ttk.Treeview(Display_Frame,columns=("a","b","c"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.display_table.xview)
        scroll_y.config(command=self.display_table.yview)
        self.display_table.heading("a",text="COMPANY NAME")
        self.display_table.heading("b",text="MEDICINE NAME")
        self.display_table.heading("c",text="QUANTITY")
        self.display_table['show']='headings'

        self.display_table.column("a",width=30)
        self.display_table.column("b",width=30)
        self.display_table.column("c",width=30)

        self.display_table.pack(fill=BOTH,expand=1)
        self.fetch_data()





    def new(self):
        os.system("python add_new_medicine.py")
        self.fetch_data()
    def existing(self):
        os.system("python increase_stock.py")
        self.fetch_data()
    def request(self):
        os.system("python requested_medicine.py")
        self.fetch_data()

    def fetch_data(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
        curser = mydb.cursor()
        query3 = "select name_id from log order by log_id desc limit 1"
        curser.execute(query3)
        rows1=curser.fetchall()
        self.comp_id=int(rows1[0][0])
        query = '''select c.company_name, m.medicine_name, s.med_quantity from company as c, medicine as m, stock as s
                    where s.medicine_id = m.medicine_id and s.company_id = %s and c.company_id = %s'''
        curser.execute(query,[self.comp_id,self.comp_id])
        rows=curser.fetchall()
        self.display_table.delete(*self.display_table.get_children())
        for i in rows :
            self.display_table.insert('' ,'end' ,values=i)
        mydb.commit()
        mydb.close()




    def refresh(self):
        self.com_vlu["values"]=self.fetch_company()






root = Tk()
obj = Company_Page(root)
root.mainloop()