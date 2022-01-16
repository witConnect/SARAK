import mysql.connector as msc
from tabulate import tabulate

database = msc.connect(host = 'localhost',
                 user = 'kishore',
                 passwd = 'Gr8stofa11time',
                 database = 'Inventory_Management_Final'
                 )


def supplier_info ( uid ) :
    mycursor = database.cursor()
    mycursor.execute (f'''SELECT distinct(S.supplier_first_name) as NAME FROM Supplier AS S  WHERE S.user_id = {uid}''')  
    rows = mycursor.fetchall()
    mycursor.close()
    return ( rows )


def products_supplied ( uid ) :
    mycursor = database.cursor()
    mycursor.execute(f'''SELECT S.product_id,P.product_name,P.product_type FROM Supplier AS S 
    INNER JOIN Product AS P USING (product_id) WHERE S.user_id = {uid}''')
    rows = mycursor.fetchall()
    x = mycursor.column_names
    mycursor.close()
    return rows

def adding_item( pid ,uid ,pname ,ptype ):
    try:
        mycursor = database.cursor()
        mycursor.execute (f'''insert into Product values({pid},'{pname}','{ptype}')''')
        mycursor.execute("commit")
        mycursor.close()

        mycursor = database.cursor()
        mycursor.execute (f'''SELECT distinct(S.supplier_last_name) as NAME FROM Supplier AS S WHERE S.user_id = {uid}''')  
        rows = mycursor.fetchall()
        supplier_first_name = rows[0][0]
        print(supplier_first_name)
        mycursor.close()

        mycursor = database.cursor()
        mycursor.execute (f'''SELECT distinct(S.supplier_last_name) as NAME FROM Supplier AS S  WHERE S.user_id = {uid}''')  
        rows = mycursor.fetchall()
        supplier_last_name = rows[0][0]
        print(supplier_last_name)
        mycursor.close()

        mycursor = database.cursor()
        mycursor.execute (f'''INSERT INTO Supplier VALUES({uid},"{supplier_first_name}","{supplier_last_name}",{pid})''')
        mycursor.execute("commit")
        mycursor.close()
        return True
    except:
        return False

def removing_item(pid,uid):
    mycursor = database.cursor()
    mycursor.execute (f'''DELETE FROM Supplier WHERE user_id={uid} AND product_id = {pid}''')
    mycursor.execute("commit")
    mycursor.close()
    return True

def adding_existing_item(pid,uid):
    try:
        mycursor = database.cursor()
        mycursor.execute (f'''SELECT distinct(S.supplier_first_name) as NAME FROM Supplier AS S  WHERE S.user_id = {uid}''')  
        rows = mycursor.fetchall()
        supplier_first_name = rows[0][0]
        print(supplier_first_name)
        mycursor.close()

        mycursor = database.cursor()
        mycursor.execute (f'''SELECT distinct(S.supplier_last_name) as NAME FROM Supplier AS S  WHERE S.user_id = {uid}''')  
        rows = mycursor.fetchall()
        supplier_last_name = rows[0][0]
        print(supplier_last_name)
        mycursor.close()

        mycursor = database.cursor()
        mycursor.execute (f'''INSERT INTO Supplier VALUES({uid},"{supplier_first_name}","{supplier_last_name}",{pid})''')
        mycursor.execute("commit")
        mycursor.close()
        return True
    except:
        return False



def display_all_products():
    mycursor = database.cursor()
    mycursor.execute('''select * from all_products''')
    rows = mycursor.fetchall()
    mycursor.close()
    return rows
    
