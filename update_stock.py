from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
import mysql.connector
import os



class Register:
    def __init__(self,root):
       self.root=root
       self.root.title(" UPDATE STOCK ")
       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


       frame1=Frame(self.root,bd=4,relief=RIDGE,bg="light grey")
       frame1.place(x=300,y=50,width=1100,height=700)

       title=Label(frame1,text="UPDATE STOCK",font=("times new roman",30,"bold"),bg="light grey",fg="black").place(x=400,y=30)


       medi_name=Label(frame1,text="SELECT MEDICINE HERE",font=("times new roman",20,"bold"),bg="light grey",fg="black").place(x=390,y=100)
      
       self.medi_vlu=ttk.Combobox(frame1,font=("times new roman",15),state="readonly",justify=CENTER)
       self.medi_vlu["values"]=self.fetch_company_medicine()
       self.medi_vlu.place(x=50,y=180,width=500) 
       self.medi_vlu.current(0)

       self.list_1=["Select"] 
       for i in range(10,101,10):
           self.list_1.append(i)

       self.medi_qun_vlu=ttk.Combobox(frame1,font=("times new roman",15),state="readonly",justify=CENTER)
       self.medi_qun_vlu["values"]=self.list_1
       self.medi_qun_vlu.place(x=620,y=180,width=400) 
       self.medi_qun_vlu.current(0)
      
       
       btn_add=Button(frame1,text="Remove Medicine",font=("times new roman",15),bg="grey",fg="white",bd=1,cursor="hand2",command=self.remove).place(x=200,y=250,width=300,height=60) 
       btn_remove=Button(frame1,text="ADD STOCK",font=("times new roman",15),bg="grey",fg="white",bd=1,cursor="hand2",command=self.add).place(x=600,y=250,width=300,height=60)  
    
       Display_Frame=Frame(frame1,bd=4,relief=RIDGE,bg="white")
       Display_Frame.place(x=-1,y=350,width=1095,height=345)

    
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

      #============================Condition to take values===========================================================================
   
   
   
    def clear(self):
        self.medi_vlu.current(0)
        self.medi_qun_vlu.current(0)
                                          

    def add(self):
        if  self.medi_vlu.get()=="Select" or self.medi_qun_vlu.get()=="Select"  :
            messagebox.showerror("Error","All Fields Are Required to add",parent=self.root)   
        else : 
            try :
              mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
              my_cursor=mydb.cursor()
              
              sql12="select name_id from log order by log_id desc limit 1"
              my_cursor.execute(sql12)
              rows12=my_cursor.fetchall()
              self.comp_id12=rows12[0][0]
              
              sql22="select medicine_id from medicine where medicine_name = %s"
              val22=[self.medi_vlu.get()]
              my_cursor.execute(sql22,val22)
              rows22=my_cursor.fetchall()
              self.med_id22=rows22[0][0]
              
              sql = "update stock SET med_quantity=med_quantity + %s where medicine_id = %s and company_id =%s"
              val=[self.medi_qun_vlu.get(),self.med_id22,self.comp_id12]
              my_cursor.execute(sql,val)  
              mydb.commit()
              mydb.close()
              messagebox.showinfo("Sucess","Stock updated Sucessfull",parent=self.root)
              self.clear()
              self.fetch_data()

            except Exception as e:
              messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)  

    def fetch_data(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
        curser = mydb.cursor()
        
        query3 = "select name_id from log order by log_id desc limit 1"
        curser.execute(query3)
        rows1=curser.fetchall()
        self.comp_id=rows1[0][0]
        
        query = '''select c.company_name, m.medicine_name, s.med_quantity from company as c, medicine as m, stock as s
                    where s.medicine_id = m.medicine_id and s.company_id = %s and c.company_id = %s'''
        curser.execute(query,[self.comp_id,self.comp_id])
        rows=curser.fetchall()
        self.display_table.delete(*self.display_table.get_children())
        for i in rows :
            self.display_table.insert('' ,'end' ,values=i)
        mydb.commit()
        mydb.close()

            
        
    def remove(self):
            try :
              mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
              my_cursor=mydb.cursor()
              sql12="select name_id from log order by log_id desc limit 1"
              my_cursor.execute(sql12)
              rows12=my_cursor.fetchall()
              self.comp_id12=rows12[0][0]
              
              sql22="select medicine_id from medicine where medicine_name = %s"
              val22=[self.medi_vlu.get()]
              my_cursor.execute(sql22,val22)
              rows22=my_cursor.fetchall()
              self.med_id22=rows22[0][0]

              sql123="select med_quantity from stock where medicine_id = %s and company_id = %s "
              val123=[self.med_id22,self.comp_id12]
              my_cursor.execute(sql123,val123)
              rows123=my_cursor.fetchall()
              self.med_rel_quantity=rows123[0][0]

              if (int(self.medi_qun_vlu.get()) <= self.med_rel_quantity ):
                sql = "update stock SET med_quantity=med_quantity - %s where medicine_id = %s and company_id =%s"
                val=[self.medi_qun_vlu.get(),self.med_id22,self.comp_id12]
                my_cursor.execute(sql,val)  
                mydb.commit()
                mydb.close()
               
                messagebox.showinfo("Sucess","Medicine removed Sucessfull",parent=self.root)
               
                self.clear()
                self.fetch_data()
              else :
                  messagebox.showerror("Error",f"Error due to : medicine remove value exceeds quantity",parent=self.root)

            except Exception as e:
              messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


    def fetch_company_medicine(self):
        self.li1=['Select']
        try :
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
            my_cursor=mydb.cursor()
            q1 = ('select medicine_name from medicine where medicine_id in (select medicine_id from stock where company_id = %s)')
            my_cursor.execute(q1,[1])
            row1=my_cursor.fetchall()
            for i in range(0, len(row1)):
                self.li1.append(row1[i][0])
            mydb.commit()
            mydb.close()
            return self.li1

        except Exception as e:
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


    def refresh(self):
        self.com_vlu["values"]=self.fetch_company()


        
root=Tk()
obj=Register(root)
root.mainloop()