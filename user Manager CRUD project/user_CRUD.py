from pydoc import Helper
import mysql.connector as connector



class Dbhelper:
    # default constructor 
    def __init__(self): 
        self.con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='raj@28022002',
                        database='pythontest')
        query = 'create table if not exists user(userid int primary key , username varchar(200),phone varchar(20))'                
        cur =self.con.cursor()
        cur.execute(query)
        print("created")
    

    def insert_user(self , userid , username , phone):
        query = "insert into user(userid,username,phone) values ({} ,'{}' ,'{}')".format(userid , username , phone)   
        cur =self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print(query)
        print("user data inserted")
        print()

    def delete_user(self , userid):
        query = "delete from user where userid = {}".format(userid)
        cur =self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print(query)
        print("user {} id deleted ".format(userid))
        print()

        
    def display_users(self) :
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query) 
        
        for row in cur:
            print("user id : {} \n user name :'{}' \nphone : '{}'".format(row[0] ,row[1] ,row[2]))
            print()


    def update_user(self,userid , name , phonenum):
        query = "update user set username  = '{}' ,phone ='{}' where userid = {}".format(name , phonenum , userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")



#main
helper = Dbhelper()        


helper.display_users()

