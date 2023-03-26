from tkinter import *
from tkinter import messagebox
from subprocess import call
import tkinter.font as font


w=Tk()
w.geometry('500x500')
w.resizable(False,False)
myfont=font.Font(family='Comic San MS',size=20,weight='bold')

#############Heading#############
Label(w,text="Registration Form", fg="darkblue",bg="yellow",font=myfont).place(x=120,y=5)
f=LabelFrame(w,bg='yellow').place(x=45,y=60,height=300,width=400)

#############Name#############
name=StringVar()
Label(f,text="Enter Name :",fg='darkblue',bg='yellow').place(x=130,y=70)
Entry(f,bd=5,textvariable=name,width=20).place(x=210,y=65)

#############Email#############
email=StringVar()
Label(f,text="Enter Email  :",fg='darkblue',bg='yellow').place(x=130,y=110)
Entry(f,bd=5,textvariable=email,width=20).place(x=210,y=105)

#############Password#############
password=StringVar()
Label(f,text=" Password    :",fg='darkblue',bg='yellow').place(x=130,y=150)
Entry(f,bd=5,width=20,textvariable=password,show="*").place(x=210,y=145)

#############Gender#############
gender=StringVar()
Label(f,text="   Gender      :",fg='darkblue',bg='yellow').place(x=130,y=190)
g1=Radiobutton(f,text="Male",variable=gender,value="Male",fg='darkblue',bg='yellow')
g1.select()
g1.place(x=210,y=190)

g2=Radiobutton(f,text="Female",variable=gender,value="Female",fg='darkblue',bg='yellow')
g2.deselect()
g2.place(x=270,y=190)

#############Submit/Clear#############
def myreset():
    for widget in w.winfo_children():
        if isinstance(widget,Entry):
            widget.delete(0,'end')
        if isinstance(widget,Radiobutton):
            gender.set(None)

def mysubmit():
    name_info=name.get()
    email_info=email.get()
    password_info=password.get()
    gender_info=gender.get()
    print("Name : "  ,name_info)
    print("Email : "  ,email_info)
    print("Password : "  ,password_info)
    print("Gender : "  ,gender_info)
    messagebox.showinfo("Successful Register",'Welcome, {}'.format(name_info))
    w.destroy
    call(["python","Bill_Management - Copy.py"])
    for widget in w.winfo_children():
        if isinstance(widget,Entry):
            widget.delete(0,'end')
        if isinstance(widget,Radiobutton):
            gender.set(None)


Button(f,text="Submit",fg='darkblue',bg='red',bd=5,command=lambda:mysubmit()).place(x=175,y=220)
Button(f,text="  Clear  ",fg='darkblue',bg='red',bd=5,command=lambda:myreset()).place(x=255,y=220)



w.mainloop()
