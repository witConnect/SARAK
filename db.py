import mysql.connector
import math, random 

mydb = mysql.connector.connect(
  host="localhost",
  user="kishore",
  password="Gr8stofa11time",
  database = "Inventory_Management_Final")

mycursor= mydb.cursor()

def generateOTP() : 
	digits = "0123456789"
	OTP = ""  
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)] 
	return OTP 

def check_login(username, password):
    status = False
    mycursor.execute("select * from User")
    user = mycursor.fetchall()
    for item in user:
        user_id = item[0]
        password_db = item[1]
        user_db = item[2]
        if username == user_db:
            print("in")
            if password_db == password:
                status = True
                break

    return status,user_id

def check_email(username):
    status = False
    mycursor.execute("select * from User")
    user = mycursor.fetchall()
    for item in user:
        user_db = item[2]
        if username == user_db:
            status = True
            break
    return status

def changelogin_password(email,password):
    query = f"update User set log_password='{password}' where email='{email}'"
    mycursor.execute(query)
    mydb.commit()

def check_user_type(userid):
    mycursor.execute(f"select count(user_id) from Store_Owner where user_id='{userid}'")
    status = mycursor.fetchall()[0][0]
    print("status:",status)
    if status==0:
        return 1
    else:
        return 2