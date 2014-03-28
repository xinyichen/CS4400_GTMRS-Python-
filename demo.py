from tkinter import *
import pymysql
import urllib.request
import base64


class demo:

    def __init__(self, rootWin):
        self.loginPage()

    def loginPage(self):
        self.mainWin=win 
        self.mainWin.title("GT Login") #forms the title of the GUI
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
        self.secondWin.title("GT Chat New User Registration") # the title for the GUI
##        L=Label(self.secondWin,image=self.photo) # Creates a Label with the image variable which will call the image we formed in the previous function and the other following lines of code form the rest of the GUI 
##        L.grid(row=0,columnspan=4)
        L1=Label(self.secondWin,text="Name")
        L1.grid(row=1,column=0,sticky=W)
        L2=Label(self.secondWin,text="Username")
        L2.grid(row=2,column=0,sticky=W)
        L3=Label(self.secondWin,text="Password")
        L3.grid(row=3,column=0,sticky=W)
        L4=Label(self.secondWin,text="Confirm Password")
        L4.grid(row=4,column=0,sticky=W)
        self.E11=Entry(self.secondWin,width=30)
        self.E11.grid(row=1,column=1)
        self.E21=Entry(self.secondWin,width=30)
        self.E21.grid(row=2,column=1)
        self.E31=Entry(self.secondWin,width=30,show="*")
        self.E31.grid(row=3,column=1)
        self.E41=Entry(self.secondWin,width=30,show="*")
        self.E41.grid(row=4,column=1)
        B1=Button(self.secondWin,text="Cancel",command=self.cancel) #the Button calls the function cancel 
        B1.grid(row=5,column=1,sticky=E)
        B2=Button(self.secondWin,text="Register",command=self.registerNew) #the button calls the function registerNew
        B2.grid(row=5,column=2,sticky=E)

    def cancel(self):
        self.secondWin.destroy() #destroys the second GUI, the registration page
        self.mainWin.deiconify() #it 'shows' the main GUI, the login page

    def connect(self):
        try:
            db=pymysql.connect(host="academic-mysql.cc.gatech.edu",user="cs4400_Group_52",passwd="DDoVXAaM",db="cs4400_Group_52") #tries to connect to the database
            print("Success!!! YOU ROCK MAN!!!!")
        except:
            message=messagebox.showwarning("Unable to connect to the database!","Please check your internet connection!") #if it does not connect to the database, it pops up a showwarning message box that tells the user to check their internet connection.
        return db

    def loginCheck(self):
        database=self.connect() #calls the connect function 
        self.username=self.E1.get() #gets the username from the entry widget 
        self.password=self.E2.get() #gets the password from the entry widget 
        cursor=database.cursor() #forms a cursor 
        sql="SELECT * FROM PATIENT WHERE Username=%s and Password=%s" #forms the sql query that will check for the username in the existing database
        a=cursor.execute(sql,(self.username,self.password)) #executes the query
        
        if a==1:
            message2=messagebox.showinfo("Login Successful","Login Successful") #if the login is successful, it'll return a message saying the same.
        else:
            message3=messagebox.showwarning("Login Unsuccessful","Wrong Username/password combination, please try again") #if the login is unsuccessful, it'll return a message saying the user to check his/her username/password combo

        cursor.close()
        database.commit()
        self.mainWin.withdraw()

    def registerNew(self):
        database=self.connect() #calls the connect function in order to connect to the database
        firstname=self.E11.get()#get the firstname from the entry widget
        newUsername=self.E21.get() #gets the username from the entry widget
        newPassword=self.E31.get()#gets the password from the entry widget
        confirmNewPassword=self.E41.get()#gets the password from the entry widget
        if newUsername.strip()=="": 
            message6=messagebox.showinfo("Registration Failed!","Please enter a Username!") #if the username is an empty string, raises an error and asks the user to input a username
        elif newPassword.strip()=="":
            message7=messagebox.showinfo("Registration Falied!","Please enter a Password!") #if the password is an empty string, raises an error and asks the user to input a password

        elif newPassword != confirmNewPassword:
            message4=messagebox.showinfo("Registration Unsuccessful","Passwords dont match, please try again") #if the passwords do not match, it shows a messagebox telling the user the same.
        else:
        
            cursor=database.cursor() #forms a cursor 
            sql1="SELECT * FROM PATIENT WHERE Username=%s" #forms a query which checks if the username already exists in the database
            b=cursor.execute(sql1,(newUsername)) #executes the query 
            if b >0:
                message5=messagebox.showinfo("Registration Unsuccessful","Username already taken") #if the username is taken, it shows a messagebox telling the user that the username is already taken 
            else:
                sql="INSERT INTO PATIENT (Username,Password,Name) VALUES (%s,%s,%s)"#if the username is not already taken, it forms a query that inserts the data into the database
                a=cursor.execute(sql,(newUsername,newPassword,firstname)) #it executes the query
                message8=messagebox.showinfo("Registration Succcessful!","Registration Successful") #pops a message box telling the user that the registration was successful
            cursor.close()
            database.commit()
        



        

win=Tk()
app=demo(win)
win.mainloop()
