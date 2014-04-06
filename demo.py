from tkinter import *
import urllib.request
import base64
from db_connect import MySqlConnect

class demo:

    def __init__(self, rootWin):
        self.loginPage()
        self.database = MySqlConnect("academic-mysql.cc.gatech.edu", "cs4400_Group_52", "DDoVXAaM", "cs4400_Group_52").connect()

    def loginPage(self):
        self.mainWin=win 
        self.mainWin.title("GTMRS Login") #forms the title of the GUI
        self.photo=PhotoImage(file="buzz.gif") 
        L=Label(self.mainWin,image=self.photo) #creates a label that has an image variable and the following couple of lines form the GUI
        L.grid(row=0,columnspan=3)
        L1=Label(self.mainWin,text="Username") 
        L1.grid(row=1,column=0)
        L2=Label(self.mainWin,text="Password")
        L2.grid(row=2,column=0)
        self.E1=Entry(self.mainWin,width=30)
        self.E1.grid(row=1,column=1)
        self.E2=Entry(self.mainWin,width=30,show="*") #shows a '*' for every letter you type in and hence the person next to you cannot see the password
        self.E2.grid(row=2,column=1)
        B1=Button(self.mainWin,text="Register",command=self.register) # the button calls the function register
        B1.grid(row=3,column=1,sticky=E)
        B2=Button(self.mainWin,text="Login",command=self.loginCheck) #the button calls the function loginCheck
        B2.grid(row=3,column=2)

    def register(self):
        self.mainWin.withdraw() #withdraws the loginPage GUI 
        self.secondWin=Toplevel() #froms a second tkinter window 
        self.secondWin.title("GTMRS New User Registration") # the title for the GUI
        L=Label(self.secondWin,image=self.photo) # Creates a Label with the image variable which will call the image we formed in the previous function and the other following lines of code form the rest of the GUI 
        L.grid(row=0,columnspan=4)
        L1=Label(self.secondWin,text="Username:")
        L1.grid(row=2,column=0,sticky=W)
        L2=Label(self.secondWin,text="Password:")
        L2.grid(row=3,column=0,sticky=W)
        L3=Label(self.secondWin,text="Confirm Password:")
        L3.grid(row=4,column=0,sticky=W)
        L5=Label(self.secondWin,text="Name:")
        L5.grid(row=1,column=0,sticky=W)
        L4=Label(self.secondWin,text="Type:")
        L4.grid(row=5,column=0,sticky=W)
        self.w = Spinbox(self.secondWin,values=( "Patient","Doctor", "Admin"))
        self.w.grid(row=5,column=1,sticky=W)
        self.E11=Entry(self.secondWin,width=30)
        self.E11.grid(row=2,column=1)
        self.E21=Entry(self.secondWin,width=30,show="*")
        self.E21.grid(row=3,column=1)
        self.E31=Entry(self.secondWin,width=30,show="*")
        self.E31.grid(row=4,column=1)
        self.E41=Entry(self.secondWin,width=30,)
        self.E41.grid(row=1,column=1)
        B1=Button(self.secondWin,text="Cancel",command=self.cancel) #the Button calls the function cancel 
        B1.grid(row=6,column=1,sticky=E)
        B2=Button(self.secondWin,text="Register",command=self.registerNew) #the button calls the function registerNew
        B2.grid(row=6,column=2,sticky=E)

    def cancel(self):
        self.secondWin.destroy() #destroys the second GUI, the registration page
        self.mainWin.deiconify() #it 'shows' the main GUI, the login page

    def loginCheck(self):
        self.username=self.E1.get() #gets the username from the entry widget 
        self.password=self.E2.get() #gets the password from the entry widget 
        cursor=self.database.cursor() #forms a cursor 
        sql="SELECT * FROM PATIENT WHERE Username=%s and Password=%s" #forms the sql query that will check for the username in the existing database
        a=cursor.execute(sql,(self.username,self.password)) #executes the query
        
        if a==1:
            message2=messagebox.showinfo("Login Successful","Login Successful") #if the login is successful, it'll return a message saying the same.
        else:
            message3=messagebox.showwarning("Login Unsuccessful","Wrong Username/password combination, please try again") #if the login is unsuccessful, it'll return a message saying the user to check his/her username/password combo

        cursor.close()
        self.database.commit()
        self.mainWin.withdraw()

    def registerNew(self):
        self.newUsername=self.E11.get()#get the firstname from the entry widget
        self.newPassword=self.E21.get() #gets the username from the entry widget
        self.confirmNewPassword=self.E31.get()#gets the password from the entry widget
        if self.newUsername.strip()=="": 
            message6=messagebox.showinfo("Registration Failed!","Please enter a Username!") #if the username is an empty string, raises an error and asks the user to input a username
        elif self.newPassword.strip()=="":
            message7=messagebox.showinfo("Registration Failed!","Please enter a Password!") #if the password is an empty string, raises an error and asks the user to input a password

        elif self.newPassword != self.confirmNewPassword:
            message4=messagebox.showinfo("Registration Unsuccessful","Passwords dont match, please try again") #if the passwords do not match, it shows a messagebox telling the user the same.
        else:
            
            cursor=self.database.cursor() #forms a cursor 
            sql1="SELECT * FROM PATIENT WHERE Username=%s" #forms a query which checks if the username already exists in the database
            b=cursor.execute(sql1,(self.newUsername)) #executes the query 
            if b >0:
                message5=messagebox.showinfo("Registration Unsuccessful","Username already taken") #if the username is taken, it shows a messagebox telling the user that the username is already taken 
            else:
                usertype=self.w.get()
                if usertype == "Patient":
                    self.patientLogin()
##                    sql="INSERT INTO PATIENT (Username,Password,Name) VALUES (%s,%s,%s)"#if the username is not already taken, it forms a query that inserts the data into the database
##                    w=cursor.execute(sql,(newUsername,newPassword,name)) #it executes the query
##                    message8=messagebox.showinfo("Registration Successful!","Registration Successful") #pops a message box telling the user that the registration was successful
                elif usertype == "Doctor":
                    self.doctorLogin()
##                    sql="INSERT INTO DOCTOR (Username,Password) VALUES (%s,%s)"#if the username is not already taken, it forms a query that inserts the data into the database
##                    x=cursor.execute(sql,(newUsername,newPassword)) #it executes the query
##                    message8=messagebox.showinfo("Registration Successful!","Registration Successful") #pops a message box telling the user that the registration was successful

                else:
                    sql="INSERT INTO ADMINISTRATION_PERSONNEL (Username,Password) VALUES (%s,%s)"#if the username is not already taken, it forms a query that inserts the data into the database
                    y=cursor.execute(sql,(self.newUsername,self.newPassword)) #it executes the query
                    message8=messagebox.showinfo("Registration Successful!","Registration Successful") #pops a message box telling the user that the registration was successful
                    self.adminHomepage()
                
                
            cursor.close()
            self.database.commit()

    def patientLogin(self):
        self.secondWin.destroy()
        self.patientloginWin=Tk()
        self.patientloginWin.title("GTMRS New Patient Registration") # the title for the GUI
        L=Label(self.patientloginWin,text="image goes here!") # Creates a Label with the image variable which will call the image we formed in the previous function and the other following lines of code form the rest of the GUI 
        L.grid(row=0,columnspan=4)
        L1=Label(self.patientloginWin,text="Patient Name:")
        L1.grid(row=1,column=0,sticky=W)
        L2=Label(self.patientloginWin,text="Date of Birth:")
        L2.grid(row=2,column=0,sticky=W)
        L3=Label(self.patientloginWin,text="Gender:")
        L3.grid(row=3,column=0,sticky=W)
        L4=Label(self.patientloginWin,text="Address:")
        L4.grid(row=4,column=0,sticky=W)
        L5=Label(self.patientloginWin,text="Home Phone:")
        L5.grid(row=5,column=0,sticky=W)
        L6=Label(self.patientloginWin,text="Work Phone:")
        L6.grid(row=6,column=0,sticky=W)
        L7=Label(self.patientloginWin,text="Weight (in pounds):")
        L7.grid(row=7,column=0,sticky=W)
        L8=Label(self.patientloginWin,text="Height (in inches):")
        L8.grid(row=8,column=0,sticky=W)
        L9=Label(self.patientloginWin,text="Annual Income:")
        L9.grid(row=9,column=0,sticky=W)
        L10=Label(self.patientloginWin,text="Allergies:")
        L10.grid(row=10,column=0,sticky=W)
        self.w = Spinbox(self.patientloginWin,values=( "Male","Female"))
        self.w.grid(row=3,column=1,sticky=W)
        var=StringVar(self.patientloginWin)
        var.set("$0-$25,000")
        self.menu=OptionMenu(self.patientloginWin,var, "$0-$25,000","$25,000-$50,000","$50,000-$75,000","$75,000-$100,000","$100,000+")
        self.menu.grid(row=9,column=1,sticky=W)
        self.E1=Entry(self.patientloginWin,width=30)
        self.E1.grid(row=1,column=1)
        self.E2=Entry(self.patientloginWin,width=30)
        self.E2.grid(row=2,column=1)
        self.E3=Entry(self.patientloginWin,width=30)
        self.E3.grid(row=4,column=1)
        self.E4=Entry(self.patientloginWin,width=30)
        self.E4.grid(row=5,column=1)
        self.E5=Entry(self.patientloginWin,width=30)
        self.E5.grid(row=6,column=1)
        self.E6=Entry(self.patientloginWin,width=30)
        self.E6.grid(row=7,column=1)
        self.E7=Entry(self.patientloginWin,width=30)
        self.E7.grid(row=8,column=1)
        self.E8=Entry(self.patientloginWin,width=30)
        self.E8.grid(row=10,column=1)
        B1=Button(self.patientloginWin,text="Cancel",command=self.cancel) #the Button calls the function cancel 
        B1.grid(row=11,column=1,sticky=E)
        B2=Button(self.patientloginWin,text="Register",command=self.patientregis) #the button calls the function registerNew
        B2.grid(row=11,column=2,sticky=E)
        a="+ Add more Allergies"
        L111=Label(self.patientloginWin,text=a, foreground="#0000ff")
        L111.bind("<1>", lambda event, text=a: \
                  self.click_Test())
        L111.grid(row=10, column = 3, sticky=W)

    def click_Test(self):
        print("Still need to finish the addition of extra allergy entries!")
        
        


    def doctorLogin(self):
        self.secondWin.destroy()
        self.doctorloginWin=Tk()
        self.doctorloginWin.title("GTMRS New Doctor Registration") # the title for the GUI
        L=Label(self.doctorloginWin,text="image goes here!") # Creates a Label with the image variable which will call the image we formed in the previous function and the other following lines of code form the rest of the GUI 
        L.grid(row=0,columnspan=4)
        L1=Label(self.doctorloginWin,text="License Number:")
        L1.grid(row=1,column=0,sticky=W)
        L2=Label(self.doctorloginWin,text="First Name:")
        L2.grid(row=2,column=0,sticky=W)
        L3=Label(self.doctorloginWin,text="Last Name:")
        L3.grid(row=3,column=0,sticky=W)
        L4=Label(self.doctorloginWin,text="Date of Birth:")
        L4.grid(row=4,column=0,sticky=W)
        L5=Label(self.doctorloginWin,text="Work Phone:")
        L5.grid(row=5,column=0,sticky=W)
        L6=Label(self.doctorloginWin,text="Speciality:")
        L6.grid(row=6,column=0,sticky=W)
        L7=Label(self.doctorloginWin,text="Room Number:")
        L7.grid(row=7,column=0,sticky=W)
        L8=Label(self.doctorloginWin,text="Home Address:")
        L8.grid(row=8,column=0,sticky=W)
        L9=Label(self.doctorloginWin,text="Availabilty:")
        L9.grid(row=9,column=0,sticky=W)
        L10=Label(self.doctorloginWin,text="From:")
        L10.grid(row=9,column=2,sticky=W)
        L11=Label(self.doctorloginWin,text="To:")
        L11.grid(row=9,column=4,sticky=W)
        var1=StringVar(self.doctorloginWin)
        var1.set("Monday")
        self.menu1=OptionMenu(self.doctorloginWin,var1, "Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday","Sunday")
        self.menu1.grid(row=9,column=1,sticky=W)
        var2=StringVar(self.doctorloginWin)
        var2.set("Heart Specialist")
        self.menu2=OptionMenu(self.doctorloginWin,var2, "Heart Specialist","Eye Specialist","Brain Specialist","Somethingelse Specialist","Blah Specialist", "Xinyi","hulalala")
        self.menu2.grid(row=6,column=1,sticky=W)
        var3=StringVar(self.doctorloginWin)
        var3.set("12:00 am")
        self.menu3=OptionMenu(self.doctorloginWin,var3, "12:00 am", "12:30 am","1:00 am","1:30 am","2:00 am","2:30 am","3:00 am","3:30 am","4:00 am","4:30 am","5:00 am","5:30 am","6:00 am","6:30 am","7:00 am","7:30 am","8:00 am","8:30 am","9:00 am","9:30 am","10:00 am","10:30 am","11:00 am","11:30 am","12:00 pm", "12:30 pm","1:00 pm","1:30 pm","2:00 pm","2:30 pm","3:00 pm","3:30 pm","4:00 pm","4:30 pm","5:00 pm","5:30 pm","6:00 pm","6:30 pm","7:00 pm","7:30 pm","8:00 pm","8:30 pm","9:00 pm","9:30 pm","10:00 pm","10:30 pm","11:00 pm","11:30 pm")
        self.menu3.grid(row=9,column=3,sticky=W)
        var4=StringVar(self.doctorloginWin)
        var4.set("12:00 am")
        self.menu4=OptionMenu(self.doctorloginWin,var4, "12:00 am", "12:30 am","1:00 am","1:30 am","2:00 am","2:30 am","3:00 am","3:30 am","4:00 am","4:30 am","5:00 am","5:30 am","6:00 am","6:30 am","7:00 am","7:30 am","8:00 am","8:30 am","9:00 am","9:30 am","10:00 am","10:30 am","11:00 am","11:30 am","12:00 pm", "12:30 pm","1:00 pm","1:30 pm","2:00 pm","2:30 pm","3:00 pm","3:30 pm","4:00 pm","4:30 pm","5:00 pm","5:30 pm","6:00 pm","6:30 pm","7:00 pm","7:30 pm","8:00 pm","8:30 pm","9:00 pm","9:30 pm","10:00 pm","10:30 pm","11:00 pm","11:30 pm")
        self.menu4.grid(row=9,column=5,sticky=W)
        self.E10=Entry(self.doctorloginWin,width=30)
        self.E10.grid(row=1,column=1, columnspan=3)
        self.E20=Entry(self.doctorloginWin,width=30)
        self.E20.grid(row=2,column=1, columnspan=3)
        self.E30=Entry(self.doctorloginWin,width=30)
        self.E30.grid(row=3,column=1, columnspan=3)
        self.E40=Entry(self.doctorloginWin,width=30)
        self.E40.grid(row=4,column=1, columnspan=3)
        self.E50=Entry(self.doctorloginWin,width=30)
        self.E50.grid(row=5,column=1, columnspan=3)
        self.E60=Entry(self.doctorloginWin,width=30)
        self.E60.grid(row=7,column=1, columnspan=3)
        self.E70=Entry(self.doctorloginWin,width=30)
        self.E70.grid(row=8,column=1, columnspan=3)
        B1=Button(self.doctorloginWin,text="Cancel",command=self.cancel) #the Button calls the function cancel 
        B1.grid(row=10,column=4,sticky=E)
        B2=Button(self.doctorloginWin,text="Register",command=self.doctorregis) #the button calls the function registerNew
        B2.grid(row=10,column=5,sticky=E)
        a="+ Add Availability"
        L111=Label(self.doctorloginWin,text=a, foreground="#0000ff")
        L111.bind("<1>", lambda event, text=a: \
                  self.click_Test())
        L111.grid(row=9, column = 6, sticky=W)

    def patientregis(self):
        message=messagebox.showinfo(title="Registration Successful", message="Registration Successful!")
        self.patientloginWin.withdraw()
        self.patientHomepage()

    def doctorregis(self):
        message=messagebox.showinfo(title="Registration Successful", message="Registration Successful!")
        self.doctorloginWin.withdraw()
        self.doctorHomepage()


    def patientHomepage(self):
        self.patientHomepageWin=Tk()
        self.patientHomepageWin.title("Patient Home Page")
        self.patientHomepageWin.minsize(400,100)
        text1="Make Appointments"
        Limage=Label(self.patientHomepageWin,text="Image goes here!")
        Limage.grid(row=0, column=1, columnspan=3)
        L=Label(self.patientHomepageWin,text=text1, foreground="#0000ff")
        L.bind("<1>", lambda event, text=text1: \
                  self.click_Test())
        L.grid(row=1, column =1, columnspan =3, sticky=W,padx=10)
        text2="View Visit History"
        L1=Label(self.patientHomepageWin,text=text2, foreground="#0000ff")
        L1.bind("<1>", lambda event, text=text2: \
                  self.click_Test())
        L1.grid(row=2, column = 1, columnspan =3, sticky=W,padx=10)
        text3="Order Medication"
        L2=Label(self.patientHomepageWin,text=text3, foreground="#0000ff")
        L2.bind("<1>", lambda event, text=text3: \
                  self.click_Test())
        L2.grid(row=3, column = 1, columnspan =3, sticky=W,padx=10)
        text4="Communicate"
        L3=Label(self.patientHomepageWin,text=text4, foreground="#0000ff")
        L3.bind("<1>", lambda event, text=text4: \
                  self.click_Test())
        L3.grid(row=4, column = 1, columnspan =3, sticky=W,padx=10)
        text5="Rate a Doctor"
        L4=Label(self.patientHomepageWin,text=text5, foreground="#0000ff")
        L4.bind("<1>", lambda event, text=text5: \
                  self.click_Test())
        L4.grid(row=5, column = 1, columnspan =3, sticky=W,padx=10)
        text6="Edit Profile"
        L5=Label(self.patientHomepageWin,text=text6, foreground="#0000ff")
        L5.bind("<1>", lambda event, text=text6: \
                  self.click_Test())
        L5.grid(row=6, column = 1, columnspan =3, sticky=W,padx=10)
        
        

    def adminHomepage(self):
        self.secondWin.withdraw()
        self.adminHomepageWin=Tk()
        self.adminHomepageWin.title("Administration Personnel Homepage")
        self.adminHomepageWin.minsize(300,100)
        text1="Billing"
        Limage=Label(self.adminHomepageWin,text="Image goes here!")
        Limage.grid(row=0, column=1, columnspan=3)
        L=Label(self.adminHomepageWin,text=text1, foreground="#0000ff")
        L.bind("<1>", lambda event, text=text1: \
                  self.click_Test())
        L.grid(row=1, column =1, columnspan =3, padx=50)
        text2="Doctor Performance Report"
        L1=Label(self.adminHomepageWin,text=text2, foreground="#0000ff")
        L1.bind("<1>", lambda event, text=text2: \
                  self.click_Test())
        L1.grid(row=2, column = 1, columnspan =3,  padx=50)
        text3="Surgery Report"
        L2=Label(self.adminHomepageWin,text=text3, foreground="#0000ff")
        L2.bind("<1>", lambda event, text=text3: \
                  self.click_Test())
        L2.grid(row=3, column = 1, columnspan =3,  padx=50)
        text4="Patient Visit Report"
        L3=Label(self.adminHomepageWin,text=text4, foreground="#0000ff")
        L3.bind("<1>", lambda event, text=text4: \
                  self.click_Test())
        L3.grid(row=4, column = 1, columnspan =3,  padx=50)



    def doctorHomepage(self):
        self.doctorHomepageWin=Tk()
        self.doctorHomepageWin.title("Doctor Home Page")
        self.doctorHomepageWin.minsize(400,100)
        text1="View Appointments Calender"
        Limage=Label(self.doctorHomepageWin,text="Image goes here!")
        Limage.grid(row=0, column=1, columnspan=3)
        L=Label(self.doctorHomepageWin,text=text1, foreground="#0000ff")
        L.bind("<1>", lambda event, text=text1: \
                  self.click_Test())
        L.grid(row=1, column =1, columnspan =3, sticky=W,padx=10)
        text2="Patient Visits"
        L1=Label(self.doctorHomepageWin,text=text2, foreground="#0000ff")
        L1.bind("<1>", lambda event, text=text2: \
                  self.click_Test())
        L1.grid(row=2, column = 1, columnspan =3, sticky=W,padx=10)
        text3="Record a Surgery"
        L2=Label(self.doctorHomepageWin,text=text3, foreground="#0000ff")
        L2.bind("<1>", lambda event, text=text3: \
                  self.click_Test())
        L2.grid(row=3, column = 1, columnspan =3, sticky=W,padx=10)
        text4="Communicate"
        L3=Label(self.doctorHomepageWin,text=text4, foreground="#0000ff")
        L3.bind("<1>", lambda event, text=text4: \
                  self.click_Test())
        L3.grid(row=4, column = 1, columnspan =3, sticky=W,padx=10)
        text5="Edit Profile"
        L4=Label(self.doctorHomepageWin,text=text5, foreground="#0000ff")
        L4.bind("<1>", lambda event, text=text5: \
                  self.click_Test())
        L4.grid(row=5, column = 1, columnspan =3, sticky=W,padx=10)
 
        

win=Tk()
app=demo(win)
win.mainloop()
