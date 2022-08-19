
from os import system
from socket import create_connection
import mysql.connector as connector
from datetime import date
from tabulate import tabulate

mydb = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='raj@28022002')


mycursor = mydb.cursor()

today = date.today()
d1 = today.strftime("%Y/%m/%d")

def DataBase_Creation():
    database_create = "CREATE DATABASE IF NOT EXISTS student_records"
    mycursor.execute(database_create)
    mycursor.execute("use student_records")

    # sql table create_connection
    student_data_table = ''' CREATE TABLE IF NOT EXISTS student_data
    ( sid int primary key AUTO_INCREMENT,
      name varchar(35) NOT NULL,
      rollNo int NOT NULL ,
      dob date , 
      phone char(10),
      city char(30),
      branch char(34)     
    ) '''
    
    
    student_marks_table = ''' CREATE TABLE IF NOT EXISTS student_marks
      (
        tid int primary key AUTO_INCREMENT,
        sid int NOT NULL , 
        s_roll int ,
        branch char(34) ,
        pass_year int , 
        total_marks int 
      )'''
    
    fees_table =''' CREATE TABLE IF NOT EXISTS fees
    (
        fid int  primary key AUTO_INCREMENT,
        rollNo int ,
        sid int NOT NULL,
        amount int , 
        pay_date date , 
        mode_of_payment char(35)
    )'''
    
    

    mycursor.execute(student_data_table)
    mycursor.execute(student_marks_table)
    mycursor.execute(fees_table)


#functions to acess the table

#VIEW DATA 
def show_student_data():
    query = "SELECT * FROM student_data ORDER BY sid"
    mycursor.execute(query)
    res = mycursor.fetchall()
    return res

def show_marks_data():
    query = "SELECT * FROM student_marks ORDER BY tid"
    mycursor.execute(query)
    res = mycursor.fetchall()
    return res

def show_fees_data():
    query = "SELECT * FROM fees ORDER BY fid"
    mycursor.execute(query)
    res = mycursor.fetchall()
    return res        

#ADDING DATA
def add_Student_data():
    name = input("Enter Student Name : ")
    rollno = int(input("Enter Roll No : "))
    dob = input("Enter DOB (yyyy/mm/dd) : ")
    branch = input("Enter Branch : ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City : ")

    val = (name , rollno ,dob , phone ,city ,branch)

    query = "INSERT INTO  student_data(name , rollno ,dob , phone ,city ,branch) VALUES {}".format(val)

    mycursor.execute(query)
    mydb.commit()


def add_marks_data():
    sid = int(input("Enter Student id : "))
    s_roll = int(input("Enter Roll No : "))
    pass_year = int(input("Enter pass_year (yyyy) : "))
    branch = input("Enter Branch : ")
    t_marks = int(input("Total Marks : "))

    val = (sid ,s_roll, branch,pass_year , t_marks)

    query = "INSERT INTO  student_marks(sid ,s_roll  ,branch ,pass_year  , total_marks) VALUES {}".format(val)

    mycursor.execute(query)
    mydb.commit()


def add_fess_data():
    sid = int(input("Enter Student id : "))
    rollNo = int(input("Enter Roll No : "))
    amount = int(input("Enter fees Amount: "))
    paydate = input("Enter PayDate(yyyy/mm/dd) : ")
    mode_of_payment = input("Enter Mode.of.Payment(CARD/UPI/NEFT/RTGS/STUDENT LOAN/OTHER): ")

    val = (sid , rollNo , amount,paydate , mode_of_payment)
    query = "INSERT INTO  fees(sid , rollNo , amount , pay_date ,mode_of_payment) VALUES {}".format(val)

    mycursor.execute(query)
    mydb.commit()



DataBase_Creation()


while(True):
    
    print()
    print("-Main Menu-")
    data = []
    print()
    print("1.Show student Details\n2.add Student\n3.Show marks \n4.Add Student Marks\n5.Show fees Data\n6.to add fees \n7.Exit")   

    n = int(input("Enter your Choice : "))

    if (n==1):
        res = show_student_data()
        for x in res:
            data.append(x)
        table = tabulate(data ,headers= ['Name ', 'Rollno' ,'DOB' , 'phone','City' ,'Branch'] )    
        print(table)

    if(n==2):
        add_Student_data()

    if(n==3):
        res = show_marks_data()
        for x in res:
            data.append(x)
        table = tabulate(data ,headers= ['s_id' ,'s_roll', 'branch','pass_year' , 'total_marks'] )    
        print(table)

    if(n==4):
        add_marks_data()

    if(n==5):
        res= show_fees_data()
        for x in res:
            data.append(x)
        table = tabulate(data ,headers= ['rollNo' ,'sid'  , 'amount' , 'paydate' ,'mode_of_payment'] )    
        print(table)

    if(n==6):
        add_fess_data()

    if(n==7):
        exit()   