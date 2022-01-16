import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sampleconnect as db

h = 2160
w = 1110

root = tk.Tk()
root.geometry(f'{w}x{h}')
root.title('Product-Supplier')
root.configure(bg = '#3a77ae')

def supplier(product_id):
    tab = db.supplier_info(product_id)    
    count = tab[0]
    label = tk.Label(root,text = tab,bg ='#3a77ae',fg = '#ffffff',height = 1, width = 15)
    label.place(x = 300,y = 80)

def products_supply(supplier_id):
    tab = db.products_supply(supplier_id)
    new_win = tk.Tk()
    new_win.title(f'Products Supplied') 
    tree = ttk.Treeview(new_win,columns = (1,2,3), show = "headings")
    tree.pack()
    
    tree.column(1,width = 85,minwidth=75)
    tree.heading(1,text = 'Product ID')

    tree.column(2,width = 85,minwidth=75)
    tree.heading(2,text = 'Product Name',anchor = 'center')

    tree.column(3,width = 120,minwidth=75)
    tree.heading(3,text = 'Product Type',anchor = 'center')

    for i in tab:
        tree.insert('','end',values = i)
    new_win.mainloop()

#-5 marks for the main function
def main_jeeva():
    supplier_info = tk.Button(root,text = 'Find Supplier',command = lambda : supplier(pid.get()), bg = '#3a77ae',fg = '#ffffff')
    supplier_info.place(x = 15, y =80)
    
    pid = tk.Entry(root,width = 5)
    pid.place(x = 150, y = 80)

    products = tk.Button(root,text = 'Find Products',command = lambda : products_supply(sid.get()), bg = '#3a77ae',fg = '#ffffff')
    products.place(x = 15, y =120)

    sid = tk.Entry(root,width = 5)
    sid.place(x = 150, y = 120)


