import mysql.connector as msc
from tabulate import tabulate

db = msc.connect(host = 'localhost',
                 user = 'kishore',
                 password = 'Gr8stofa11time',
                 database = 'Inventory_Management_Final'
                 )

def store(sid):
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT store_id,product_id,quantity,reorder_lvl
                     FROM Inventory WHERE store_id = {sid}''')
    rows = mycursor.fetchall()
    db.commit()
    mycursor.close()

    return (rows)


    
def reorder(sid):
    mycursor = db.cursor()
    mycursor.execute(f'''update Inventory
                    set
                    quantity = quantity + reorder_lvl 
                    where
                    reorder_lvl >= quantity and store_id = {sid};''')
    db.commit()
    mycursor.close()
     

def update(sid,pid,quan):
    mycursor = db.cursor()
    mycursor.execute(f'''update Inventory
                    set
                    quantity = {quan}
                    where
                    product_id = {pid};''')
    db.commit()
    mycursor.close()

def create(sid,pid,quan,re_lvl):
    mycursor = db.cursor()
    mycursor.execute(f'''CALL Inventory_Management_Final.add_item({sid},{pid},{quan},{re_lvl})''')
    mycursor.close()
    db.commit()