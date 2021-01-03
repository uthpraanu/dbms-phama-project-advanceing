from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import os
#import register.py
#import pymysql



class Choice_of_medicine:
    def __init__(self,root):
       self.root=root
       self.root.title("Choice of medicine --- (choice_of_medicine.py)")

       self.ig=ImageTk.PhotoImage(file="images\ic.jpg")
       
       self.root.iconphoto(False, self.ig) 

       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
       #================= Register Frame ============================================

       frame1=Frame(self.root,bd=2,relief=RIDGE,bg="sky blue")
       frame1.place(x=520,y=140,width=500,height=550)


       title=Label(frame1,text="Order Method",font=("times new roman",30,"bold"),bg="sky blue",fg="black").place(x=130,y=50)


        #---------------------------Button------------------------------------------------------------------------------------------------

       
       btn_register=Button(frame1,text="Upload Prescription",font=("times new roman",20),bg="grey",fg="black",bd=2,cursor="hand2",command=self.register_data).place(x=80,y=180,width=360,height=80) 

       btn_register=Button(frame1,text="Unprescriped Order",font=("times new roman",20),bg="grey",fg="black",bd=2,cursor="hand2",command=self.ad_signin_data).place(x=80,y=340,width=360,height=80) 

       


       

    def register_data(self):
        os.system('python pdf.py')
        messagebox.showinfo('Sucess','Presciption uploaded ',parent = self.root)

    def ad_signin_data(self):
        os.system('python 2-cu2.py')

                  

        
root=Tk()
obj=Choice_of_medicine(root)
root.mainloop()