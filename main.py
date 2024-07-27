from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os 

root = Tk()
root.title("Canteen Management System")
root.iconbitmap("C:\\Gautam58\\softwarecompetion\\images\\cheficon1.ico")
img = PhotoImage(file = "C:\\Gautam58\\softwarecompetion\\images\\logocanteen2.png")

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width,height,x,y))

root.config(background = "#297373")
wel_label = Label(text = "Canteen Management System",bg = "#297373",font = ('Imprint MT Shadow',28,"bold"),fg = "black")
wel_label.place(x = 13,y = 20)

bg_label = Label(root,image = img,bg = "#297373")
bg_label.place(x = 140,y = 67)

progress_label = Label(root,text = "Loading......",font = ('Imprint MT Shadow',20,"bold"),fg = "black",bg = "#297373")
progress_label.place(x = 160,y = 330)

progress = ttk.Style()
progress.theme_use("clam")
progress.configure("blue.Horizontal.TProgressbar", background = "yellow", troughcolor = "orange")


progress = Progressbar(root,orient = HORIZONTAL,length = 400,mode = "determinate",style = "blue.Horizontal.TProgressbar")
progress.place(x = 60,y = 370)

def top():
    root.withdraw()
    os.system("C:\\Gautam58\\softwarecompetion\\1s.py")
    root.destroy()

i = 0

def load():
    global i
    if i <= 100:
        txt = "Loading...."+(str(1*i)+'%')
        progress_label.config(text = txt)
        progress_label.after(30,load)
        progress['value'] = 1*i
        i += 1
    else:
        top()

load()


root.resizable(False,False)
root.mainloop()