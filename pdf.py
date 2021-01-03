from tkinter import *
import PyPDF2
from tkinter import filedialog
from PIL import Image,ImageTk
import shutil


root = Tk()
root.title("pdf uploder ---(pdf.py)")

ig=ImageTk.PhotoImage(file="images\ic.jpg") 
       
root.iconphoto(False, ig)

filename = filedialog.askopenfilename(initialdir = r'C:\Users\Uthkarsh Gaikwad\Desktop\SIMPLE DBMS\presciption ', title = 'Upload _file',filetypes = [('pdf file','*.pdf'),('txt files','*.txt')])

print(f'see this -- {filename}')
shutil.copy(filename, 'upload files')