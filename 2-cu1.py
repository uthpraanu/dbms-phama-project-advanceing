from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import os
#import register.py



class Register:
    def __init__(self,root):
       self.root=root
       self.root.title("Register Window")
       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
       #================= login Frame ============================================

       frame1=Frame(self.root,bg="sky blue")
       frame1.place(x=520,y=140,width=500,height=550)

       title=Label(frame1,text="SIGN IN",font=("times new roman",30,"bold"),bg="sky blue",fg="black").place(x=160,y=50)

       #===============================NAME================================================

       fname=Label(frame1,text="EMAIL",font=("times new roman",20,"bold"),bg="sky blue",fg="black").place(x=40,y=165)
       self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_email.place(x=160,y=165,width=250,height=40)

       #===============================Password==============================================

       password=Label(frame1,text="PASSWORD",font=("times new roman",15,"bold"),bg="sky blue",fg="black").place(x=30,y=305)
       self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_password.place(x=160,y=300,width=250,height=40)

       #=================================sign in button =======================================

       btn_login=Button(frame1,text="Sign in",font=("times new roman",18),bg="lightgrey",bd=1,cursor="hand2",command=self.register_data).place(x=150,y=420,width=230,height=50)

       #====================================================================================================
       
    def register_data(self):
        if (self.txt_email == "" or self.txt_password == ""):
            messagebox.showerror("Error","All Fields Are Required to add",parent=self.root)
        else :    
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
            my_cursor=mydb.cursor()  
            sql="insert into medicine (medicine_name,medicine_price,medicine_quantity,medicine_expiary) values(%s,%s,%s,%s)"
            val=[self.txt_med_name.get(),self.txt_med_price.get(),self.txt_med_quantity.get(),self.txt_med_exp.get()]
            my_cursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            messagebox.showinfo("Sucess","Medicen Added",parent=self.root)
            self.clear()
            os.system("python 2-cu2.py")
            


        

        
root=Tk()
obj=Register(root)
root.mainloop()