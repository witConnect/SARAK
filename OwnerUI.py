import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import UI_To_DB as db

uid = 1
h = 2160
w = 1110
bgc = '#3a77ae'
fgc = '#ffffff'
owner_name = ''


def no_of_stores(user_id):
   tab = db.store_count(user_id)
   count = tab[0]
   label = tk.Label(root,text = tab,bg = bgc,fg = fgc,height = 1, width = 15)
   label.place(x = 110,y = 81)
   
def owner_info(user_id):
    global owner_name
    tab = db.owner_name(user_id)
    owner_name = tab[0][0]
    welcome = tk.Label(root,text = f'Welcome {owner_name}',font = ('Times New Roman',22),borderwidth=3,
                       relief='ridge',bg = bgc)
    welcome.pack(fill = 'x')
    
def store_info(store_id,uid):
    tab = db.store_info(store_id,uid)
    new_win = tk.Tk()
    new_win.configure(bg = bgc)
    new_win.geometry()
    tree = ttk.Treeview(new_win,columns = (1,2,3,4), show = "headings",height = 1)
  
    tree.pack()
    tree.column(1,width = 85,minwidth=75)
    tree.heading(1,text = 'Store ID')

    tree.column(2,width = 85,minwidth=75)
    tree.heading(2,text = 'User ID',anchor = 'center')

    tree.column(3,width = 120,minwidth=110)
    tree.heading(3,text = 'Store Name',anchor = 'center')
    
    tree.column(4,width = 300,minwidth = 290)
    tree.heading(4,text = 'Address',anchor = 'center')
    for i in tab:
        tree.insert('','end',values = i)
    new_win.mainloop()
        
def all_store_info(uid):
    tab = db.all_store_info(uid)
    new_win = tk.Tk()
    new_win.title(f'All Stores Owned By {owner_name}') 
    tree = ttk.Treeview(new_win,columns = (1,2,3,4), show = "headings")
    tree.pack()
    
    tree.column(1,width = 85,minwidth=75)
    tree.heading(1,text = 'Store ID')

    tree.column(2,width = 85,minwidth=75)
    tree.heading(2,text = 'User ID',anchor = 'center')

    tree.column(3,width = 120,minwidth=110)
    tree.heading(3,text = 'Store Name',anchor = 'center')
    
    tree.column(4,width = 300,minwidth = 290)
    tree.heading(4,text = 'Address',anchor = 'center')
    for i in tab:
        tree.insert('','end',values = i)
    new_win.mainloop()
    
def add_store(uid):
    def add_s(sid,uid,sname,street,city,state,pin):
        suc = False
        suc = db.add_store(sid,uid,sname,street,city,state,pin)
        if suc:
           messagebox.showinfo('Added!','New Store Successfully Added!')
           new_win.destroy()
        else:
           messagebox.showinfo('Error','An Error Occured! Check Your Values!')
    new_win = tk.Tk()
    new_win.geometry('300x350')
    new_win.title('Add Store')
    new_win.configure(bg = bgc)
    store_id = tk.Label(new_win,text = 'Store ID',bg = bgc,fg = fgc)
    store_id.place(x = 15, y = 20)
    store_id_entry = tk.Entry(new_win)
    store_id_entry.place(x = 100,y = 20,width = 100)
    
    store_name = tk.Label(new_win,text = 'Store Name',bg = bgc,fg = fgc)
    store_name.place(x = 15, y = 60)
    store_name_entry = tk.Entry(new_win)
    store_name_entry.place(x = 100,y = 60,width = 100)
    
    store_street = tk.Label(new_win,text = 'Street',bg = bgc,fg = fgc)
    store_street.place(x = 15, y = 100)
    store_street_entry = tk.Entry(new_win)
    store_street_entry.place(x = 100,y = 100,width = 100)
    
    store_city = tk.Label(new_win,text = 'City',bg = bgc,fg = fgc)
    store_city.place(x = 15, y = 140)
    store_city_entry = tk.Entry(new_win)
    store_city_entry.place(x = 100,y = 140,width = 100)
    
    store_pin = tk.Label(new_win,text = 'PIN',bg = bgc,fg = fgc)
    store_pin.place(x = 15, y = 180)
    store_pin_entry = tk.Entry(new_win)
    store_pin_entry.place(x = 100,y = 180,width = 100)
    
    store_state = tk.Label(new_win,text = 'State',bg = bgc,fg = fgc)
    store_state.place(x = 15, y = 220)
    store_state_entry = tk.Entry(new_win)
    store_state_entry.place(x = 100,y = 220,width = 100)
    
    add_button = tk.Button(new_win,text = 'Add',bg = bgc,fg = fgc,command = 
                           lambda: add_s(int(store_id_entry.get()),uid,str(store_name_entry.get()),str(store_street_entry.get()),str(store_city_entry.get()),str(store_state_entry.get()),int(store_pin_entry.get())))
    add_button.place(x = 120, y = 260)

def remove_store(sid):
   suc = db.remove_store(sid)
   if suc:
      messagebox.showinfo('Removed!',f'Store no:{sid} Removed Successfully!')
    
    
def change_password():
    def change(newp,confp):
        suc = db.change_password(uid,newp,confp)
        if suc:
           messagebox.showinfo('Sucess!','Password Reseted') 
           new_win.destroy()
        else:
           messagebox.showinfo('Failed','Falied to reset password')
    new_win = tk.Tk()
    new_win.geometry('450x200')
    new_win.configure(bg = bgc)
    chp = tk.Label(new_win,text = 'Changing Password',font = ('Times New Roman',15),borderwidth = 3,
                   relief = 'ridge',bg = bgc)
    chp.pack(fill = 'x')
    new_password = tk.Label(new_win,text = 'New Password',bg = bgc,fg = fgc)
    new_password.place(x = 15, y = 40)
    
    new_password_entry = tk.Entry(new_win,width = 15,show = '*')
    new_password_entry.place(x = 150,y = 40)
    
    confirm_password = tk.Label(new_win,text = 'Confirm Password',bg = bgc,fg = fgc)
    confirm_password.place(x = 15, y = 80)
    
    confirm_password_entry = tk.Entry(new_win,width = 15,show = '*')
    confirm_password_entry.place(x = 150,y = 80)
    
    ch = tk.Button(new_win,text = 'Change',bg = bgc,fg = fgc,command = lambda:change(new_password_entry.get(),confirm_password_entry.get()))
    ch.place(x = 180, y =120)
    
    
    
def main():    
   owner_info(uid)
   store_count = tk.Button(root,text = 'Stores Avilable',command = lambda : no_of_stores(uid),bg = bgc,fg = fgc)
   store_count.place(x = 15,y = 80)

   change_pwd = tk.Button(root,text = 'Change Password',bg = bgc,fg = fgc,height = 1, width = 15,command = lambda:change_password())
   change_pwd.place(x = 1000,y = 15)

   get_info = tk.Button(root,text = 'Store Info',command = lambda : store_info(store_id_entry.get(),uid),
                        bg = bgc,fg = fgc)
   get_info.place(x = 15, y =120)

   store_id_entry = tk.Entry(root,width = 5)
   store_id_entry.place(x = 150,y = 120)

   all_store = tk.Button(root,text = 'Show All Stores',command = lambda: all_store_info(uid)
                         ,bg = bgc,fg = fgc)
   all_store.place(x = 15,y = 160)

   new_store = tk.Button(root,text = 'Add Store',command = lambda :add_store(uid),
                         bg = bgc,fg = fgc)
   new_store.place(x = 15,y = 200)

   delete_store = tk.Button(root,text = 'Remove Store',command = lambda:remove_store(delete_store_entry.get()),
                            bg = bgc,fg = fgc)
   delete_store.place(x = 15, y = 240)

   delete_store_entry = tk.Entry(root,width = 5)
   delete_store_entry.place(x = 150, y = 240)

   check_inventory = tk.Button(root,text = 'Check Inventory',
                               bg = bgc,fg = fgc)
   check_inventory.place(x = 15,y = 280)

   check_inventory_entry = tk.Entry(root,width = 5)
   check_inventory_entry.place(x = 150, y = 280)
   root.mainloop()

   

