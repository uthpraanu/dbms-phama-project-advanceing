from tkinter import*
from tkinter import ttk,messagebox
import tkinter.ttk as ttk
from PIL import Image,ImageTk
import pymysql
import mysql.connector
import os
from datetime import date 
#import register.py



class Customer_window:
    def __init__(self,root):
       self.root=root
       self.root.title("customer Window ---(2-cu2.py)")
       self.root.geometry("2000x800+0+0")
       self.root.config(bg="white")# WINDOW COLOUR
       #================   Big Image ===============================================

       self.bg=ImageTk.PhotoImage(file="images\Imj1.jpg")
       bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        
       #================= order frame ============================================

       frame1=Frame(self.root,bd=4,relief=RIDGE,bg="sky blue")
       frame1.place(x=120,y=80,width=1350,height=650)

       title=Label(frame1,text="ADD ORDERS",font=("times new roman",30,"bold"),bg="sky blue",fg="black").place(x=95,y=20)

        #================= ORDER (Id) TO DELETE frame============================================

       frame2=Frame(self.root,bd=4,relief=RIDGE,bg="light grey")
       frame2.place(x=580,y=105,width=850,height=600)

       title=Label(frame2,text="ORDER (Id) TO DELETE",font=("times new roman",30,"bold"),bg="light grey",fg="black").place(x=200,y=10)

       #=================================place order button =======================================

       place_order=Button(frame1,text=" Place Order",font=("times new roman",18),bg="lightgrey",bd=1,cursor="hand2",command=self.order_it).place(x=40,y=540,width=150,height=80)


       #=================================view order button =======================================

       delete_order=Button(frame1,text="Medicine price",font=("times new roman",18),bg="lightgrey",bd=1,cursor="hand2",command=self.med_it).place(x=250,y=540,width=180,height=80)


       #=============================== Frame 3 and Medicen name Buttons/combobox =====================================================
       frame3=Frame(self.root,bd=4,relief=RIDGE,bg="light grey")
       frame3.place(x=155,y=180,width=400,height=400)

       title=Label(frame3,text="MEDICIN NAME ",font=("times new roman",18,"bold"),bg="light grey",fg="black").place(x=60,y=15)

       self.li_med=["Select"]

       mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
       curser = mydb.cursor()
       query = "select medicine_name from medicine "
       curser.execute(query)
       rows2=curser.fetchall()
       for i in range(0, len(rows2)):
           self.li_med.append(rows2[i][0])

       self.medicen_name=ttk.Combobox(frame3,font=("times new roman",14),state="readonly")
       self.medicen_name['values']=self.li_med
       self.medicen_name.place(x=10,y=75,width=370,height=35)
       self.medicen_name.current(0)

        #================================ Company name buttton =======================================================================

       title=Label(frame3,text="MEDICIN COMPANY",font=("times new roman",18,"bold"),bg="light grey",fg="black").place(x=60,y=150)

       self.li_comp=["Select"]
       mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
       curser = mydb.cursor()
       query = "select company_name from company "
       curser.execute(query)
       rows1=curser.fetchall()
       for i in range(0, len(rows1)):
           self.li_comp.append(rows1[i][0])

       self.medicen_company=ttk.Combobox(frame3,font=("times new roman",14),state="readonly")
       self.medicen_company['values']=self.li_comp
       self.medicen_company.place(x=10,y=210,width=370,height=35)
       self.medicen_company.current(0)

        #================================= QUANTITY ===================================================================================

       title=Label(frame3,text="QUANTITY",font=("times new roman",18,"bold"),bg="light grey",fg="black").place(x=120,y=285)

       self.list_1=["Select"] 
       for i in range(10,101,10):
           self.list_1.append(i)

       self.medicen_quantityy=ttk.Combobox(frame3,font=("times new roman",14),state="readonly")
       self.medicen_quantityy['values']=self.list_1
       self.medicen_quantityy.place(x=10,y=345,width=370,height=35)
       self.medicen_quantityy.current(0)

       #=================================delete order button =======================================
      
       self.order_id=ttk.Combobox(frame2,font=("times new roman",14),state="readonly")
       self.li_delete=["Select"]
       mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
       curser = mydb.cursor()
       query = "select order_id from orders "
       curser.execute(query)
       rows1=curser.fetchall()
       for i in range(0, len(rows1)):
           self.li_delete.append(rows1[i][0])
       self.order_id['values']=self.li_delete
       self.order_id.place(x=15,y=90,width=370,height=35)
       self.order_id.current(0)

       view_order=Button(frame2,text="Delete order",font=("times new roman",18),bg="sky blue",bd=1,cursor="hand2",command=self.delete_it).place(x=470,y=85,width=300,height=50)


       #===================================== Display Frame ==============================================================

       self.Display_Frame=Frame(frame2,bd=4,relief=RIDGE,bg="white")
       self.Display_Frame.place(x=0,y=150,width=842,height=441)
 
       scroll_x=Scrollbar(self.Display_Frame,orient=HORIZONTAL) 
       scroll_y=Scrollbar(self.Display_Frame,orient=VERTICAL) 
       self.display_table=ttk.Treeview(self.Display_Frame,columns=("a","b","c","d","e","f"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)
       scroll_x.config(command=self.display_table.xview)
       scroll_y.config(command=self.display_table.yview)
       self.display_table.heading("a",text="order_id")
       self.display_table.heading("b",text="medecine_name")
       self.display_table.heading("c",text="medecine_company")
       self.display_table.heading("d",text="medecine_quantity")
       self.display_table.heading("e",text="medecine_price_per_packet")
       self.display_table.heading("f",text="order_date")
       self.display_table['show']='headings'

       self.display_table.column("a",width=50)
       self.display_table.column("b",width=100)
       self.display_table.column("c",width=100)
       self.display_table.column("d",width=50)
       self.display_table.column("e",width=100)
       self.display_table.column("f",width=50)
       self.display_table.pack(fill=BOTH,expand=1)
       self.refresh()


    def refresh(self):
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
            curser = mydb.cursor()
            query = "create view your_order as select order_id,medicine_name,company_name,quantity,medicine_price as medicinr_price_per_packet,order_date from company,medicine,orders where MEDICINE_ID=med_id and COMPANY_ID=com_id "
            curser.execute(query)
            query ="select * from your_order "
            curser.execute(query)
            rows=curser.fetchall()
            self.display_table.delete(*self.display_table.get_children())
            for i in rows :
                self.display_table.insert('' ,'end' ,values=i)
            query="drop view your_order ; "    
            curser.execute(query) 
            mydb.commit()
            mydb.close()
        except mysql.connector.errors.ProgrammingError :
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
            curser = mydb.cursor()   
            query="drop view your_order ; "    
            curser.execute(query)
            mydb.commit()
            mydb.close()
            self.refresh() 
        except Exception as e :
            messagebox.showerror("Error",f"Error due to : {str(e)}",parent = self.root)

       
       

    def order_it(self):
        if self.medicen_company.get()=="Select" or self.medicen_name.get()=="Select" or self.medicen_quantityy.get()=="Select" :
            messagebox.showerror("Error","Please fill all the fields ",parent=self.root)
        else :
            try :
                mydb=mysql.connector.connect(host="localhost", user="root", password="123456789", database = "testdb")
                curser=mydb.cursor()
                query = ("select company_id from company where company_name = %s")
                valu=[self.medicen_company.get()]
                curser.execute(query,(valu))
                self.comp_id=curser.fetchall()
                self.comp_id = self.comp_id[0][0]
                query = ("select medicine_id from medicine where medicine_name = %s")
                valu=[self.medicen_name.get()]
                curser.execute(query,(valu))
                self.medi_id=curser.fetchall()
                self.medi_id = self.medi_id[0][0]

                self.today = str(date.today())
                curser.execute("insert into orders (com_id, med_id, order_date, quantity) values(%s,%s,%s,%s)",(self.comp_id,self.medi_id,self.today,self.medicen_quantityy.get()))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Sucess", "Your order has been registered ")
                self.refresh()
                self.refresh2()
                self.medicen_name.current(0)
                self.medicen_company.current(0)
                self.medicen_quantityy.current(0)
            except Exception as e :
                messagebox.showerror("Error", f'error due to : {str(e)}', parent=self.root)


    def med_it(self):
        os.system("python 78.py")
        
        
    def delete_it(self):
        if self.order_id.get()=="Select" :
            messagebox.showerror("Error","Please select the company",parent=self.root)
        else :
            try :
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="testdb")
                curser=mydb.cursor()
                query="delete from orders where order_id = %s"
                val=[self.order_id.get()]
                curser.execute(query,val)
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Sucess", "Your order has been deleted ")
                self.refresh()
                self.refresh2()
                self.order_id.current(0)
            except Exception as e :
                messagebox.showerror("Error",f"Error : {str(e)}",parent=self.root)
        
    def refresh2(self) :
       self.li_delete.clear()
       self.li_delete=["Select"]
       mydb=mysql.connector.connect(host="localhost",user="root",password="123456789", database = "testdb")
       curser = mydb.cursor()
       query = "select order_id from orders "
       curser.execute(query)
       rows1=curser.fetchall()
       for i in range(0, len(rows1)):
           self.li_delete.append(rows1[i][0])
       self.order_id['values']=self.li_delete


        

        
root=Tk()
obj=Customer_window(root)
root.mainloop()