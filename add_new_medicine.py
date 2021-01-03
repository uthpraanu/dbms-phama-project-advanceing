from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import mysql.connector
import os



class Add_new_medicine:
    def __init__(self,root):
       self.root=root
       self.root.title("Add New Medicine")

       self.ig=ImageTk.PhotoImage(file="images\ic.jpg")
       
       self.root.iconphoto(False, self.ig) 

       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       #================= Register Frame ============================================

       frame1=Frame(self.root,bd=3,relief=RIDGE,bg="light grey")
       frame1.place(x=450,y=90,width=560,height=650)


       title=Label(frame1,text="ADD MEDICEN HERE",font=("times new roman",30,"bold"),bg="light grey",fg="black").place(x=70,y=40)

       

    
       med_name=Label(frame1,text="MEDICEN NAME",font=("times new roman",16,"bold"),bg="light grey",fg="black").place(x=180,y=125)
       self.txt_med_name=Entry(frame1,font=("times new roman",15),bg="white")
       self.txt_med_name.place(x=120,y=180,width=300)
       

        
        #-----------------------------------------

       comp_id=Label(frame1,text="MEDICEN QUANTITY",font=("times new roman",15,"bold"),bg="light grey",fg="black").place(x=170,y=240)
       self.txt_med_quantity=Entry(frame1,font=("times new roman",15),bg="white")
       self.txt_med_quantity.place(x=120,y=285,width=300) 
       

        #=========================row 2===================================================

       manu=Label(frame1,text="PRICE PER PACKET",font=("times new roman",15,"bold"),bg="light grey",fg="black").place(x=165,y=345)
       self.txt_med_price=Entry(frame1,font=("times new roman",15),bg="white")
       self.txt_med_price.place(x=120,y=390,width=300)
       

       exp=Label(frame1,text="DATE OF EXPIRY",font=("times new roman",15,"bold"),bg="light grey",fg="black").place(x=180,y=450)
       self.txt_med_exp=Entry(frame1,font=("times new roman",15),bg="white")
       self.txt_med_exp.place(x=120,y=495,width=300)


        #---------------------------Button------------------------------------------------------------------------------------------------

       btn_register=Button(frame1,text="ADD",font=("times new roman",20),bg="grey",fg="white",bd=1,cursor="hand2",command=self.register_data).place(x=135,y=570,width=250,height=45) 

      #============================Condition to take values===========================================================================
    def clear(self):
        self.txt_med_name.delete(0,END)
        self.txt_med_quantity.delete(0,END)
        self.txt_med_price.delete(0,END)
        self.txt_med_exp.delete(0,END)                                   

    def register_data(self):
        x=self.txt_med_exp.get()
        if self.txt_med_exp.get()=="" or self.txt_med_name=="" or self.txt_med_price.get()=="" or self.txt_med_quantity.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)  
        elif x[4]!="-" or x[7]!="-" :
            messagebox.showerror("Error","Correct Format Required as YYYY-MM-DD",parent=self.root) 
        else : 
            try :
              mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
              my_cursor=mydb.cursor()  

              self.table = []
              sql92211 = 'select medicine_name from medicine '
              my_cursor.execute(sql92211)
              rows95111 = my_cursor.fetchall()
              for i in range(len(rows95111)):
                self.table.append(rows95111[i][0])


              if self.txt_med_name.get() in self.table :
                sql44 = 'select name_id from log order by log_id desc limit 1'
                my_cursor.execute(sql44)              
                row147 = my_cursor.fetchall()
                self.rows147 = row147[0][0]

                sql4455 = 'select medicine_id from medicine where medicine_name = %s'
                my_cursor.execute(sql4455,[self.txt_med_name.get()])              
                row14755 = my_cursor.fetchall()
                self.rows14755 = row14755[0][0]

                self.lst = []
                sql922 = 'select m.medicine_name from medicine as m, stock as s where s.company_id = %s and m.medicine_id = s.medicine_id '
                my_cursor.execute(sql922,[self.rows147])
                rows951 = my_cursor.fetchall()
                for i in range(len(rows951)):
                    self.lst.append(rows951[i][0])


                if self.txt_med_name.get() not in self.lst:
                    squery = "insert into stock (company_id,medicine_id,med_quantity) values (%s,%s,%s) "
                    my_cursor.execute(squery,[self.rows147,self.rows14755,self.txt_med_quantity.get()])
                    mydb.commit()
                    self.clear()
                    messagebox.showinfo("Sucess","Medicen Added",parent=self.root)
                    return
                else :
                    messagebox.showerror("Error","Medicine already exists",parent=self.root)

            
              else :  
                sql="insert into medicine (medicine_name,medicine_price,medicine_quantity,medicine_expiary) values(%s,%s,%s,%s)"
                val=[self.txt_med_name.get(),self.txt_med_price.get(),self.txt_med_quantity.get(),self.txt_med_exp.get()]
                my_cursor.execute(sql,val)
                mydb.commit()

                sql44 = 'select name_id from log order by log_id desc limit 1'
                my_cursor.execute(sql44)              
                row147 = my_cursor.fetchall()
                self.rows147 = row147[0][0]

                sql44 = 'select medicine_id from medicine order by medicine_id desc limit 1'
                my_cursor.execute(sql44)              
                row147 = my_cursor.fetchall()
                self.rows1471 = row147[0][0]

                sql14587 = "insert into stock values(%s,%s,%s)"
                my_cursor.execute(sql14587,[self.rows147,self.rows1471,self.txt_med_quantity.get()])
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Sucess","Medicen Added",parent=self.root)
                self.clear()

            except Exception as e:
               messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)
        
        
        

        
root=Tk()
obj=Add_new_medicine(root)
root.mainloop()