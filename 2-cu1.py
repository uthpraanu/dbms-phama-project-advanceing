from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import mysql.connector
import os

class Customer_sign_in:
    def __init__(self,root):
       self.root=root
       self.root.title("Customer Sign_in ---(2-cu1.py)")
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
        try:
            if (self.txt_email.get() == "" or self.txt_password.get() == ""):
                messagebox.showerror("Error","You left the box empty",parent=self.root)
            else :
                mydb = mysql.connector.connect(host = "localhost", user = "root", password = "123456789", database = "testdb")
                mycursor = mydb.cursor()
                
                sql1="select customer_id,customer_email,customer_name from customer where customer_email = %s"
                mycursor.execute(sql1,[self.txt_email.get()])
                room1 =mycursor.fetchall()
                ls1=[]
                for i in range(len(room1)):
                    ls1.append(room1[i])


                sql123="select customer_email,customer_password from customer"
                mycursor.execute(sql123)
                room123 =mycursor.fetchall()
                ls123=[]
                for i in range(len(room123)):
                    ls123.append(room123[i])

                if (self.txt_email.get(),self.txt_password.get()) not in ls123:
                    messagebox.showerror('Error',"Crendentials doesn't exist",parent = self.root)
                    
                tup1=(self.txt_email.get(),self.txt_password.get())
                
                if tup1 in ls123:
                    sql2="insert into customer_log (customer_id,customer_email,customer_name) values(%s,%s,%s)"
                    mycursor.execute(sql2,ls1[0])
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Sucess","ID confirmed",parent =self.root)
                    self.txt_email.delete(0,END)
                    self.txt_password.delete(0,END)
                    os.system("python 2-cu2.py")
                else :
                    messagebox.showerror("Erroe","Please enter valid information",parent =self.root)
        except Exception as e:
            messagebox.showerror("Error",f"error due to {str(e)}",parent=self.root) 
            


        

        
root=Tk()
obj=Customer_sign_in(root)
root.mainloop()