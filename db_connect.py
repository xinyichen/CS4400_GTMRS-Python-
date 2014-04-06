import pymysql

class MySqlConnect:

    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
    
    def connect(self):
        try:
            #tries to connect to the database
            return pymysql.connect(self.host, self.user, self.passwd, self.db)
        except:
            raise Exception("Unable to connect to the database")
