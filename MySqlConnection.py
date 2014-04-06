import pymysql

def connect():
    try:
        db=pymysql.connect(host="academic-mysql.cc.gatech.edu",user="cs4400_Group_52",passwd="DDoVXAaM",db="cs4400_Group_52") #tries to connect to the database
    except:
        message=messagebox.showwarning("Unable to connect to the database!","Please check your internet connection!") #if it does not connect to the database, it pops up a showwarning message box that tells the user to check their internet connection.
    return db
