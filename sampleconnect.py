import mysql.connector as sql
from tabulate import tabulate

db = sql.connect(host = 'localhost',
                 user = 'kishore',
                 password = 'Gr8stofa11time',
                 database = 'Inventory_Management_Final'
                 )

mycursor = db.cursor()

def supplier_info(pid):
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT user_id,CONCAT(supplier_first_name,' ', supplier_last_name) from Supplier WHERE product_id = {pid}''')
    rows = mycursor.fetchall()
    mycursor.close()
    return rows

def products_supply(sid):
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT Supplier.product_id, product_name, product_type FROM Product INNER JOIN Supplier ON Product.product_id = Supplier.product_id WHERE user_id = {sid};''')
    rows = mycursor.fetchall()
    mycursor.close()
    return rows
    
def suppliers_products():
    mycursor = db.cursor()
    mycursor.execute(f'''SELECT * FROM Products_Suppliers;''')
    rows = mycursor.fetchall()
    mycursor.close()
    return rows