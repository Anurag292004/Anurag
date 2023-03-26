from tkinter import *
from tkinter import messagebox
from subprocess import call
import tkinter.font as font


w=Tk()
w.geometry('500x500')
w.resizable(False,False)
myfont=font.Font(family='Comic San MS',size=20,weight='bold')

#############Heading#############
Label(w,text="          Login          ", fg="yellow",bg="green",font=myfont).place(x=120,y=5)
f=LabelFrame(w,bg='green').place(x=45,y=60,height=300,width=400)

#############Email#############
name=StringVar()
Label(f,text="Enter Name :",fg='yellow',bg='green').place(x=130,y=70)
Entry(f,bd=5,textvariable=name,width=20).place(x=210,y=65)

#############Password#############
password=StringVar()
Label(f,text=" Password    :",fg='yellow',bg='green').place(x=130,y=110)
Entry(f,bd=5,width=20,textvariable=password,show="*").place(x=210,y=105)


#############Submit/Clear#############
def myreset():
    for widget in w.winfo_children():
        if isinstance(widget,Entry):
            widget.delete(0,'end')

def mysubmit():
    name_info=name.get()
    password_info=password.get()
    print("Email : "  ,name_info)
    print("Password : "  ,password_info)
    messagebox.showinfo("Successful Login",'Welcome, {}'.format(name_info))
    w.destroy
    call(["python","Bill_Management - Copy.py"])
    for widget in w.winfo_children():
        if isinstance(widget,Entry):
            widget.delete(0,'end')



Button(f,text="Submit",fg='darkblue',bg='red',bd=5,command=lambda:mysubmit()).place(x=175,y=150)
Button(f,text="  Clear  ",fg='darkblue',bg='red',bd=5,command=lambda:myreset()).place(x=255,y=150)



w.mainloop()
