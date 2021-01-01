from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import os
#import register.py
#import pymysql



class First_page:
    def __init__(self,root):
       self.root=root
       self.root.title("E - PHARMA --- (2-firstpage.py)")
       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
       #================= Register Frame ============================================

       frame1=Frame(self.root,bd=2,relief=RIDGE,bg="sky blue")
       frame1.place(x=520,y=140,width=500,height=550)


       title=Label(frame1,text="LOGIN AS",font=("times new roman",30,"bold"),bg="sky blue",fg="black").place(x=150,y=50)


        #---------------------------Button------------------------------------------------------------------------------------------------

       
       btn_register=Button(frame1,text="Admin",font=("times new roman",20),bg="grey",fg="white",bd=2,cursor="hand2",command=self.ad_signin_data).place(x=130,y=370,width=250,height=40) 

       btn_register=Button(frame1,text="Customer",font=("times new roman",20),bg="grey",fg="white",bd=2,cursor="hand2",command=self.register_data).place(x=130,y=270,width=250,height=40)

       btn_register=Button(frame1,text="Company",font=("times new roman",20),bg="grey",fg="white",bd=2,cursor="hand2",command=self.c_signin_data).place(x=130,y=170,width=250,height=40)


       

    def register_data(self):
         os.system('python 2-register.py')

    def ad_signin_data(self):
        os.system('python 2-ad1.py')

    def c_signin_data(self):
       os.system('python 2-comp1.py')

            


        

        
root=Tk()
obj=First_page(root)
root.mainloop()