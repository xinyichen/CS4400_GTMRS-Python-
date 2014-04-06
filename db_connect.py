import pymysql

class MySqlConnect:

    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
    
    def connect(self):
        try:
            db = pymysql.connect(self.host, self.user, self.passwd, self.db) #tries to connect to the database
        except:
            message = messagebox.showwarning("Unable to connect to the database!","Please check your internet connection!") #if it does not connect to the database, it pops up a showwarning message box that tells the user to check their internet connection.
        return db
