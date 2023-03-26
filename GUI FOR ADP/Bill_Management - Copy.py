from tkinter import *
import random

class Bill_App:
    def __init__(self,root):
          self.root=root
          self.root.geometry("1300x670")
          self.root.maxsize(width = 1280,height = 670)
          self.root.minsize(width = 1280,height = 670)
          self.root.title("Bill Management")
          self.root.resizable(False,False)


#names#
          self.cus_name = StringVar()
          self.c_phone = StringVar()
          self.c_bill_no = StringVar()
          self.or_pizza=IntVar()
          self.cr_pizza=IntVar()
          self.psr_pizza=IntVar()
          self.ccr_pizza=IntVar()
          self.ctr_pizza=IntVar()
          self.mar_pizza=IntVar()
          self.vpr_pizza=IntVar()
          self.ppr_pizza=IntVar()
          self.om_pizza=IntVar()
          self.cm_pizza=IntVar()
          self.psm_pizza=IntVar()
          self.ccm_pizza=IntVar()
          self.ctm_pizza=IntVar()
          self.mam_pizza=IntVar()
          self.vpm_pizza=IntVar()
          self.ppm_pizza=IntVar()
          self.p_drink=IntVar()
          self.t_drink=IntVar()
          self.c_drink=IntVar()
          self.s_drink=IntVar()
          self.m_drink=IntVar()
          self.up_drink=IntVar()
          self.p2_drink=IntVar()
          self.t2_drink=IntVar()
          self.c2_drink=IntVar()
          self.s2_drink=IntVar()
          self.m2_drink=IntVar()
          self.up2_drink=IntVar()
          self.total_rpizza=StringVar()
          self.total_mpizza=IntVar()
          self.total_pizza=StringVar()
          self.tax_pizza=StringVar()
          self.total_1drink=StringVar()
          self.total_2drink=IntVar()
          self.total_drink=StringVar()
          self.tax_drink=StringVar()



          Label(self.root,text="Yummy Pizza Center",bg="red",fg="white",font=("Comic Sans MS",33),width="300",height="2").pack()
          #==========Customers Frame==========#
          F1 = LabelFrame(text = "Customer Details",font = ("Comic Sans MS",12,"bold"),fg = "white",bg ="red",relief = GROOVE,bd = 10)
          F1.place(x = 0,y = 90,relwidth = 1)           
          #===============Customer Name===========#
          cname_lbl = Label(F1,text="Customer Name",bg ="red",fg ="white",font=("Comic Sans MS",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
          cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
          cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)
          #=================Customer Phone==============#
          cphon_lbl = Label(F1,text = "Phone No",bg ="red",fg ="white",font = ("Comic Sans MS",15,"bold")).grid(row = 0,column = 2,padx = 20)
          cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
          cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)           
          #====================Customer Bill No==================#
          cbill_lbl = Label(F1,text = "Bill No.",bg ="red",fg ="white",font = ("Comic Sans MS",15,"bold"))
          cbill_lbl.grid(row = 0,column = 4,padx = 20)
          cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
          cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)          
          
          
          
#List of Dishes
          f=LabelFrame(self.root,text="Pizza's",bg="darkblue",font = ("Comic Sans MS",12,"bold"),fg="gold",highlightbackground="black",highlightthickness=1,width=460,height=350,bd = 10,relief = GROOVE)
          f.place(x=10,y=180)           
          
          Label(f,text="Name            Regular   Medium",font=("Comic Sans MS",18,"bold"),fg="gold",bg="darkblue").place(x=10,y=0)             
          Label(f,font=("Comic Sans MS",17),text="Onion                     ₹99           ₹199",fg="gold",bg="darkblue").place(x=10,y=45)
          Label(f,font=("Comic Sans MS",17),text="Capsicum                ₹99           ₹199",fg="gold",bg="darkblue").place(x=10,y=75)
          Label(f,font=("Comic Sans MS",17),text="Paneer Special       ₹99           ₹199",fg="gold",bg="darkblue").place(x=10,y=105)
          Label(f,font=("Comic Sans MS",17),text="Cheese & Corn       ₹99           ₹199",fg="gold",bg="darkblue").place(x=10,y=140)
          Label(f,font=("Comic Sans MS",17),text="Cheese & Tomato   ₹99           ₹199",fg="gold",bg="darkblue").place(x=10,y=175)
          Label(f,font=("Comic Sans MS",17),text="Margherita           ₹199          ₹299",fg="gold",bg="darkblue").place(x=10,y=210)
          Label(f,font=("Comic Sans MS",17),text="Veggie Paradise    ₹215          ₹395",fg="gold",bg="darkblue").place(x=10,y=240)
          Label(f,font=("Comic Sans MS",17),text="Peppy Paneer        ₹215          ₹395",fg="gold",bg="darkblue").place(x=10,y=275)


#Regular Entry
          Entry(f,bd=5,width=5,textvariable=self.or_pizza).place(x=265,y=47)
          Entry(f,bd=5,width=5,textvariable=self.cr_pizza).place(x=265,y=77)
          Entry(f,bd=5,width=5,textvariable=self.psr_pizza).place(x=265,y=107)
          Entry(f,bd=5,width=5,textvariable=self.ccr_pizza).place(x=265,y=142)
          Entry(f,bd=5,width=5,textvariable=self.ctr_pizza).place(x=265,y=177)
          Entry(f,bd=5,width=5,textvariable=self.mar_pizza).place(x=265,y=207)
          Entry(f,bd=5,width=5,textvariable=self.vpr_pizza).place(x=265,y=237)
          Entry(f,bd=5,width=5,textvariable=self.ppr_pizza).place(x=265,y=277)


#Medium Entry
          Entry(f,bd=5,width=5,textvariable=self.om_pizza).place(x=393,y=47)
          Entry(f,bd=5,width=5,textvariable=self.cm_pizza).place(x=393,y=77)
          Entry(f,bd=5,width=5,textvariable=self.psm_pizza).place(x=393,y=107)
          Entry(f,bd=5,width=5,textvariable=self.ccm_pizza).place(x=393,y=142)
          Entry(f,bd=5,width=5,textvariable=self.ctm_pizza).place(x=393,y=177)
          Entry(f,bd=5,width=5,textvariable=self.mam_pizza).place(x=393,y=212)
          Entry(f,bd=5,width=5,textvariable=self.vpm_pizza).place(x=393,y=242)
          Entry(f,bd=5,width=5,textvariable=self.ppm_pizza).place(x=393,y=277)


#List of Drinks
          d1 = LabelFrame(self.root,text = "Drink",font = ("Comic Sans MS",12,"bold"),fg = "gold",bg="darkblue",highlightbackground="black",highlightthickness=1,width=400,height=350,relief = GROOVE,bd = 10)
          d1.place(x = 475,y = 180)
          
          Label(d1,text="Name       750ml      2Lt",font=("Comic Sans MS",18,"bold"),fg="gold",bg="darkblue").place(x=10,y=0)           
          Label(d1,font=("Comic Sans MS",17),text="Pepsi              ₹40          ₹95",fg="gold",bg="darkblue").place(x=10,y=45)
          Label(d1,font=("Comic Sans MS",17),text="Thums UP      ₹40          ₹95",fg="gold",bg="darkblue").place(x=10,y=75)
          Label(d1,font=("Comic Sans MS",17),text="Coco Cola       ₹40          ₹95",fg="gold",bg="darkblue").place(x=10,y=105)
          Label(d1,font=("Comic Sans MS",17),text="Sprite            ₹40          ₹95",fg="gold",bg="darkblue").place(x=10,y=140)
          Label(d1,font=("Comic Sans MS",17),text="Maaza            ₹40          ₹95",fg="gold",bg="darkblue").place(x=10,y=175)
          Label(d1,font=("Comic Sans MS",17),text="7 UP               ₹40          ₹95",fg="gold",bg="darkblue").place(x=10,y=205  )        
          
#750ml Drinks          
          Entry(d1,bd=5,width=5,textvariable=self.p_drink).place(x=213,y=47)
          Entry(d1,bd=5,width=5,textvariable=self.t_drink).place(x=213,y=77)
          Entry(d1,bd=5,width=5,textvariable=self.c_drink).place(x=213,y=107)
          Entry(d1,bd=5,width=5,textvariable=self.s_drink).place(x=213,y=142)
          Entry(d1,bd=5,width=5,textvariable=self.m_drink).place(x=213,y=177)
          Entry(d1,bd=5,width=5,textvariable=self.up_drink).place(x=213,y=207)
          
#2Lt Drinks          
          Entry(d1,bd=5,width=5,textvariable=self.p2_drink).place(x=325,y=47)
          Entry(d1,bd=5,width=5,textvariable=self.t2_drink).place(x=325,y=77)
          Entry(d1,bd=5,width=5,textvariable=self.c2_drink).place(x=325,y=107)
          Entry(d1,bd=5,width=5,textvariable=self.s2_drink).place(x=325,y=142)
          Entry(d1,bd=5,width=5,textvariable=self.m2_drink).place(x=325,y=177)
          Entry(d1,bd=5,width=5,textvariable=self.up2_drink).place(x=325,y=207)
    
    
#===================Bill Aera================#
          F3 = Label(self.root,bd = 10,relief = GROOVE)
          F3.place(x = 880,y = 180,width = 410,height = 350)
          #===========
          bill_title = Label(F3,text = "Bill Area",fg="white",font = ("Comic Sans MS",13,"bold"),bg="darkblue",bd= 7,relief = GROOVE)
          bill_title.pack(fill = X)             
          #============
          scroll_y = Scrollbar(F3,orient = VERTICAL)
          self.txt = Text(F3,yscrollcommand = scroll_y.set)
          scroll_y.pack(side = RIGHT,fill = Y)
          scroll_y.config(command = self.txt.yview)
          self.txt.pack(fill = BOTH,expand = 1)             
    
    
#===========Buttons Frame=============#
          F4 = LabelFrame(self.root,text = "Calculates",bd = 10,relief = GROOVE,bg ="darkgreen",fg ="gold",font = ("Comic Sans MS",13,"bold"))
          F4.place(x = 0,y = 535,relwidth = 1,height = 130)
          #===================
          piz_lbl = Label(F4,font = ("Comic Sans MS",15,"bold"),fg ="white",bg ="darkgreen",text = "Total Price of Pizza's")
          piz_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
          piz_en = Entry(F4,bd = 8,relief = GROOVE, textvariable=self.total_pizza)
          piz_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)           
          #================
          dri_lbl = Label(F4,font = ("Comic Sans MS",15,"bold"),fg ="white",bg ="darkgreen",text = "Total Price of Drink's")
          dri_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
          dri_en = Entry(F4,bd = 8,relief = GROOVE,textvariable =self.total_drink)
          dri_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)           
          #================
          pizt_lbl = Label(F4,font = ("Comic Sans MS",15,"bold"),fg ="white",bg ="darkgreen",text = "Pizza's Tax")
          pizt_lbl.grid(row = 1,column = 2,padx = 30,pady = 0)
          pizt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable =self.tax_pizza)
          pizt_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)          
          #=================
          drit_lbl = Label(F4,font = ("Comic Sans MS",15,"bold"),fg ="white",bg ="darkgreen",text = "Drink's Tax")
          drit_lbl.grid(row = 2,column = 2,padx = 30,pady = 5)
          drit_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_drink)
          drit_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)          
          #====================
          total_btn = Button(F4,text = "Total",fg ="white",bg ="darkgreen",font=("Comic Sans MS",12,"bold"),bd = 7,relief = GROOVE,command =self.total)
          total_btn.place(x=740,y=20,width=100)
          #========================
          genbill_btn = Button(F4,text = "Generate Bill",fg ="white",bg ="darkgreen",font=("Comic Sans MS",12,"bold"),bd = 7,relief = GROOVE,command =self.bill_area)
          genbill_btn.place(x=850,y=20,width=150)
          #====================
          clear_btn = Button(F4,text = "Clear",fg ="white",bg ="darkgreen",font=("Comic Sans MS",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
          clear_btn.place(x=1010,y=20,width=90)
          #======================
          exit_btn = Button(F4,text = "Exit",fg ="white",bg ="darkgreen",font=("Comic Sans MS",12,"bold"),bd = 7,relief = GROOVE,command =self.exit)
          exit_btn.place(x=1110,y=20,width=100)


#Function to get total prices
    def total(self):
        self.total_rpizza = (
            (self.or_pizza.get() * 99)+
            (self.cr_pizza.get() * 99)+
            (self.psr_pizza.get() * 99)+
            (self.ccr_pizza.get() * 99)+
            (self.ctr_pizza.get() * 99)+
            (self.mar_pizza.get() * 199)+
            (self.vpr_pizza.get() * 215)+
            (self.ppr_pizza.get() * 215)
            )
        self.total_mpizza = (
            (self.om_pizza.get() * 199)+
            (self.cm_pizza.get() * 199)+
            (self.psm_pizza.get() * 199)+
            (self.ccm_pizza.get() * 199)+
            (self.ctm_pizza.get() * 199)+
            (self.mam_pizza.get() * 299)+
            (self.vpm_pizza.get() * 395)+
            (self.ppm_pizza.get() * 395)
            )
        self.total_pizza.set("Rs. "+str(round(self.total_rpizza)+(self.total_mpizza)))
        self.tax_pizza.set("Rs. "+str(round(self.total_rpizza*0.05)+round(self.total_mpizza*0.05)))


##Drinks
        self.total_1drink = (
            (self.p_drink.get() * 40)+
            (self.t_drink.get() * 40)+
            (self.c_drink.get() * 40)+
            (self.s_drink.get() * 40)+
            (self.m_drink.get() * 40)+
            (self.up_drink.get() * 40)
            )
        self.total_2drink = (
            (self.p2_drink.get() * 95)+
            (self.t2_drink.get() * 95)+
            (self.c2_drink.get() * 95)+
            (self.s2_drink.get() * 95)+
            (self.m2_drink.get() * 95)+
            (self.up2_drink.get() * 95)
            )
        self.total_drink.set("Rs. "+str(round(self.total_1drink)+(self.total_2drink)))
        self.tax_drink.set("Rs. "+str(round(self.total_1drink*0.05)+round(self.total_2drink*0.05)))

   
#Function For Text Area
    def welcome_soft(self):
            self.txt.delete('1.0',END)
            self.txt.insert(END,"       Welcome To Yummy Pizza Center\n")
            self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
            self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
            self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
            self.txt.insert(END,"\n=============================================")
            self.txt.insert(END,"\nPizza's            Size      Qty       Price")
            self.txt.insert(END,"\n=============================================")


#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)


#Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.or_pizza.get() != 0:
            self.txt.insert(END,f"\n Onion             Reg        {self.or_pizza.get()}         {self.or_pizza.get() * 99}")
        if self.om_pizza.get() != 0:
            self.txt.insert(END,f"\n Onion             Med        {self.om_pizza.get()}         {self.om_pizza.get() * 199}")
        if self.cr_pizza.get() != 0:
            self.txt.insert(END,f"\n Capsicum          Reg        {self.cr_pizza.get()}         {self.cr_pizza.get() * 99}")
        if self.cm_pizza.get() != 0:
            self.txt.insert(END,f"\n Capsicum          Med        {self.cm_pizza.get()}         {self.cm_pizza.get() * 199}")
        if self.psr_pizza.get() != 0:
            self.txt.insert(END,f"\n Panner Special    Reg        {self.psr_pizza.get()}         {self.psr_pizza.get() * 99}")
        if self.psm_pizza.get() != 0:
            self.txt.insert(END,f"\n Panner Special    Med        {self.psm_pizza.get()}         {self.psm_pizza.get() * 199}")
        if self.ccr_pizza.get() != 0:
            self.txt.insert(END,f"\n Cheese & Corn     Reg        {self.ccr_pizza.get()}         {self.ccr_pizza.get() * 99}")
        if self.ccm_pizza.get() != 0:
            self.txt.insert(END,f"\n Cheese & Corn     Med        {self.ccm_pizza.get()}         {self.ccm_pizza.get() * 199}")
        if self.ctr_pizza.get() != 0 :
            self.txt.insert(END,f"\n Cheese & Tomato   Reg        {self.ctr_pizza.get()}         {self.ctr_pizza.get() * 99}")
        if self.ctm_pizza.get() != 0 :
            self.txt.insert(END,f"\n Cheese & Tomato   Med        {self.ctm_pizza.get()}         {self.ctm_pizza.get() * 199}")
        if self.mar_pizza.get() != 0:
            self.txt.insert(END,f"\n Margherita        Reg        {self.mar_pizza.get()}         {self.mar_pizza.get() * 199}")
        if self.mam_pizza.get() != 0:
            self.txt.insert(END,f"\n Margherita        Med        {self.mam_pizza.get()}         {self.mam_pizza.get() * 299}")
        if self.vpr_pizza.get() != 0:
            self.txt.insert(END,f"\n Veggie Paradise   Reg        {self.vpr_pizza.get()}         {self.vpr_pizza.get() * 215}")
        if self.vpm_pizza.get() != 0:
            self.txt.insert(END,f"\n Veggie Paradise   Med        {self.vpm_pizza.get()}         {self.vpm_pizza.get() * 395}")
        if self.ppr_pizza.get() != 0:
            self.txt.insert(END,f"\n Peppy Panner      Reg        {self.ppr_pizza.get()}         {self.ppr_pizza.get() * 215}")
        if self.ppm_pizza.get() != 0:
            self.txt.insert(END,f"\n Peppy Panner      Med        {self.ppm_pizza.get()}         {self.ppm_pizza.get() * 395}")
        if self.p_drink.get() != 0:
            self.txt.insert(END,f"\n Pepsi           750ml        {self.p_drink.get()}         {self.p_drink.get() * 40}")
        if self.p2_drink.get() != 0:
            self.txt.insert(END,f"\n Pepsi             2Lt        {self.p2_drink.get()}         {self.p2_drink.get() * 95}")
        if self.t_drink.get() != 0:
            self.txt.insert(END,f"\n Thums UP        750ml        {self.t_drink.get()}         {self.t_drink.get() * 40}")
        if self.t2_drink.get() != 0:
            self.txt.insert(END,f"\n Thums UP          2Lt        {self.t2_drink.get()}         {self.t2_drink.get() * 95}")
        if self.c_drink.get() != 0:
            self.txt.insert(END,f"\n Coca Cola       750ml        {self.c_drink.get()}         {self.c_drink.get() * 40}")
        if self.c2_drink.get() != 0:
            self.txt.insert(END,f"\n Coca Cola         2Lt        {self.c2_drink.get()}         {self.c2_drink.get() * 95}")
        if self.s_drink.get() != 0:
            self.txt.insert(END,f"\n Sprite          750ml        {self.s_drink.get()}         {self.s_drink.get() * 40}")
        if self.s2_drink.get() != 0:
            self.txt.insert(END,f"\n Sprite            2Lt        {self.s2_drink.get()}         {self.s2_drink.get() * 95}")
        if self.m_drink.get() != 0:
            self.txt.insert(END,f"\n Maaza           750ml        {self.m_drink.get()}         {self.m_drink.get() * 40}")
        if self.m2_drink.get() != 0:
            self.txt.insert(END,f"\n Maaza             2Lt        {self.m2_drink.get()}         {self.m2_drink.get() * 95}")
        if self.up_drink.get() != 0:
            self.txt.insert(END,f"\n 7 UP            750ml        {self.up_drink.get()}         {self.up_drink.get() * 40}")
        if self.up2_drink.get() != 0:
            self.txt.insert(END,f"\n 7 UP              2Lt        {self.up2_drink.get()}         {self.up2_drink.get() * 95}")
        self.txt.insert(END,"\n=============================================")
        self.txt.insert(END,f"\n                               Total : {round(self.total_rpizza+self.total_mpizza+self.total_1drink+self.total_2drink+self.total_rpizza * 0.05+self.total_mpizza * 0.05+self.total_1drink * 0.05+self.total_2drink * 0.05)}")
        self.txt.insert(END,"\n===========Thank You Visit Again=============")
        

 #Function to exit
    def exit(self):
        self.root.destroy()

    #Function To Clear All Fields


        


root = Tk()
object =Bill_App(root)
root.mainloop()
