from tkinter import *
import PyPDF2
from tkinter import filedialog
from PIL import Image,ImageTk


root = Tk()
root.title("pdf uploder ---(pdf.py)")

ig=ImageTk.PhotoImage(file="images\ic.jpg") 
       
root.iconphoto(False, ig)

root.filename = filedialog.askopenfilename(initialdir = r'C:\Users\Uthkarsh Gaikwad\Desktop\Exrernal Dbms Project\presciption ',title = 'Upload _file',filetypes = [('pdf file','*.pdf'),('txt files','*.txt')])
my_label = Label(root ,pdf = root.filename).pack
'''if root.filename:
    pdf_file = PyPDF2.PdfFileReader(root.filename)
    page = pdf_file.getPage(0)
    txt = page.extractText()'''


root.geometry("800x400")
root.mainloop()