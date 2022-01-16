import tkinter as tk
from tkinter import messagebox
import connector as data
from tkinter import ttk
#
bgc = '#3a77ae'
fgc = '#ffffff'
#
def add_items(uid):
    def add_s(pid,uid,pname,ptype):
        suc = False
        suc = data.adding_item(pid,uid,pname,ptype)
        if suc:
           messagebox.showinfo('Added!','New item Successfully Added!')
           new_win.destroy()
        else:
            messagebox.showinfo('Error','An Error Occured! product id not valid!')
    
    new_win = tk.Tk()
    new_win.geometry('300x350')
    new_win.title('Add item')
    new_win.configure(bg = bgc)
    
    product_id = tk.Label(new_win,text = 'Product ID',bg = bgc,fg = fgc)
    product_id.place(x = 15, y = 20)
    product_id_entry = tk.Entry(new_win)
    product_id_entry.place(x = 100,y = 20,width = 100)

    product_name = tk.Label(new_win,text = 'Product Name',bg = bgc,fg = fgc)
    product_name.place(x = 15, y = 60)
    product_name_entry = tk.Entry(new_win)
    product_name_entry.place(x = 100,y = 60,width = 100)
    
    product_type = tk.Label(new_win,text = 'Product Type',bg = bgc,fg = fgc)
    product_type.place(x = 15, y = 100)
    product_type_entry = tk.Entry(new_win)
    product_type_entry.place(x = 100,y = 100,width = 100)
    
    add_values= tk.Button(new_win,text = 'Add',bg = bgc,fg = fgc,command =
     lambda: add_s(int(product_id_entry.get()),uid,str(product_name_entry.get()),str(product_type_entry.get())  ))
    add_values.place(x =120,y = 260)
    new_win.mainloop()

def remove_items(uid):
    def remove(pid,uid):
        suc = False
        suc = data.removing_item(pid,uid)
        if suc:
           messagebox.showinfo('Removed!','item Successfully removed!')
           next_win.destroy()
        else:
            messagebox.showinfo('Error','An Error Occured! operation failed!')

    next_win = tk.Tk()
    next_win.geometry('300x350')
    next_win.title('remove item')
    next_win.configure(bg = bgc)
    
    product_id = tk.Label(next_win,text = 'Product ID',bg = bgc,fg = fgc)
    product_id.place(x = 15, y = 20)
    product_id_entry = tk.Entry(next_win)
    product_id_entry.place(x = 100,y = 20,width = 100)

    remove_values=tk.Button(next_win,text = "remove",bg = bgc,fg = fgc,command =
     lambda: remove(int(product_id_entry.get()),uid ))
    remove_values.place(x =120,y = 260)

    next_win.mainloop()

def add_existing_items(uid): 
    def add_exist(pid,uid):
        suc = False
        suc = data.adding_existing_item(pid,uid)
        if suc:
           messagebox.showinfo('Added!','New item Successfully Added from product table!')
           new.destroy()
        else:
            messagebox.showinfo('ERROR!','The item you are trying to add is aldready supplied by you!!!!')
    
    new = tk.Tk()
    new.geometry('300x350')
    new.title('Add item')
    new.configure(bg = bgc)
    
    existing_product_id = tk.Label(new,text = 'Product ID',bg = bgc,fg = fgc)
    existing_product_id.place(x = 15, y = 20)
    product_id_entry = tk.Entry(new)
    product_id_entry.place(x = 100,y = 20,width = 100)

    add_existing_values= tk.Button(new,text = 'Add',bg = bgc,fg = fgc,command =
     lambda: add_exist(int(product_id_entry.get()),uid  ))
    add_existing_values.place(x =120,y = 260)
    new.mainloop()

def all_products():
    
    var=data.display_all_products()
    window1 = tk.Tk() 
    window1.resizable(width = 1, height = 1)  
    treev = ttk.Treeview(window1, selectmode ='browse') 
    treev.pack(side ='right') 
    verscrlbar = ttk.Scrollbar(window1,  
                            orient ="vertical",  
                            command = treev.yview) 
    verscrlbar.pack(side ='right', fill ='x') 
    treev.configure(xscrollcommand = verscrlbar.set) 
    treev["columns"] = ("1", "2", "3") 
    treev['show'] = 'headings'
    treev.column("1", width = 90, anchor ='c') 
    treev.column("2", width = 90, anchor ='se') 
    treev.column("3", width = 90, anchor ='se') 
    treev.heading("1", text ="Product Id") 
    treev.heading("2", text ="Product Name") 
    treev.heading("3", text ="Product Type") 
    for tuple in var:
        treev.insert("", 'end', 
                    values =tuple)


