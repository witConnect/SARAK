import mysql.connector as msc
from tabulate import tabulate

db = msc.connect(host = 'localhost',
                 user = 'kishore',
                 passwd = 'Gr8stofa11time',
                 database = 'Inventory_Management_Final'
                 )


def store_count(uid):
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT `Stores Owned` FROM store_count
                            where user_id = {uid};''')
    rows = mycursor.fetchall()
    mycursor.close()
    return (rows)


def store_info(sid,uid):
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT * FROM store_info WHERE
                        store_id = {sid} and user_id = {uid}''')
    rows = mycursor.fetchall()
    mycursor.close()
    return rows

def all_store_info(uid):
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT * FROM store_info WHERE user_id = {uid}''')
    rows = mycursor.fetchall()
    mycursor.close()
    return rows



def owner_name(uid):
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT CONCAT(first_name ,' ', last_name) AS `Name`
                     FROM Store_Owner WHERE Store_Owner.user_id = {uid}''')
    rows = mycursor.fetchall()
    mycursor.close()
    return(rows)


def add_store(sid,uid,s_name,street,city,state,pin):
    mycursor = db.cursor()
    mycursor.execute(f'''CALL Inventory_Management_Final.insert_store({sid},{uid},'{s_name}','{street}','{city}','{state}',{pin})''')
    mycursor.execute('commit')
    mycursor.close()
    return True
    
def remove_store(sid):
    mycursor = db.cursor()
    mycursor.execute(f'''CALL Inventory_Management_Final.remove_store({sid})''')
    mycursor.execute('commit')
    mycursor.close()
    return True

def change_password(uid,new_password,confirm_password):
    mycursor = db.cursor()
    if new_password == confirm_password:
        mycursor.execute(f'''UPDATE User
                            SET log_password = '{confirm_password}'
                            WHERE user_id = {uid}''')
        mycursor.execute('commit')
        mycursor.close()
        return True
    mycursor.close()
    return False


        
