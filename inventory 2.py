import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import inventory1 as db

h = 2160
w = 1110


def inventory(sid):
    tab = db.store(sid)
    new_win = tk.Tk()
    new_win.configure(bg = '#3a77ae')
    new_win.geometry()
    tree = ttk.Treeview(new_win,columns = (1,2,3,4), show = "headings",height = 5)
  
    tree.pack()
    tree.column(1,width = 85,minwidth=75)
    tree.heading(1,text = 'Store ID')

    tree.column(2,width = 85,minwidth=75)
    tree.heading(2,text = 'Product ID',anchor = 'center')

    tree.column(3,width = 85,minwidth=75)
    tree.heading(3,text = 'Quantity',anchor = 'center')
    
    tree.column(4,width = 85,minwidth = 75)
    tree.heading(4,text = 'Reorder',anchor = 'center')
    for i in tab:
        tree.insert('','end',values = i)
    new_win.mainloop()
    

def inventory_reorder(sid):
    tab = db.reorder(sid)
    label = tk.Label(root,text = tab,bg = '#3a77ae')
    label.pack()
    messagebox.showinfo('Added!','New items Successfully Added!')


def update_quantity(sid):
    def update(pid,quan):
        db.update(sid,pid,quan)
        messagebox.showinfo('Updated!','Successfully Updated')
        new_win.destroy()
    new_win = tk.Tk()
    new_win.geometry('450x200')
    new_win.configure(bg = '#3a77ae')
    chp = tk.Label(new_win,text = 'Update Inventory',font = ('Times New Roman',15),borderwidth = 3,
                   relief = 'ridge',bg = '#3a77ae')
    chp.pack(fill = 'x')
    
    pid = tk.Label(new_win,text = 'Product Id',bg = '#3a77ae',fg ='#ffffff')
    pid.place(x = 15, y = 40)
    
    pid_entry = tk.Entry(new_win,width = 15)
    pid_entry.place(x = 150,y = 40)
    
    quan = tk.Label(new_win,text = 'Quantity',bg = '#3a77ae',fg = '#ffffff')
    quan.place(x = 15, y = 80)
    
    quan_entry = tk.Entry(new_win,width = 15)
    quan_entry.place(x = 150,y = 80)


    ch = tk.Button(new_win,text = 'Confirm',bg = '#3a77ae',fg =  '#ffffff',command = lambda:update(int(pid_entry.get()),int(quan_entry.get())))
    ch.place(x = 180, y =120)

def create(sid,pid,quan,re_lvl):
    mycursor = db.cursor()
    mycursor.execute(f'''CALL Inventory_Management_Final.add_item({sid},{pid},{quan},{re_lvl})''')
    mycursor.close()
    db.commit()

def main():

    button = tk.Button(root,text = "DISPLAY",command = lambda: inventory(1),bg = '#3a77ae')
    button.place(x=20,y=50)


    button = tk.Button(root,text = "REODER",command = lambda: inventory_reorder(1),bg = '#3a77ae')
    button.place(x=20,y=90)


    button = tk.Button(root,text = "UPDATE",command = lambda: update_quantity(1),bg = '#3a77ae')
    button.place(x=20,y=130)

    button = tk.Button(root,text = "SEARCH SUPPLIER",command = lambda: print('abc'),bg = '#3a77ae')
    button.place(x=20,y=170)

    root.mainloop()

if __name__  == '__main__':
    root = tk.Tk()
    root.geometry(f'{w}x{h}')
    root.title('INVENTORY')
    label = tk.Label(root,text = 'INVENTORY',bg = '#3a77ae',font = ('Times New Roman',30),borderwidth = 5,
                   relief = 'ridge')
    label.pack()
    root.configure(bg = '#3a77ae')
    main()