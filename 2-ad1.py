from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import os
#import register.py



class Admin_sing_in:
    def __init__(self,root):
       self.root=root
       self.root.title("Admin_sing_in ---2ad1.py")
       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
       #================= login Frame ============================================

       frame1=Frame(self.root,bg="sky blue")
       frame1.place(x=520,y=140,width=500,height=550)

       title=Label(frame1,text="ADMIN SIGN IN",font=("times new roman",30,"bold"),bg="sky blue",fg="black").place(x=100,y=50)

       #===============================NAME================================================

       fname=Label(frame1,text="USER ID",font=("times new roman",17,"bold"),bg="sky blue",fg="black").place(x=40,y=165)
       self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_email.place(x=160,y=165,width=250,height=40)

       #===============================Password==============================================

       password=Label(frame1,text="PASSWORD",font=("times new roman",17,"bold"),bg="sky blue",fg="black").place(x=28,y=305)
       self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_password.place(x=160,y=300,width=250,height=40)

       #=================================sign in button =======================================

       btn_login=Button(frame1,text="Sign in",font=("times new roman",18),bg="lightgrey",bd=1,cursor="hand2",command=self.register_data).place(x=150,y=420,width=230,height=50)

       #====================================================================================================
       
    def register_data(self):
        os.system("python 2-ad2.py")
            


        

        
root=Tk()
obj=Admin_sing_in(root)
root.mainloop()