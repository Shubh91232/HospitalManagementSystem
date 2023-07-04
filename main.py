from tkinter import*
import tkinter as tk
# In[2]:
from tkinter import ttk
# In[3]:
import random
import time
import datetime
# In[4]:
from tkinter import messagebox
from tkinter.messagebox import askyesno
# In[5]:
import pymongo
from bson.objectid import ObjectId
#ploting
import matplotlib.pyplot as pt
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# import Bill
import billView

# In[ ]:
class Hospital:
    global Data
    def __init__(self,root):
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1200x700+0+0")
        
#----mydbconnect-----------------------------------------------------------------------------------------------------------------
        try:
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["hospital"] # Edit Hospital Nmae
            myadmin = mydb["admin"]
            myuser=mydb["userloginpass"]
            mypasent = mydb["PasentDatile"]
            mydoctor=mydb["DoctorList"]     
        except:
            print("Create or connect MangoDB ")
            hostitle=Label(self.root, bd=10 , relief=RIDGE , text="connect databse error " , fg="#1F7181" , bg="white",font=("times new roman",50,"bold"))
            hostitle.pack(side=TOP,fill=X)
            error='''myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            myb = myclient["hospital"] 
            myadmin = mydb["admin"]
            myuser=mydb["userloginpass"]
            mypasent = mydb["PasentDatile"]
            mydoctor=mydb["DoctorList"]
            '''
            Page=Text(self.root,relief=RIDGE,font=("Courier New",15))
            Page.place(x=0,y=160,width=710,height=350)
            Page.insert(tk.END, error)
            root.mainloop()
            

#-----------------------------------------------------------------------------------------------------------------
        def Clear_button():
            if BtnClr:
                txtName.delete(0,END)
                txtFName.delete(0,END)
                txtAdd.delete(0,END)
                txtMn.delete(0,END)
                txtAge.delete(0,END)
                txtAge.insert(0, "Year")
                txtAge.config(fg = 'grey')
                txtAge.bind("<FocusIn>", temp_text)
                txtPincode.delete(0,END) 
            else:
                pass
 #--------------------------------------------------------------------------------------------           
        def clock():
            global date,currenttime
            date=time.strftime('%d/%m/%Y')
            currenttime=time.strftime('%H:%M:%S')
        
#------------------------------------------------------------------------------------------
        def Login_f():
            BtnAdmin=Button(LogFrame,font=("arial",12,"bold"),text="Admin",fg="white",bg="Orange",padx=10,pady=4,command=Admin_Log)
            BtnAdmin.place(x=100,y=10,width=200,height=50)
            BtnUser=Button(LogFrame,font=("arial",12,"bold"),text="User",fg="white",bg="#1F7181",padx=17,pady=4,command=User_log)
            BtnUser.place(x=100,y=75,width=200,height=50)
            
        
#------------------------------------------------------------------------------------
            
                    
            
#------------------------------------------------------------------------------------------------------------------------------------
        def Take_Appoinment():
        
    
            AdminFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="DasBoard",fg="#1F7181",bg="white")
            AdminFrameRight.place(x=450,y=0,width=750,height=540)
            
            def Apoinment_Datile_Show():
                myquery = { "_id":count}
                myapoin = mypasent.find(myquery)
                for x in myapoin:
                    if x:
                        space='     '
                        MINES='----'
                        LINE='_'    
                        Data = MINES*5+"HOSPITAL"+MINES*5+"\n\n"+ space*6+"Date : "+x["Date"]+"   "+x["Currenttime"]+"\n "+x["Department"]+"  :"+x["DoctorName"]+"\n"+" ID :"+x["_id" ] + "\n Name : " + x["name" ] + "\n Father's Name : "+x["Father name"]+"\n Gender : "+x["Gender"]+"\n Age : "+x["Age"]+"\n Mobil no."+x["Mobile"]+"\n Addresh : "+x["address"]+"\n"+space*2+x["Pincode"]+"\n\n"+LINE*58
                    else:
                        messagebox.showerror('Error','Fields cannot be empty or \n Enter vailed ID')
                    
                Page=Text(AdminFrameRight,relief=RIDGE,font=("Courier New",15))
                Page.place(x=0,y=60,width=710,height=500)
                Page.insert(tk.END, Data)
                    
                    
            typeMn=txtMn.get()
            typeAge=txtAge.get()
            typePincode=txtPincode.get()
            
            if txtName.get()=='' or txtFName.get()==''or txtMn.get()=='' or txtAdd.get()=='' or  txtAge.get()=='' or txtPincode.get()=='':
                    messagebox.showwarning('Error','Fields cannot be empty')
                    
            elif Take_Appoinment:
                
                if typeMn.isdigit() and len(typeMn)==10 :
                    if typeAge.isdigit() and txtAge.get() != 0:
                        if typePincode.isdigit() and len(typePincode)==6:
                            x=0
                            y=0
                            p=0
                            for x in mypasent.find({},{"_id":1}):
                                p=int(x["_id"])
                            C=p+1
                            count=str(C)
                            
                            
                            myquery= { "_id":comDepartmentTable.current()}
                            mydoc =  mydoctor.find(myquery)
                            doct="Unknow"
                            for D in mydoc:
                                doct=D["name"]
                            
                            myquery = { "name":txtName.get(),"Mobile":txtMn.get()}
                            checker = mypasent.find(myquery)
                            for y in checker:
                                if y:
                                    y=1
                                else:
                                    y=0
                                
                                
                            if y==1:
                                messagebox.showinfo('Apointment','Appointment already taken')
                            else:
                                ratio={0:"Male",1:"Female",2:"Other"}
                                depart={0:"General Surgery",1:"General Medicine",2:"Neurology",3:"Nephrology",4:"ENT",5:"Dental Science",6:"Cardiology"}
                                dep=depart[comDepartmentTable.current()]
                                Gen=ratio[comGenderTable.current()]
                                clock()
                                mydict = { "_id":count,"Department":dep,"DoctorName":doct,"name":txtName.get() ,"Father name":txtFName.get(),"Mobile":txtMn.get() ,"Age":txtAge.get() ,"address":txtAdd.get() , "Pincode":txtPincode.get() ,"Gender":Gen,"Date":date ,"Currenttime":currenttime}
                                messagebox.showinfo('Apointment','Apointment Seccuss with \"Apoinment Id \"'+count)
                                mypasent.insert_one(mydict)   
                                answer = askyesno(title='Clear',message='Apoinment success Yes To clear form')
                                if answer:
                                    Clear_button()
                                Apoinment_Datile_Show()

                        else:
                            messagebox.showerror('Error','Enter vailed Pincode')    
                    else:
                        messagebox.showerror('Error','Enter vailed Age')
                else:
                     messagebox.showerror('Error','Enter vailed Mobile Number')
                
            else:
                messagebox.showerror('Error','Somethig went wrong')
 #--------------------------------------------------------------------------------------------------               
        
        hostitle=Label(self.root, bd=10 , relief=RIDGE , text="+ HOSPITAL +" , fg="#1F7181" , bg="white",font=("times new roman",50,"bold"))
        hostitle.pack(side=TOP,fill=X)
        
        DataFrame=Frame(self.root,relief=RIDGE)
        DataFrame.place(x=0,y=100,width=1200,height=600)
        
        DataFrameLeft=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Aappoinment",fg="#2490AB")
        DataFrameLeft.place(x=0,y=0,width=445,height=375)
        
        LogFrame=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Login",fg="#2490AB")
        LogFrame.place(x=0,y=380,width=445,height=160)
        
        DataFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="status",fg="#1F7181",bg="white")
        DataFrameRight.place(x=450,y=0,width=750,height=540)
        
        
        #bg = PhotoImage(file = "hospital.png")
  
        #label1 = Label( DataFrameRight, image = bg)
        #label1.place(x = 0, y = 0)
        #DataFrameDown=LabelFrame(DataFrame,bd=1,relief=RIDGE)
        #DataFrameDown.place(x=0,y=500,width=1200,height=60)
        #------------------------------------------------------------------------------------------------------
        
        lblDepartmentTablet=Label(DataFrameLeft,font=("arial",12,"bold"),text="Department",padx=2,pady=6)
        lblDepartmentTablet.grid(row=0,column=0,sticky=W)
        
        comDepartmentTable=ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12,"bold"),width=25)
        comDepartmentTable['value']=("General Surgery","General Medicine","Neurology","Nephrology","ENT","Dental Science","Cardiology")
        comDepartmentTable.current(0)
        comDepartmentTable.grid(row=0,column=1)
        #-------------------------------------------------------------------------------------------------------------------------
        
        lblName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Name :",padx=2,pady=4)
        lblName.grid(row=1,column=0,sticky=W)
        txtName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=27)
        txtName.grid(row=1,column=1)
        #------------------------------------------------------------------------------------------------------------------------
        
        lblFName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Father Name :",padx=2,pady=8)
        lblFName.grid(row=2,column=0,sticky=W)
        txtFName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=27)
        txtFName.grid(row=2,column=1)
        #------------------------------------------------------------------------------------------------------------------------
        
        lblMn=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile No :",padx=2,pady=6)
        lblMn.grid(row=3,column=0,sticky=W)
        txtMn=Entry(DataFrameLeft,font=("arial",13,"bold"),width=27)
        txtMn.grid(row=3,column=1)
        #------------------------------------------------------------------------------------------------------------------------
        
        lblAdd=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address :",padx=2,pady=6)
        lblAdd.grid(row=5,column=0,sticky=W)
        txtAdd=Entry(DataFrameLeft,font=("arial",13,"bold"),width=27)
        txtAdd.grid(row=5,column=1)
        #------------------------------------------------------------------------------------------------------------------------

        lblPincode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Pincode :",padx=2,pady=6)
        lblPincode.grid(row=6,column=0,sticky=W)
        txtPincode=Entry(DataFrameLeft,font=("arial",13,"bold"),width=27)
        txtPincode.grid(row=6 ,column=1)
        #------------------------------------------------------------------------------------------------------------------------
        def temp_text(e):
            txtAge.delete(0,"end")
            txtAge.config(fg = 'black')
        
        lblAge=Label(DataFrameLeft,font=("arial",12,"bold"),text="Age :",padx=2,pady=6)
        lblAge.grid(row=4,column=0,sticky=W)
        txtAge=Entry(DataFrameLeft,font=("arial",13,"bold"),width=27)
        txtAge.insert(0, "Year")
        txtAge.config(fg = 'grey')
        txtAge.bind("<FocusIn>", temp_text)
        txtAge.grid(row=4,column=1)
        #------------------------------------------------------------------------------------------------------------------------
        
        lblGender=Label(DataFrameLeft,font=("arial",12,"bold"),text="Gender :",padx=2,pady=6)
        lblGender.grid(row=7,column=0,sticky=W)
        
        comGenderTable=ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12,"bold"),width=25)
        comGenderTable['value']=("Male","Female","Other")
        comGenderTable.current(0)
        comGenderTable.grid(row=7,column=1)
        
        #----------------------------------------------------------------------------------------------------------
        
        BtnApoin=Button(font=("arial",12,"bold"),text="Apointment",fg="white",bg="#1F7181",command=Take_Appoinment)
        BtnApoin.place(x=277,y=410,width=100,height=50)
        
        BtnClr=Button(font=("arial",12,"bold"),text="Clear",fg="white",bg="#2490AB",command=Clear_button)
        BtnClr.place(x=127,y=410,width=100,height=50)
        
#---Admin LOGIN----------------------------------------------------------------------------------------------
    
        def Admin_Log():
            
            Line='_'
            def Admin_Dashboard():  
                AdminFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Dashboard",fg="#1F7181")
                AdminFrameRight.place(x=450,y=0,width=750,height=540)
                
                def Admin_Update():
                    def clear():
                        N_IDtxtEntry.delete(0,END)
                        N_PasstxtEntry.delete(0,END)
                        Re_PasstxtEntry.delete(0,END)
                        AdIDtxtEntry.delete(0,END)
                        PasstxtEntry.delete(0,END)
                        NPasstxtEntry.delete(0,END)
                        
                    def Update_Admin_Password():
                        if AdIDtxtEntry.get()=='' or PasstxtEntry.get()=='' or NPasstxtEntry.get()=='':
                            messagebox.showerror('Error','Fields cannot be empty ')
                        else:
                            myquery = { "_id":str(AdIDtxtEntry.get()) ,"password": str(PasstxtEntry.get()) }
                            check = myadmin.find(myquery)
                            x=0
                            pas=0
                            for x in check:
                                pas=x["password"]
                            if pas==PasstxtEntry.get():
                                newvalues = { "$set": { "password": NPasstxtEntry.get()} }
                                myadmin.update_one(myquery, newvalues)
                                messagebox.showinfo('Success','Password change success')
                                clear()
                            else:
                                messagebox.showinfo('Not vailed','Id and Password not vailed')
                                    
                    UpdateAdminFrameRight=LabelFrame(AdminFrameRight,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),fg="#1F7181",bg="#c9dfe3")
                    UpdateAdminFrameRight.place(x=0,y=130,width=720,height=380)
                    
                    AdIDtxtlbl=Label(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Enter AdminId :",fg="#1F7181",bg="#c9dfe3")
                    AdIDtxtlbl.place(x=50,y=70)
                    AdIDtxtEntry=Entry(UpdateAdminFrameRight,font=("arial",13),width=25)
                    AdIDtxtEntry.place(x=210,y=70)
                       
                        
                    Passtxtlbl=Label(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Old Password :",fg="#1F7181",bg="#c9dfe3")
                    Passtxtlbl.place(x=50,y=100)
                    PasstxtEntry=Entry(UpdateAdminFrameRight,font=("arial",13),width=25)
                    PasstxtEntry.place(x=210,y=100)
                    
                    
                    NPasstxtlbl=Label(UpdateAdminFrameRight,font=("arial",12,"bold"),text="New Password :",fg="#1F7181",bg="#c9dfe3")
                    NPasstxtlbl.place(x=50,y=130)
                    NPasstxtEntry=Entry(UpdateAdminFrameRight,font=("arial",13),width=25)
                    NPasstxtEntry.place(x=210,y=130)
                    
                    UpdateButton=Button(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Update",fg="white",bg="#1F7181",command=Update_Admin_Password)
                    UpdateButton.place(x=250,y=160,width=130,height=30)
                    
                    
                    def Delet_Admin():
                        if Re_PasstxtEntry.get()=='' or N_IDtxtEntry.get()=='':
                                messagebox.showerror('Error','Fields cannot be empty or \n Enter vailed ID')
                        else:
                            
                            if N_PasstxtEntry.get()==Re_PasstxtEntry.get():
                                delet={"_id":N_IDtxtEntry.get(),"password":Re_PasstxtEntry.get()}
                            
                                myquary=myadmin.find(delet)
                                x=0
                                for x in myquary:
                                    pass
                                if x:
                                    myadmin.delete_one(delet)
                                    messagebox.showinfo('Sucess','delete sucessfull')
                                    clear()
                                else:
                                    messagebox.showerror('Error','Not avilable')
                            else:
                                messagebox.showerror('Error','Not Match Password')
                            
                    def Register_New_Admin():
                        if Re_PasstxtEntry.get()=='' or N_IDtxtEntry.get()=='':
                             messagebox.showerror('Error','Fields cannot be empty')
                        else:
                            
                            if N_PasstxtEntry.get()==Re_PasstxtEntry.get():
                                check={"_id":N_IDtxtEntry.get(),"password":Re_PasstxtEntry.get()}
                                myquary=myadmin.find(check)
                                x=0
                                for x in myquary:
                                    pass
                                if x:
                                    messagebox.showerror('Error','Id already taken')
                                else:
                                    myadmin.insert_one(check)
                                    messagebox.showinfo('Success','Admin Sucessfull register')
                                    clear()
                            else:
                                messagebox.showerror('Error','Password not matched')
                        
                    N_IDtxtlbl=Label(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Enter Id :",fg="#1F7181",bg="#c9dfe3")
                    N_IDtxtlbl.place(x=50,y=220)
                    N_IDtxtEntry=Entry(UpdateAdminFrameRight,font=("arial",13),width=25)
                    N_IDtxtEntry.place(x=210,y=220)
                    
                    N_Passtxtlbl=Label(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Enter Password :",fg="#1F7181",bg="#c9dfe3")
                    N_Passtxtlbl.place(x=50,y=250)
                    N_PasstxtEntry=Entry(UpdateAdminFrameRight,font=("arial",13),width=25)
                    N_PasstxtEntry.place(x=210,y=250)
                    
                    Re_Passtxtlbl=Label(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Re-Enter Password :",fg="#1F7181",bg="#c9dfe3")
                    Re_Passtxtlbl.place(x=50,y=280)
                    Re_PasstxtEntry=Entry(UpdateAdminFrameRight,font=("arial",13),width=25)
                    Re_PasstxtEntry.place(x=210,y=280)
                    
                    DeletButton=Button(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Delete",fg="red",bg="white",command=Delet_Admin)
                    RegisterButton=Button(UpdateAdminFrameRight,font=("arial",12,"bold"),text="Register",fg="white",bg="#1F7181",command=Register_New_Admin)
                    DeletButton.place(x=220,y=330)
                    RegisterButton.place(x=360,y=330)
                    
                
               # def Apn_Datile_Show_Frame():  
                def temp_ID_search(e):
                    IDSearch.delete(0,"end")
                    IDSearch.config(fg = 'black')
                def temp_Name_search(e):
                    NameSearch.delete(0,"end")
                    NameSearch.config(fg = 'black')      
                def temp_Mn_search(e):
                    MnSearch.delete(0,"end")
                    MnSearch.config(fg = 'black')
                    
                def All_Apoinment_Show():
                    ApoinAdminFrameRight=LabelFrame(AdminFrameRight,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),fg="#1F7181",bg="white")
                    ApoinAdminFrameRight.place(x=0,y=130,width=720,height=380)
                    Page=Text(ApoinAdminFrameRight,relief=RIDGE,font=("Courier New",15))
                    Page.place(x=0,y=0,width=700,height=360)
                    myapoin = mypasent.find()
                    data=0
                    for x in myapoin:
                        data="ID :" + str(x["_id"])+":Name :"+x["name"]+": Mn :"+x["Mobile"]+"\n"+30*" "+"Date :"+x["Date"]+" ~ "+x["Currenttime"]+"\n"+Line*58+"\n"
                        Page.insert(tk.END,data)
                        
                        
                def All_User_Show():
                    UserFrameRight=LabelFrame(AdminFrameRight,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),fg="#1F7181",bg="white")
                    UserFrameRight.place(x=0,y=130,width=720,height=380)
                    Page=Text(UserFrameRight,relief=RIDGE,font=("Courier New",15))
                    Page.place(x=-2,y=0,width=700,height=360)
                    myuserdatile = myuser.find()
                    data=0
                    for x in myuserdatile:
                        data="@ ID :" + str(x["_id"])+4*" "+"Pasword :"+x["Pasword"]+"\nName :"+x["name"]+"   Father name :"+x["Father name"]+"\nMobile no :"+x["Mobile"]+"   Address :"+x["address"]+","+x["Pincode"]+"\n"+Line*58+"\n\n"
                        Page.insert(tk.END,data)
                        
                        
                def Doct_Show():
                    
                    DoctFrameRight=LabelFrame(AdminFrameRight,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),fg="#1F7181",bg="white")
                    DoctFrameRight.place(x=0,y=130,width=720,height=380)
                    
                    def pageing():    
                        Page=Text(DoctFrameRight,relief=RIDGE,font=("Courier New",15))
                        Page.place(x=0,y=50,width=700,height=315)

                        myDoctList = mydoctor.find()
                        x=0
                        for x in myDoctList:
                            if x:
                                Doctdata= "Department : "+x["department"]+"   "+" Name : "+x["name"]+"\n"+Line*58+"\n\n"
                                Page.insert(tk.END,Doctdata)
                            else:
                                Doctdata=0
                                Page.insert(tk.END,Doctdata)
                    
                    def temp_Dep_search(e):
                        DSearch.delete(0,"end")
                        DSearch.config(fg = 'black')
                        
                    def Doc_Upd():
                        #Page.insert(tk.END,DSearch.get())
                        doctor_name=str(DSearch.get())
                        answer = askyesno(title='Doctor Update',message='Are you sure Update')
                        if answer:
                            myquery = { "_id":  Department_Doct.current() }
                            mydoccheck=mydoctor.find(myquery)
                            x=0
                            for x in mydoccheck:
                                x=1
                                
                            if x==1:
                                newvalues = { "$set": { "name":doctor_name} }
                                mydoctor.update_one(myquery, newvalues)
                                pageing()
                            else:
                                depart={0:"General Surgery",1:"General Medicine",2:"Neurology",3:"Nephrology",4:"ENT",5:"Dental Science",6:"Cardiology"}
                                dep=depart[Department_Doct.current()]
                                mydict = { "_id": Department_Doct.current(),"department":dep ,"name": doctor_name }
                                mydoctor.insert_one(mydict)
                
                    pageing()
                    DNametxtlbl=Label(DoctFrameRight,font=("arial",12,"bold"),text="Select Department :",bg="#bde5e8")
                    DNametxtlbl.place(x=0,y=7)
                    Department_Doct=ttk.Combobox(DoctFrameRight,state="readonly",font=("arial",12,"bold"),width=15)
                    Department_Doct['value']=("General Surgery","General Medicine","Neurology","Nephrology","ENT","Dental Science","Cardiology")
                    Department_Doct.current(0)
                    Department_Doct.place(x=160,y=7)
                    DSearch=Entry(DoctFrameRight,font=("arial",13),width=23)
                    DSearch.insert(0, "Doctor Full Name")
                    DSearch.config(fg = 'grey')
                    DSearch.bind("<FocusIn>", temp_Dep_search)
                    DSearch.place(x=340,y=7)
                    D_btnDocUpd=Button(DoctFrameRight,font=("arial",12,"bold"),text="Update",fg="white",bg="#1F7181",command=Doc_Upd)
                    D_btnDocUpd.place(x=565,y=7,width=130,height=30)
                 
                def Apoinment_Delet():
                    
                    answer = askyesno(title='Delete',message='Are you sure that you want to delete it')
                    if answer:
                        #myquery = { "name":NameSearch.get(),"Mobile":MnSearch.get()}
                        mypasent.delete_one(myquery)
                        messagebox.showinfo('deleted','Doc deleted')
                    else:
                        pass
                    
                def Apoinment_Datile_Show():
                    apoinmentid=[]
                    if IDSearch.get() == '':
                        if MnSearch.get()=='' and NameSearch.get()=='' :
                            messagebox.showerror('Error','Fields cannot be empty or \n Enter vailed ID')
                        global myquery
                        myquery= { "name":NameSearch.get(),"Mobile":MnSearch.get()}
                        myapoin = mypasent.find(myquery) 
                        
                    else:
                        myquery = { "_id":IDSearch.get()}
                        myapoin = mypasent.find(myquery)
                    Data="Plase Enter correct datile"
                    for x in myapoin:
                        if x:
                            space='     '
                            MINES='----'
                            LINE='_'
                            dep=x["Department"]
                            Gen=x["Gender"]
                            apoinmentid.append(x["_id"])   
                            Data = MINES*5+" HOSPITAL"+MINES*5+"\n\n"+ space*6+"Date : "+x["Date"]+"   "+x["Currenttime"]+"\n "+dep+"  :"+x["DoctorName"]+"\n"+" ID :"+x["_id" ] + "\n Name : " + x["name" ] + "\n Father's Name : "+x["Father name"]+"\n Gender : "+Gen+"\n Age : "+x["Age"]+"\n Mobil no."+x["Mobile"]+"\n Addresh : "+x["address"]+"\n"+space*2+x["Pincode"]+"\n\n"+LINE*58
                        else:
                            messagebox.showerror('Error','Fields cannot be empty or \n Enter vailed ID')
                    UserFrameRight=LabelFrame(AdminFrameRight,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),fg="#1F7181",bg="white")
                    UserFrameRight.place(x=0,y=130,width=720,height=380)
                    
                    if Data=="Plase Enter correct datile":
                        Page=Text(UserFrameRight,relief=RIDGE,font=("Courier New",15))
                        Page.place(x=-2,y=0,width=700,height=360)
                        Page.insert(tk.END, Data)
                    
                    else:
                        Page=Text(UserFrameRight,relief=RIDGE,font=("Courier New",15))
                        Page.place(x=-2,y=0,width=700,height=360)
                        Page.insert(tk.END, Data)
#july 1 2023 -------------------------------------------------------------------------------------------------------------------------------------------
                        import billView
                        def view_bill():
                            #print("appp"-apoinmentid)
                            for x in apoinmentid:
                                 billView.bill(x)
                        viewBill=Button(UserFrameRight,font=("arial",12,"bold"),text="ViewBill",fg="red",bg="white",command=view_bill)
                        viewBill.place(x=0,y=0,width=70,height=15)
                        
                        import AddorUpdateBill

                        def add_bill():
                            AddorUpdate=False
                            AddorUpdateBill.Admin_bill(apoinmentid[0],AddorUpdate)
                        def update_bill():
                            AddorUpdate=True
                            AddorUpdateBill.Admin_bill(apoinmentid[0],AddorUpdate)



                        AddBill=Button(UserFrameRight,font=("arial",12,"bold"),text="AddBill",fg="red",bg="white",command=add_bill)
                        AddBill.place(x=80,y=0,width=70,height=15)

                        UpdateBill=Button(UserFrameRight,font=("arial",12,"bold"),text="UpdateBill",fg="red",bg="white",command=update_bill)
                        UpdateBill.place(x=155,y=0,width=90,height=15)

                        btnDelet=Button(UserFrameRight,font=("arial",12,"bold"),text="delete",fg="red",bg="white",command=Apoinment_Delet)
                        btnDelet.place(x=580,y=0,width=70,height=15)

                btnBill=Button(AdminFrameRight,font=("arial",12,"bold"),text="Bill",fg="white",bg="#1F7181",command=Apoinment_Datile_Show)
                btnBill.place(x=0,y=80,width=130,height=30)
                    
# analysing function-----------------------------------------------------------------------------------------------------------------------------                    
                def Analysis_tracker():
                    # Create the GUI window
                    class Plotter:
                        def __init__(self, master, x, x_pos,labels,titles):
                            self.fig = Figure(figsize=(4, 3), dpi=120)
                            self.ax = self.fig.add_subplot(111)
                            self.ax.pie(x, labels=labels, autopct='%1.1f%%', startangle=90)
                            self.ax.set_title(titles)

                            self.canvas = FigureCanvasTkAgg(self.fig, master=master)
                            self.canvas.draw()
                            self.canvas.get_tk_widget().place(x=x_pos, y=450)

                    # Create the GUI window
                    root = tk.Tk()
                    root.geometry("1200x800")
                    
                    def Back():
                        root.destroy()
                        Analysis_tracker()
                        
                    
                    def Fullanalysis():
                        My_collection=mydb["Number_passents_data"]
                        # Create a pandas DataFrame
                        doc_id = ObjectId("642598c0b2ca26da36838713")
                        my_document = my_collection.find_one({"_id": doc_id})
                        hospitals = pd.DataFrame(my_document)
                        # Pivot the DataFrame to create a matrix of passenger counts for each month and year
                        hospitals_pivot = hospitals.pivot("month", "year", "patient")

                        # Create a heatmap of passenger counts
                        fig, ax = plt.subplots(figsize=(15, 10))
                        ax.set_title("Number of Patient")
                        sns.heatmap(hospitals_pivot, fmt="d", annot=True, cmap='Blues')

                        canvas = FigureCanvasTkAgg(fig, master=root)
                        canvas.draw()
                        canvas.get_tk_widget().pack()
                        
                        BtnBack=Button(root,font=("arial",12,"bold"),text="<~~GO BACK",fg="white",bg="#1F7181",padx=17,pady=4,command=Back)
                        BtnBack.place(x=0,y=0,width=240,height=40)

                    
                    def Monthly():
                        # Add some data to the plot
                        y=[80,20]
                        lavel1=["Full","Avilable"]
                        
                        x = [2,30,5,40,3,10,10]
                        lavel2=["Cancer", "Diabrtes","Meningitis","Fiver","Heart attack","Asthma","Arthritis"]
                        # Create the plot objects
                        plot1 = Plotter(root,y,0,lavel1,"Hospital Resources")
                        plot1 = Plotter(root, x,720,lavel2,"Diseases")


                        fig = Figure(figsize=(12, 4.5), dpi=100)
                        ax = fig.add_subplot(111)


                        data={"date":[],"illnes":[]}

                        for x in range(30):
                          data["date"]=data["date"]+[x+1]
                          data["illnes"]=data["illnes"]+[random.randint(300,1000)]

                        colors = ['#37535c' if height > 500 else '#628b99' for height in data["illnes"]]
                        ax.bar(data["date"],data["illnes"],color=colors)
                        for i, v in enumerate(data["illnes"]):
                            ax.text(i+1, v+1, str(v), ha='center', fontweight='bold')

                        ax.set_xlabel("Date:DD")
                        ax.set_ylabel("Counts")
                        ax.set_title("Numbers of Patient")

                        #ax.bar(x, y)
                        canvas = FigureCanvasTkAgg(fig, master=root)
                        canvas.draw()
                        canvas.get_tk_widget().place(x=0,y=0)
                    
                    
                    Monthly()
                    
                    R_lblUserId=Label(root,font=("arial",12,"bold"),text="Year         Month          Day",bg="white",padx=2,pady=4)
                    R_lblUserId.place(x=480,y=455,width=240,height=20)

                    R_txtUserId=Entry(root,font=("arial",13),width=50)
                    R_txtUserId.place(x=482.5,y=480,width=75,height=35)

                    R_txtUserId=Entry(root,font=("arial",13),width=50)
                    R_txtUserId.place(x=560.5,y=480,width=80,height=35)

                    R_txtUserId=Entry(root,font=("arial",13),width=50)
                    R_txtUserId.place(x=643,y=480,width=75,height=35)


                    Btnchangemonth=Button(root,font=("arial",12,"bold"),text="GO TO~~>",fg="white",bg="#1F7181",padx=17,pady=4)
                    Btnchangemonth.place(x=480,y=520,width=240,height=40)

                    BtnALLV=Button(root,font=("arial",12,"bold"),text="ALL HISTORICAL~~>",fg="white",bg="#1F7181",padx=17,pady=4,command=Fullanalysis)
                    BtnALLV.place(x=480,y=570,width=240,height=40)

                    R_lblUserId=Label(root,font=("arial",12,"bold"),text="Temp Notes :",bg="white",padx=2,pady=4)
                    R_lblUserId.place(x=480,y=620,width=240,height=20)

                    Page=Text(root,relief=RIDGE,font=("Courier New",15))
                    Page.place(x=485,y=640,width=230,height=150)
                    
                    # Start the GUI loop
                    tk.mainloop()

 #-----------------------------------------------------------------------------------------------------------------------------------------------------           
                IDtxtlbl=Label(AdminFrameRight,font=("arial",12,"bold"),text="Apointment ID")
                IDtxtlbl.place(x=0,y=10)
                Nametxtlbl=Label(AdminFrameRight,font=("arial",12,"bold"),text="Name")
                Nametxtlbl.place(x=160,y=10)
                Mntxtlbl=Label(AdminFrameRight,font=("arial",12,"bold"),text="Mobile No.")
                Mntxtlbl.place(x=380,y=10)
                
                IDSearch=Entry(AdminFrameRight,font=("arial",13),width=15)
                IDSearch.insert(0, "ID")
                IDSearch.config(fg = 'grey')
                IDSearch.bind("<FocusIn>", temp_ID_search)
                IDSearch.place(x=0,y=40)
                
                Ortxtlbl=Label(AdminFrameRight,font=("arial",12,"bold"),text="Or'")
                Ortxtlbl.place(x=130,y=40)
                
                NameSearch=Entry(AdminFrameRight,font=("arial",13),width=20)
                NameSearch.insert(0, "Name")
                NameSearch.config(fg = 'grey')
                NameSearch.bind("<FocusIn>", temp_Name_search)
                NameSearch.place(x=160,y=40)
                
                MnSearch=Entry(AdminFrameRight,font=("arial",13),width=20)
                MnSearch.insert(0, "Mobile No.")
                MnSearch.config(fg = 'grey')
                MnSearch.bind("<FocusIn>", temp_Mn_search)
                MnSearch.place(x=380,y=40)
                
                
                
                btnSearch=Button(AdminFrameRight,font=("arial",12,"bold"),text="Search",fg="white",bg="#1F7181",command=Apoinment_Datile_Show)
                btnSearch.place(x=580,y=36,width=130,height=30)
                
                btnAllApoin=Button(AdminFrameRight,font=("arial",12,"bold"),text="All Apoinment",fg="white",bg="#1F7181",command=All_Apoinment_Show)
                btnAllApoin.place(x=580,y=80,width=130,height=30)
                
                btnAllUser=Button(AdminFrameRight,font=("arial",12,"bold"),text="All User",fg="white",bg="#1F7181",command=All_User_Show)
                btnAllUser.place(x=435,y=80,width=130,height=30)
                
                btnDoc=Button(AdminFrameRight,font=("arial",12,"bold"),text="Doctor",fg="white",bg="#1F7181",command=Doct_Show)
                btnDoc.place(x=290,y=80,width=130,height=30)
                
                btnAdminUpdate=Button(AdminFrameRight,font=("arial",12,"bold"),text="Admin Update",fg="white",bg="#1F7181",command=Admin_Update)
                btnAdminUpdate.place(x=145,y=80,width=130,height=30)
    
                
                
                
                
                
                
 #-------------------------------------------------------------------------------------------------------------------------------------------------               
                
            LogFrame=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Login",fg="#2490AB")
            LogFrame.place(x=0,y=380,width=445,height=160)
            
            lblAdId=Label(LogFrame,font=("arial",12,"bold"),text="AdminID :",padx=2,pady=6)
            lblAdId.grid(row=0,column=0,sticky=W)
            txtAdId=Entry(LogFrame,font=("arial",13,"bold"),width=27)
            txtAdId.grid(row=0,column=1)
            
            lblPas=Label(LogFrame,font=("arial",13,"bold"),text="Password :",padx=2,pady=6)
            lblPas.grid(row=1,column=0,sticky=W)
            txtPas=Entry(LogFrame,font=("arial",13,"bold"),show="*",width=27)
            txtPas.grid(row=1,column=1)
            
            BtnUserA=Button(LogFrame,font=("arial",12,"bold"),text="<~~User",fg="white",bg="orange",padx=17,pady=4,command=User_log)
            BtnUserA.place(x=97,y=80,width=100,height=50)
            
            def Admin_login_button():
                myquary = {"_id":txtAdId.get(),"password":txtPas.get()}
                mylog = myadmin.find(myquary)
                adid=0
                adpas=0
                
                for x in mylog:
                    if x:
                        adid=x["_id"]
                        adpas=x["password"]
                    else:
                        massagebox.showerror('Error','Wrong id  or password')
                
                if txtAdId.get()=='' or txtPas.get()=='':
                    messagebox.showerror('Error','Fields cannot be empty')

                elif (txtAdId.get()=='1' and txtPas.get()=='1') or (txtAdId.get()==adid and txtPas.get()==adpas):
                    messagebox.showinfo('Success','Welcome')
                    Admin_Dashboard()
                    
                    def LogOut_Button():
                        answer = askyesno(title='Logout',message='Are you sure that you want to Logout?')
                        if answer:
                            DataFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="status",fg="#1F7181")
                            DataFrameRight.place(x=450,y=0,width=750,height=540)
                            messagebox.showinfo('Logout','Logout successfull')
                            Admin_Log()
                        else:
                            pass
                    
                    BtnLogOut=Button(LogFrame,font=("arial",12,"bold"),text="LogOut",fg="#1F7181",bg="white",padx=17,pady=4,command=LogOut_Button)
                    BtnLogOut.place(x=97,y=80,width=100,height=50)


                else:
                    messagebox.showerror('Error','Please enter correct c#2490ABentials')
                    
            BtnLog=Button(LogFrame,font=("arial",12,"bold"),text="Login~~>",fg="white",bg="#1F7181",padx=17,pady=4,command=Admin_login_button)
            BtnLog.place(x=245,y=80,width=100,height=50)
            
            
#----New registation-------------------------------------------------------------------------------------    
        def New_Reg(): 
        
            DataFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="status",fg="#1F7181",bg="white")
            DataFrameRight.place(x=450,y=0,width=750,height=540)
        
            def UserRegisterMyDB():
            
                    mydict = { "_id":R_txtUserId.get(),"Pasword": R_txtPasword.get(),"name":R_txtName.get() ,"Father name":R_txtFName.get(),"Mobile":R_txtMn.get() ,"address": R_txtAdd.get() , "Pincode":R_txtPincode.get() ,"Gender":R_comGenderTable.current()}
                    messagebox.showinfo('sucess','User register Seccuss with userId  '+R_txtUserId.get()+'  Pasword  '+R_txtPasword.get())
                    myuser.insert_one(mydict)
                    R_txtUserId.delete(0,END)
                    R_txtPasword.delete(0,END)
                    R_txtName.delete(0,END)
                    R_txtFName.delete(0,END)
                    R_txtMn.delete(0,END)
                    R_txtAdd.delete(0,END)
                    R_txtPincode.delete(0,END)
                    
            def R_Btn_Reg_press():
                if R_txtUserId.get()=='' or R_txtPasword.get()==''or R_txtName.get()=='' or R_txtFName.get()=='' or  R_txtMn.get()=='' or R_txtPincode.get()=='':
                    messagebox.showerror('Error','Fields cannot be empty')
                    
                    
                elif R_Btn_Reg :
                        
                    if R_txtMn.get().isdigit() and len(R_txtMn.get())==10:
                        if R_txtPincode.get().isdigit() and len(R_txtPincode.get())==6:
                            UserRegisterMyDB()
                            #DataFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="status",fg="#1F7181",bg="white")
                            #DataFrameRight.place(x=450,y=0,width=750,height=540)
                            #User_log()
                        else:
                            messagebox.showerror('Error','Enter vailed pincode')
                    else:
                        messagebox.showerror('Error','Enter vailed  Mobile no')
                else:
                    pass

            
            R_lblUserId=Label(DataFrameRight,font=("arial",12,"bold"),text="UserID :",bg="white",padx=2,pady=4)
            R_lblUserId.grid(row=1,column=0,sticky=W)
            R_txtUserId=Entry(DataFrameRight,font=("arial",13),width=50)
            R_txtUserId.grid(row=1,column=1)
            
            R_lblPasword=Label(DataFrameRight,font=("arial",12,"bold"),text="Password :",bg="white",padx=2,pady=4)
            R_lblPasword.grid(row=2,column=0,sticky=W)
            R_txtPasword=Entry(DataFrameRight,font=("arial",13,"bold"),show="*",width=50)
            R_txtPasword.grid(row=2,column=1)
            
            R_lblName=Label(DataFrameRight,font=("arial",12,"bold"),text="Name :",bg="white",padx=2,pady=4)
            R_lblName.grid(row=3,column=0,sticky=W)
            R_txtName=Entry(DataFrameRight,font=("arial",13),width=50)
            R_txtName.grid(row=3,column=1)
            #------------------------------------------------------------------------------------------------------------------------

            R_lblFName=Label(DataFrameRight,font=("arial",12,"bold"),text="Father's Name :",bg="white",padx=2,pady=8)
            R_lblFName.grid(row=4,column=0,sticky=W)
            R_txtFName=Entry(DataFrameRight,font=("arial",13),width=50)
            R_txtFName.grid(row=4,column=1)
            #------------------------------------------------------------------------------------------------------------------------

            R_lblMn=Label(DataFrameRight,font=("arial",12,"bold"),text="Mobile No :",bg="white",padx=2,pady=6)
            R_lblMn.grid(row=5,column=0,sticky=W)
            R_txtMn=Entry(DataFrameRight,font=("arial",13),width=50)
            R_txtMn.grid(row=5,column=1)
            #------------------------------------------------------------------------------------------------------------------------

            R_lblAdd=Label(DataFrameRight,font=("arial",12,"bold"),text="Address :",bg="white",padx=2,pady=6)
            R_lblAdd.grid(row=6,column=0,sticky=W)
            R_txtAdd=Entry(DataFrameRight,font=("arial",13),width=50)
            R_txtAdd.grid(row=6,column=1)
            #------------------------------------------------------------------------------------------------------------------------

            R_lblPincode=Label(DataFrameRight,font=("arial",12,"bold"),text="Pincode :",bg="white",padx=2,pady=6)
            R_lblPincode.grid(row=7,column=0,sticky=W)
            R_txtPincode=Entry(DataFrameRight,font=("arial",13),width=50)
            R_txtPincode.grid(row=7 ,column=1)
            #------------------------------------------------------------------------------------------------------------------------

            R_lblGender=Label(DataFrameRight,font=("arial",12,"bold"),text="Gender :",bg="white",padx=2,pady=6)
            R_lblGender.grid(row=8,column=0,sticky=W)

            R_comGenderTable=ttk.Combobox(DataFrameRight,state="readonly",font=("arial",12),width=48)
            R_comGenderTable['value']=("Male","Female","Other")
            R_comGenderTable.current(0)
            R_comGenderTable.grid(row=8,column=1)
            
            R_Btn_Reg=Button(DataFrameRight,font=("arial",12,"bold"),text="Register",fg="#2490AB",command=R_Btn_Reg_press)
            R_Btn_Reg.place(x=300,y=410,width=100,height=50)
            #------------------------------------------------------------------------------------------------
                    
#------------------------------------------------------------------------------------------------
            
#---user login ----------------------------------------------------------------------------------------------    
        def User_log():
        
            AdminFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Dashboard",fg="#1F7181")
            AdminFrameRight.place(x=450,y=0,width=750,height=540)
            
            def logout():
                answer = askyesno(title='Logout',message='Are you sure logout ')
                if answer:
                    AdminFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Dashboard",fg="#1F7181")
                    AdminFrameRight.place(x=450,y=0,width=750,height=540)
                    User_log()
                else:
                    pass
                    
                    
            def User_login_page():
                
                def Apoinment_Datile_Show_userpage():
                    
                    
                    if MnSearch.get()=='' and NameSearch.get()=='' :
                        messagebox.showerror('Error','Fields cannot be empty or \n Enter vailed ID') 
                        
                    else:
                        myquery = { "name":NameSearch.get(),"Mobile":MnSearch.get()}
                        myapoin = mypasent.find(myquery)
                        print(myapoin)
                    Data="Plase Enter correct datile"
                    id_p='1'
                    for x in myapoin:
                        if x:
                            space='     '
                            MINES='----'
                            LINE='_'
                            dep=x["Department"]
                            Gen=x["Gender"]
                            id_p=x["_id"]
                            Data = MINES*5+" HOSPITAL"+MINES*5+"\n\n"+ space*6+"Date : "+x["Date"]+"   "+x["Currenttime"]+"\n "+dep+"  :"+x["DoctorName"]+"\n"+" ID :"+x["_id" ] + "\n Name : " + x["name" ] + "\n Father's Name : "+x["Father name"]+"\n Gender : "+Gen+"\n Age : "+x["Age"]+"\n Mobil no."+x["Mobile"]+"\n Addresh : "+x["address"]+"\n"+space*2+x["Pincode"]+"\n\n"+LINE*58
                        else:
                            messagebox.showerror('Error','Fields cannot be empty or \n Enter vailed ID')
#------------------------------------------------------------------------------------------------------Edit july 1 2023
                    def viewer():
                        try:
                            billView.bill(id_p)
                        except:
                            print("billviewer not working") 
                    btn_bill=Button(AdminFrameRight,font=("arial",12,"bold"),text="Bill-view",fg="white",bg="#1F7181",command=viewer)
                    btn_bill.place(x=580,y=80,width=130,height=30)
#------------------------------------------------------------------------------------------------------Edit july 1 2023
                    Page=Text(AdminFrameRight,relief=RIDGE,font=("Courier New",15))
                    Page.place(x=0,y=140,width=710,height=350)
                    Page.insert(tk.END, Data)
                    
                    
                myqueary={"_id":txtAdId.get(),"Pasword":txtPas.get()}
                checkid=myuser.find(myqueary)
                x=0
                for x in checkid:
                    if x:
                        x=1
                if x ==1:
                    messagebox.showinfo('Sucess','Login sucess')
                    
                    AdminFrameRight=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Dashboard",fg="#1F7181")
                    AdminFrameRight.place(x=450,y=0,width=750,height=540)
                    Nametxtlbl=Label(AdminFrameRight,font=("arial",12,"bold"),text="Name")
                    Nametxtlbl.place(x=160,y=10)
                    Mntxtlbl=Label(AdminFrameRight,font=("arial",12,"bold"),text="Mobile No.")
                    Mntxtlbl.place(x=380,y=10)
                    
                    def temp_Name_search(e):
                        NameSearch.delete(0,"end")
                        NameSearch.config(fg = 'black')      
                    def temp_Mn_search(e):
                        MnSearch.delete(0,"end")
                        MnSearch.config(fg = 'black')
                        
                        
                    IDtxtlbl=Label(AdminFrameRight,font=("arial",12,"bold"),text="Apointment :",fg="#1F7181")
                    IDtxtlbl.place(x=0,y=40)
                    
                    NameSearch=Entry(AdminFrameRight,font=("arial",13),width=20)
                    NameSearch.insert(0, "Name")
                    NameSearch.config(fg = 'grey')
                    NameSearch.bind("<FocusIn>", temp_Name_search)
                    NameSearch.place(x=160,y=40)

                    MnSearch=Entry(AdminFrameRight,font=("arial",13),width=20)
                    MnSearch.insert(0, "Mobile No.")
                    MnSearch.config(fg = 'grey')
                    MnSearch.bind("<FocusIn>", temp_Mn_search)
                    MnSearch.place(x=380,y=40)

                    btnSearch=Button(AdminFrameRight,font=("arial",12,"bold"),text="Search",fg="white",bg="#1F7181",command=Apoinment_Datile_Show_userpage)
                    btnSearch.place(x=580,y=36,width=130,height=30)
                    
                    BtnLogOut=Button(LogFrame,font=("arial",12,"bold"),text="Logout",fg="#1F7181",bg="white",padx=17,pady=4,command= logout)
                    BtnLogOut.place(x=245,y=80,width=100,height=50)
                    
                    
                else:
                    messagebox.showerror('Error','Wrong Please Enter Vailed Datiles')
            
            LogFrame=LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Login",fg="#2490AB")
            LogFrame.place(x=0,y=380,width=445,height=160)
            
            lblAdId=Label(LogFrame,font=("arial",10,"bold"),text="UserID :",padx=2,pady=6)
            lblAdId.grid(row=0,column=0,sticky=W)
            txtAdId=Entry(LogFrame,font=("arial",13,"bold"),width=27)
            txtAdId.grid(row=0,column=1)
            
            lblPas=Label(LogFrame,font=("arial",13,"bold"),text="Password :",padx=2,pady=6)
            lblPas.grid(row=1,column=0,sticky=W)
            txtPas=Entry(LogFrame,font=("arial",13,"bold"),show="$",width=27)
            txtPas.grid(row=1,column=1)
            
            BtnUserA=Button(LogFrame,font=("arial",12,"bold"),text="Register",fg="white",bg="orange",padx=17,pady=4,command=New_Reg)
            BtnUserA.place(x=97,y=80,width=100,height=50)
            
            BtnLog=Button(LogFrame,font=("arial",12,"bold"),text="Login~~>",fg="white",bg="#1F7181",padx=17,pady=4,command= User_login_page)
            BtnLog.place(x=245,y=80,width=100,height=50)
            
            BtnUndo=Button(LogFrame,font=("arial",12,"bold"),text="<~~",fg="white",bg="#1F7181",padx=17,pady=4,command=Admin_Log)
            BtnUndo.place(x=0,y=80,width=50,height=50)
            
        Login_f()
        
def on_closing():
    #if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
    root.destroy()

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)       
        
#root=Tk()
ob=Hospital(root)
root.mainloop()


# In[ ]: