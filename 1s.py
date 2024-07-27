import customtkinter as ct 
from tkinter import *
from PIL import Image
import os


root = ct.CTk()
root.title("FLAMES")
root.config(bg = "white")
root.resizable(False,False)

x = (root.winfo_screenwidth())
y = (root.winfo_screenheight())
root.geometry('{}x{}+{}+{}'.format(x,y,-7,-3))
#root.geometry("1920x1080")

headFrm = ct.CTkFrame(root,height = 115,fg_color = "#297373",bg_color = "#297373")
headFrm.pack(fill = "x")


flame = Image.open("C:\\Gautam58\\softwarecompetion\\images\\flame.png")
flameimg = ct.CTkImage(flame,size = (200,200))
logo = ct.CTkLabel(headFrm,image = flameimg,text = None)
logo.place(x = 170,y = -25)

pan = Image.open("C:\\Gautam58\\softwarecompetion\\images\\pan.png")
panimg = ct.CTkImage(pan,size = (170,112))
logo = ct.CTkLabel(headFrm,image = panimg,text = None)
logo.place(x = 10,y = 0)
logo.lift()




mainfrm = ct.CTkFrame(root,width = 1920,height = 720,bg_color="#EE956E",fg_color="#EE956E",border_width=2,border_color="black")
ymain=0.136
mainfrm.place(relx=0,rely=ymain)
img=Image.open("C:\\Gautam58\\softwarecompetion\\images\\chef.png")
imgnew=ct.CTkImage(img,size=(800,800))
imglbl=ct.CTkLabel(mainfrm,image=imgnew,text=None)
imglbl.place(x=30,y=10)

img2=Image.open("C:\\Gautam58\\softwarecompetion\\images\\btimg.png")
img2new=ct.CTkImage(img2,size=(680,680))
img2lbl=ct.CTkLabel(mainfrm,image=img2new,text=None)
img2lbl.place(x=800,y=10)


#ANIMATION DEF:
def ani_down():
    global ymain
    ymain=ymain+0.008
    if ymain<1:
        mainfrm.place(relx=0,rely=ymain)
        mainfrm.after(5,ani_down)
    else:
        pass

def dash_ani():
    global dy,meny
    meny+=2
    dy=dy+2
    if dy<=115:
        dashFrm.place(x=73,y=dy)
        mainfrm.after(5,dash_ani)
    else:
        pass
    if meny<=115:
        menubtn.place(x=-5,y=meny)
    else:
        pass

def dash_for():
    if dashx<=160:
        dashFrm.place(x=dashx)
        dashFrm.after(2,dash_for)
    else:
        pass

def dash_back():
    if dashx>=73:
        dashFrm.place(x=dashx)
        dashFrm.after(2,dash_back)
    else:
        pass

menu_tog=True
def menu_animation():
    if menu_tog:
        menu_for()
    else:
        menu_back()

def menu_for():
    global menwid,dashx,menu_tog
    dashx+=2.2
    menwid=menwid+2
    dash_for()
    sidebar_ani_for()
    if menwid<=165:
        menubtn.configure(width=menwid)
        menubtn.after(2,menu_for)
    else:
        menu_tog=False
    dashFrm.configure(width=1385)

def menu_back():
    global menwid,dashx,menu_tog 
    dashx-=2.2
    menwid=menwid-2
    dash_back()
    sidebar_ani_back()
    if menwid>=85:
        menubtn.configure(width=menwid)
        menubtn.after(2,menu_back)
    else:
        menu_tog=True
    dashFrm.configure(width=1462)

def sidebar_ani_for():
    global sidex
    sidex+=0.00009
    if sidex<=0:
        sidefrm.place(relx=sidex,rely=0.195,relheight=0.796,relwidth=0.1045)
        sidefrm.after(5,sidebar_ani_for)
    else:
        pass

def sidebar_ani_back():
    global sidex
    sidex-=0.00009
    if sidex>=-0.104:
        sidefrm.place(relx=sidex,rely=0.195,relheight=0.796,relwidth=0.1045)
        sidefrm.after(5,sidebar_ani_back)
    else:
        pass


def cat(event): 
    ani_down()
    dash_ani()

def ordhis(event):
    print("you are clicking order history!!")
    

def no(event):
    print("nothing")

def ext(event):
    root.destroy()

def categoryframe():
    catfrm.place(relx=0.104,rely=0.195,relheight=0.796,relwidth=0.9)
    catfrm.lower(mainfrm)
def billframe():
    billfrm.place(relx=0.104,rely=0.195,relheight=0.796,relwidth=0.9)
    billfrm.lower(mainfrm)
    
def ordhisframe():
    ordhisfrm.place(relx=0.104,rely=0.195,relheight=0.796,relwidth=0.9)
    ordhisfrm.lower(mainfrm)
def abtframe():
    abtfrm.place(relx=0.104,rely=0.195,relheight=0.796,relwidth=0.9)
    abtfrm.lower(mainfrm)

menu=Image.open("C:\\Gautam58\\softwarecompetion\\images\\menuicon.png")
menuimg=ct.CTkImage(menu,size=(30,30))
menubtn=ct.CTkButton(root,text=None,image=menuimg,width=80,border_width=2,fg_color="yellow",border_color="black",hover=False,height=50,command=menu_animation)
menwid=85
meny=54
menubtn.place(x=-5,y=meny)
menubtn.lower(belowThis=headFrm)

dashFrm = ct.CTkFrame(root,fg_color = "#FE8B00",bg_color = "black",border_width = 2,border_color = "black",width=1462,height=50)

dy=54
dashx=73
dashFrm.place(x=dashx,y=dy)
dashFrm.lower(belowThis=headFrm)

xaxis=20
c1 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Cold Beverage",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c1.place(relx=0.02,rely=0.2)
c2 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Hot Beverage",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c2.place(relx=0.13,rely=0.2)
c3 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Fast Food",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c3.place(relx=0.24,rely=0.2)
c4 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Special Thali",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c4.place(relx=0.35,rely=0.2)
c5 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Dessert",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c5.place(relx=0.46,rely=0.2)
c6 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "South Indian",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c6.place(relx=0.57,rely=0.2)
c7 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Chinese",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c7.place(relx=0.68,rely=0.2)
c8 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Puri Special",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c8.place(relx=0.79,rely=0.2)
c9 = ct.CTkButton(dashFrm,width = 115,bg_color = "#FE8B00",fg_color = "yellow",corner_radius = 8,text = "Frankies",font = ('Palatino Linotype', 15,"bold"),text_color = "black",border_width = 2,border_color = "black",hover_color = "#F9D911")
c9.place(relx=0.9,rely=0.2)



b1=Image.open("C:\\Gautam58\\softwarecompetion\\images\\Cat1.png")
b1new=ct.CTkImage(b1,size=(180,180))
b1lbl=ct.CTkLabel(mainfrm,image=b1new,text=None,cursor="hand2")
b1lbl.place(x=950,y=157)
b1lbl.bind('<Button-1>',cat)

b2=Image.open("C:\\Gautam58\\softwarecompetion\\images\\Cat2.png")
b2new=ct.CTkImage(b2,size=(180,180))
b2lbl=ct.CTkLabel(mainfrm,image=b2new,text=None,cursor="hand2")
b2lbl.place(x=1155,y=157)
b2lbl.bind('<Button-1>',ordhis)

b3=Image.open("C:\\Gautam58\\softwarecompetion\\images\\Cat3.png")
b3new=ct.CTkImage(b3,size=(180,180))
b3lbl=ct.CTkLabel(mainfrm,image=b3new,text=None,cursor="hand2")
b3lbl.place(x=950,y=361)
b3lbl.bind('<Button-1>',no)

b4=Image.open("C:\\Gautam58\\softwarecompetion\\images\\Cat4.png")
b4new=ct.CTkImage(b4,size=(180,180))
b4lbl=ct.CTkLabel(mainfrm,image=b4new,text=None,cursor="hand2")
b4lbl.place(x=1155,y=361)
b4lbl.bind('<Button-1>',ext)

plat=Image.open("C:\\Gautam58\\softwarecompetion\\images\\mid.png")
platnew=ct.CTkImage(plat,size=(130,90))
platlbl=ct.CTkLabel(mainfrm,image=platnew,text=None)
platlbl.place(x=1077,y=300)

sidefrm=ct.CTkFrame(root,fg_color='red',border_width=1)
sidex=-0.104
sidefrm.place(relx=sidex,rely=0.195,relheight=0.796,relwidth=0.1045)

flm=Image.open('C:\\Gautam58\\softwarecompetion\\images\\pan1.png')
flmimg=ct.CTkImage(flm,size=(130,130))
flmlbl=ct.CTkLabel(sidefrm,image=flmimg,text=None)
flmlbl.pack(pady=40)

scat=Image.open("C:\\Gautam58\\softwarecompetion\\images\\catogary.png")
scatimg=ct.CTkImage(scat,size=(30,30))
scatogary=ct.CTkButton(sidefrm,fg_color='white',text='CATOGARIES',image=scatimg,anchor='w',height=40,font=('cambria',15,'bold'),text_color='black',command=categoryframe)
scatogary.pack(pady=20)

sbill=Image.open("C:\\Gautam58\\softwarecompetion\\images\\ord.png")
sbillimg=ct.CTkImage(sbill,size=(30,30))
sbillbl=ct.CTkButton(sidefrm,fg_color='white',text='      BILL',image=sbillimg,anchor='w',height=40,font=('cambria',15,'bold'),text_color='black',command=billframe)
sbillbl.pack(pady=20)

sord=Image.open("C:\\Gautam58\\softwarecompetion\\images\\ordhis.png")
sordimg=ct.CTkImage(sord,size=(30,30))
sordlbl=ct.CTkButton(sidefrm,fg_color='white',text='ORDER\nHISTORY',image=sordimg,anchor='w',height=40,font=('cambria',15,'bold'),text_color='black',command=ordhisframe)
sordlbl.pack(pady=20)

sabt=Image.open("C:\\Gautam58\\softwarecompetion\\images\\abt.png")
sabtimg=ct.CTkImage(sabt,size=(30,25))
sabtlbl=ct.CTkButton(sidefrm,fg_color='white',text='ABOUT US',image=sabtimg,anchor='w',height=40,font=('cambria',15,'bold'),text_color='black',command=abtframe)
sabtlbl.pack(pady=20)

srtn=Image.open("C:\\Gautam58\\softwarecompetion\\images\\return.png")
srtnimg=ct.CTkImage(srtn,size=(30,30))
srtnbl=ct.CTkButton(sidefrm,fg_color='white',text='     EXIT',image=srtnimg,anchor='w',height=50,font=('cambria',15,'bold'),text_color='black',command=root.destroy)
srtnbl.pack(pady=20)

catfrm=ct.CTkFrame(root,fg_color='blue')
billfrm=ct.CTkFrame(root,fg_color='pink')
ordhisfrm=ct.CTkFrame(root,fg_color='yellow')
abtfrm=ct.CTkFrame(root,fg_color='green')
root.mainloop()