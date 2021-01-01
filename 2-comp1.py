from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import mysql.connector
import os
#import register.py



class Company_sing_in:
    def __init__(self,root):
       self.root=root
       self.root.title("Company Sing_in ---(2-comp1.py)")
       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
       #================= login Frame ============================================

       frame1=Frame(self.root,bd=3,relief=RIDGE,bg="sky blue")
       frame1.place(x=520,y=140,width=500,height=550)

       title=Label(frame1,text="COMPANY SIGN IN",font=("times new roman",30,"bold"),bg="sky blue",fg="black").place(x=60,y=50)

       #===============================NAME================================================

       fname=Label(frame1,text="NAME",font=("times new roman",18,"bold"),bg="sky blue",fg="black").place(x=29,y=167)
       self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_email.place(x=160,y=165,width=250,height=40)

       #===============================Password==============================================

       password=Label(frame1,text="PASSWORD",font=("times new roman",16,"bold"),bg="sky blue",fg="black").place(x=25,y=305)
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
                
                sql1="select company_id,company_name from company"
                mycursor.execute(sql1)
                room1 =mycursor.fetchall()
                ls1=[]
                for i in range(len(room1)):
                    ls1.append(room1[i])

                if (int(self.txt_password.get()),self.txt_email.get()) not in ls1:
                    messagebox.showerror('Error',"Company doesn't exist",parent = self.root)

                try :
                    tup1=(int(self.txt_password.get()),self.txt_email.get())
                except :
                    messagebox.showerror('Error','You must have entered wrong password : \n       password must be a integer',parent = self.root)
                    self.txt_email.delete(0,END)
                    self.txt_password.delete(0,END)
                    return
                if tup1 in ls1:
                    sql2="insert into log (name_id,name) values(%s,%s)"
                    val=[int(self.txt_password.get()),self.txt_email.get()]
                    mycursor.execute(sql2,val)
                    mydb.commit()
                    mydb.close()
                    messagebox.showinfo("Sucess","ID confirmed",parent =self.root)
                    self.txt_email.delete(0,END)
                    self.txt_password.delete(0,END)
                    os.system("python 2-comp2.py")
                else :
                    messagebox.showerror("Erroe","Please enter valid information",parent =self.root)
        except Exception as e:
            messagebox.showerror("Error",f"error due to {str(e)}",parent=self.root)    


        
root=Tk()
obj=Company_sing_in(root)
root.mainloop()