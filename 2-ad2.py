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


       frame1=Frame(self.root,bd=4,relief=RIDGE,bg="light grey")
       frame1.place(x=300,y=50,width=1100,height=700)

       title=Label(frame1,text="ADD COMPANY",font=("times new roman",20,"bold"),bg="light grey",fg="black").place(x=100,y=50)


       fname=Label(frame1,text="COMPANY NAME",font=("times new roman",15,"bold"),bg="light grey",fg="black").place(x=100,y=125)
       self.txt_comp_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.txt_comp_name.place(x=100,y=180,width=300,height=30)

       location=Label(frame1,text="LOCATION",font=("times new roman",15,"bold"),bg="light grey",fg="black").place(x=100,y=225)
       self.txt_loc=Entry(frame1,font=("times new roman",15),bg="light gray")
       self.txt_loc.place(x=100,y=275,width=300,height=30)


       title=Label(frame1,text="REMOVE COMPANY",font=("times new roman",20,"bold"),bg="light grey",fg="black").place(x=600,y=50)

       com_name=Label(frame1,text="COMPANY NAME FOR DELETION",font=("times new roman",15,"bold"),bg="light grey",fg="black").place(x=600,y=125)
       self.com_vlu=ttk.Combobox(frame1,font=("times new roman",15),state="readonly",justify=CENTER)
       self.com_vlu["values"]=self.fetch_company()
       self.com_vlu.place(x=600,y=180,width=400) 
       self.com_vlu.current(0)
      
       
       btn_add=Button(frame1,text="ADD ",font=("times new roman",15),bg="grey",fg="white",bd=1,cursor="hand2",command=self.add).place(x=600,y=250,width=180,height=60) 
       btn_remove=Button(frame1,text="REMOVE ",font=("times new roman",15),bg="grey",fg="white",bd=1,cursor="hand2",command=self.remove).place(x=800,y=250,width=180,height=60)  

       Display_Frame=Frame(frame1,bd=4,relief=RIDGE,bg="white")
       Display_Frame.place(x=-1,y=350,width=1095,height=345)

    
       scroll_x=Scrollbar(Display_Frame,orient=HORIZONTAL) 
       scroll_y=Scrollbar(Display_Frame,orient=VERTICAL) 
       self.display_table=ttk.Treeview(Display_Frame,columns=("a","b","c"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=self.display_table.xview)
       scroll_y.config(command=self.display_table.yview)
       self.display_table.heading("a",text="COMPANY ID")
       self.display_table.heading("b",text="COMPANY NAME")
       self.display_table.heading("c",text="LOCATION")
       self.display_table['show']='headings'

       self.display_table.column("a",width=30)
       self.display_table.column("b",width=30)
       self.display_table.column("c",width=30)

       self.display_table.pack(fill=BOTH,expand=1)
       self.fetch_data()

    #    mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
    #    curser = mydb.cursor()
    #    query = "select COMPANY_ID, COMPANY_NAME, COMPANY_LOCATION  from company "
    #    curser.execute(query)
    #    rows=curser.fetchall()
    #    for i in rows :
    #        self.display_table.insert('' ,'end' ,values=i)
    #    mydb.commit()
    #    self.fetch_data()
    #    mydb.close() 

     
      #============================Condition to take values===========================================================================
    def clear(self):
        self.txt_comp_name.delete(0,END)
        self.txt_loc.delete(0,END)
        self.com_vlu.current(0)
                                          

    def add(self):
        if self.txt_comp_name.get()=="" or self.txt_loc.get()==""  :
            messagebox.showerror("Error","All Fields Are Required to add",parent=self.root)   
        elif (self.txt_comp_name.get()!="" and self.txt_loc.get()!="") and self.com_vlu.get()!="Select":
            messagebox.showerror("Error","deletion of company field not required",parent=self.root)
        else : 
            try :
              mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
              my_cursor=mydb.cursor()
              sql="insert into company (company_name,company_location) values(%s,%s)"
              val=[self.txt_comp_name.get(),self.txt_loc.get()]
              my_cursor.execute(sql,val)  
              mydb.commit()
              mydb.close()
              messagebox.showinfo("Sucess","Company Added Sucessfull",parent=self.root)
              self.clear()
              self.fetch_data()

            except Exception as e:
              messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)  

    def fetch_data(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
        curser = mydb.cursor()
        query = "select COMPANY_ID, COMPANY_NAME, COMPANY_LOCATION  from company "
        curser.execute(query)
        rows=curser.fetchall()
        self.display_table.delete(*self.display_table.get_children())
        for i in rows :
            self.display_table.insert('' ,'end' ,values=i)
        mydb.commit()
        mydb.close()

            
        
    def remove(self):
        if self.txt_comp_name.get()!="" or self.txt_loc.get()!=""  :
            messagebox.showerror("Error","You dont need to fill any of the left side blanks",parent=self.root)   
        elif self.txt_comp_name.get()=="" and self.txt_loc.get()=="" and self.com_vlu.get()=="Select":
            messagebox.showerror("Error","Please select the company to be deleated",parent=self.root)
        else : 
            try :
              mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
              my_cursor=mydb.cursor()
              query=("delete from company where company_name= %s")
              val=[self.com_vlu.get()]
              my_cursor.execute(query,(val))
              mydb.commit()
              mydb.close()
              messagebox.showinfo("Sucess","Company deleated Sucessfull",parent=self.root)
              self.fetch_data()
              self.refresh()
              self.clear()

            except Exception as e:
              messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


    def fetch_company(self):
        self.li1=['Select']
        try :
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
            my_cursor=mydb.cursor()
            my_cursor.execute("select company_name from company ")
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