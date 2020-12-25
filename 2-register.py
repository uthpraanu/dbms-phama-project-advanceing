from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import mysql.connector
import os



class Register:
    def __init__(self,root):
       self.root=root
       self.root.title("Register Window")
       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #================  Left Image ===============================================

       self.lf=ImageTk.PhotoImage(file="images\imj2.jpg")
       lf=Label(self.root,image=self.lf).place(x=150,y=90,width=400,height=650)

       #================= Register Frame ============================================

       frame1=Frame(self.root,bg="white")
       frame1.place(x=500,y=90,width=900,height=650)

       title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="orange").place(x=50,y=50)

        #========================row 1================================================
        
        #=====================First Method To Take Data ==================================================
    
       fname=Label(frame1,text="Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=125)
       self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_fname.place(x=100,y=180,width=250)

       lname=Label(frame1,text="Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=125)
       self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_lname.place(x=500,y=180,width=250) 

        #=========================row 2===================================================

       contact=Label(frame1,text="Contact number",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=225)
       self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_contact.place(x=100,y=275,width=250)

       email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=225)
       self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_email.place(x=500,y=275,width=250)


       #=========================row 3===================================================

       question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=325)
       self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
       self.cmb_quest["values"]=("Select","Your First pet","Your School","Your Birth Place","Your Best Friend")
       self.cmb_quest.place(x=100,y=375,width=250) 
       #self.cmb_quest.current(0)

       ans=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=325)
       self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_answer.place(x=500,y=375,width=250)
        #=========================row 4===================================================

       password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=425)
       self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_password.place(x=100,y=475,width=250)

       cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=500,y=425)
       self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_cpassword.place(x=500,y=475,width=250)

       #===========================Terms====================================

       self.var_chk=IntVar() 
       chk=Checkbutton(frame1,text="I Agree The Terms And Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=100,y=550) 

        #---------------------------Button------------------------------------------------------------------------------------------------

       #self.btn_img=ImageTk.PhotoImage(file="images\imj2.jpg") 
       btn_register=Button(frame1,text="Click Button",font=("times new roman",20),bg="grey",fg="white",bd=1,cursor="hand2",command=self.register_data).place(x=100,y=590,width=250,height=40) 

       btn_login=Button(self.root,text="Sign in",font=("times new roman",20),bg="lightgrey",bd=1,cursor="hand2",command=self.sign_in).place(x=200,y=600,width=240,height=60)

      #============================Condition to take values===========================================================================
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)   
        self.txt_cpassword.delete(0,END)                                 

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_email=="" or self.cmb_quest=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)   
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password and Conform Password Shoul Be Same",parent=self.root)
        elif self.var_chk.get()==0 :
          messagebox.showerror("Error","Please agree our Terms & Conditions",parent=self.root)
        else : 
            try :
              mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
              my_cursor=mydb.cursor()  
              sql="insert into coustomer (coustomer_name,coustomer_address,coustomer_contact,coustomer_email,coustomer_question,coustomer_answer,coustomer_password) values(%s,%s,%s,%s,%s,%s,%s)"
              val=[self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),self.txt_password.get()]
              my_cursor.execute(sql,val)
              mydb.commit()
              mydb.close()
              messagebox.showinfo("Sucess","Registration Sucessfull",parent=self.root)
              self.clear()

            except Exception as e:
                messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)
                


    def sign_in(self):
        os.system('python 2-cu1.py')
        

        
root=Tk()
obj=Register(root)
root.mainloop()