from tkinter import *
from db import *
from SMTP import *
from OwnerUI import *
global otp
otp = ""

def login():
    username = e1.get()
    password = e2.get()
    status, user_id_main= check_login(username, password)
    if status:
        print("correct")
        myLabel1.pack_forget()
        e1.pack_forget()
        e2.pack_forget()
        button2.forget()
        myLabel2.pack_forget()
        myLabel3.pack_forget()
        Button1.pack_forget()
        status=check_user_type(user_id_main)
        if status==2:
            main(user_id_main)
        else:
            main_jaya(user_id_main)
    else:
        print("not correct")


def verrification():
    username = ent1.get()
    global otp
    if check_email(username):
        label1.forget()
        ent1.forget()
        Button_1.forget()
        otp = generateOTP()
        send_email(otp,"kishorekumar0813@gmail.com",username)
        labelotp.pack()
        entotp.pack()
        otpsubmit.pack()
        
def checkotp():
    global otp
    OTP = entotp.get()
    if otp == OTP:
        labelotp.forget()
        entotp.forget()
        otpsubmit.forget()
        new.pack()
        entnewpassword.pack()
        confirm.pack()
        entconfirnpassword.pack()
        change.pack()
    else:
        login_screen()




def Forgot():
    myLabel1.pack_forget()
    e1.pack_forget()
    e2.pack_forget()
    button2.forget()
    myLabel2.pack_forget()
    myLabel3.pack_forget()
    Button1.pack_forget()
    label1.pack()
    ent1.pack()
    Button_1.pack()
    
def checkforconfirmation():
    password_new = entnewpassword.get()
    confirm_password = entconfirnpassword.get()
    if password_new == confirm_password:
        wrong.forget()
        changelogin_password(ent1.get(),password_new)
        new.forget()
        entnewpassword.forget()
        confirm.forget()
        entconfirnpassword.forget()
        change.forget()
        login_screen()
    else:
        wrong.pack()


def login_screen():
    myLabel1.pack()
    myLabel2.pack()
    e1.pack()
    myLabel3.pack()
    myLabel3.pack()
    myLabel3.pack()
    e2.pack()
    Button1.pack()
    button2.pack()





import sampleconnect as jdb
def suppliers_products():
    tab = jdb.suppliers_products()
    new_win = tk.Tk()
    new_win.title(f'Products and Supppliers') 
    tree = ttk.Treeview(new_win,columns = (1,2,3,4), show = "headings")
    tree.pack()
    
    tree.column(1,width = 85,minwidth=75)
    tree.heading(1,text = 'Product ID')

    tree.column(2,width = 85,minwidth=75)
    tree.heading(2,text = 'Product Name',anchor = 'center')

    tree.column(3,width = 85,minwidth=75)
    tree.heading(3,text = 'Supplier ID',anchor = 'center')
    
    tree.column(4,width = 120,minwidth=75)
    tree.heading(4,text = 'Supplier Name',anchor = 'center')

    for i in tab:
        tree.insert('','end',values = i)
    new_win.mainloop()

def supplier(product_id):
     tab = jdb.supplier_info(product_id)   
     new_win = tk.Tk()
     new_win.title(f'Suppliers') 
     tree = ttk.Treeview(new_win,columns = (1,2), show = "headings")
     tree.pack()
     
     tree.column(1,width = 85,minwidth=75)
     tree.heading(1,text = 'Supplier ID')
       
     tree.column(2,width = 85,minwidth=75)
     tree.heading(2,text = 'Supplier Name',anchor = 'center')
     
     for i in tab:
         tree.insert('','end',values = i)
     new_win.mainloop()

def products_supply(supplier_id):
    tab = jdb.products_supply(supplier_id)
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
    supplier_info = tk.Button(root,text = 'Show Products Suppliers',command = lambda : suppliers_products(), bg = '#3a77ae',fg = '#ffffff')
    supplier_info.place(x = 15, y =40)


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import UI_To_DB as db

h = 2160
w = 1110
bgc = '#3a77ae'
fgc = '#ffffff'
owner_name = ''


def no_of_stores(user_id,label):
   tab = db.store_count(user_id)
   count = tab[0]
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
    
    
    
def main(uid):    
   def foget_kk():
       store_count.place_forget()
       label.place_forget()
       change_pwd.place_forget()
       get_info.place_forget()
       store_id_entry.place_forget()
       all_store.place_forget()
       new_store.place_forget()
       delete_store.place_forget()
       delete_store_entry.place_forget()
       check_inventory.place_forget()
       check_inventory_entry.place_forget()
       main_sanjay(check_inventory_entry.get())

   owner_info(uid)
   tab = db.store_count(uid)
   count = tab[0]
   label = tk.Label(root,text = tab,bg = bgc,fg = fgc,height = 1, width = 15)
   store_count = tk.Button(root,text = 'Stores Avilable',command = lambda : no_of_stores(uid,label),bg = bgc,fg = fgc)
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
                               bg = bgc,fg = fgc,command= lambda:foget_kk())
   check_inventory.place(x = 15,y = 280)

   check_inventory_entry = tk.Entry(root,width = 5)
   check_inventory_entry.place(x = 150, y = 280)
   root.mainloop()

import inventory1 as d

h = 2160
w = 1110


def inventory(sid):
    tab = d.store(sid)
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
    tab = d.reorder(sid)
    label = tk.Label(root,text = tab,bg = '#3a77ae')
    label.pack()
    messagebox.showinfo('Added!','New items Successfully Added!')


def update_quantity(sid):
    def update(pid,quan):
        d.update(sid,pid,quan)
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

def create_product(sid):
    def create(pid,quan,re_lvl):
        d.create(sid,pid,quan,re_lvl)
        messagebox.showinfo('Added!','Successfully Added!!')
        new_win.destroy()
    new_win = tk.Tk()
    new_win.geometry('450x200')
    new_win.configure(bg = '#3a77ae')
    chp = tk.Label(new_win,text = 'ADD PRODUCT',font = ('Times New Roman',15),borderwidth = 3,
                   relief = 'ridge',bg = '#3a77ae')
    chp.pack(fill = 'x')
    
    pid = tk.Label(new_win,text = 'Product Id',bg = '#3a77ae',fg ='#ffffff')
    pid.place(x = 15, y = 30)
    
    pid_entry = tk.Entry(new_win,width = 15)
    pid_entry.place(x = 150,y = 30)
    
    quan = tk.Label(new_win,text = 'Quantity',bg = '#3a77ae',fg = '#ffffff')
    quan.place(x = 15, y = 60)
    
    quan_entry = tk.Entry(new_win,width = 15)
    quan_entry.place(x = 150,y = 60)


    re_lvl = tk.Label(new_win,text = 'Reorder level',bg = '#3a77ae',fg = '#ffffff')
    re_lvl.place(x = 15, y = 90)
    
    re_lvl_entry = tk.Entry(new_win,width = 15)
    re_lvl_entry.place(x = 150,y = 90)


    ch = tk.Button(new_win,text = 'Confirm',bg = '#3a77ae',fg =  '#ffffff',command = lambda:create(int(pid_entry.get()),int(quan_entry.get()),int(re_lvl_entry.get())))
    ch.place(x = 180, y =120)

def main_sanjay(input):
    def forgot_sanjay():
        button_display.place_forget()
        button_reorder.place_forget()
        button_update.place_forget()
        button_search.place_forget()
        button_product.place_forget()
        main_jeeva()


    button_display = tk.Button(root,text = "DISPLAY",command = lambda: inventory(input),bg = '#3a77ae')
    button_display.place(x=20,y=50)
    button_product = tk.Button(root,text = "ADD PRODUCT",command = lambda: create_product(input),bg = '#3a77ae')
    button_product.place(x=20,y=170)

    button_reorder = tk.Button(root,text = "REODER",command = lambda: inventory_reorder(input),bg = '#3a77ae')
    button_reorder.place(x=20,y=90)


    button_update = tk.Button(root,text = "UPDATE",command = lambda: update_quantity(input),bg = '#3a77ae')
    button_update.place(x=20,y=130)

    button_search = tk.Button(root,text = "SEARCH SUPPLIER",command = lambda:forgot_sanjay() ,bg = '#3a77ae')
    button_search.place(x=20,y=210)









import connector as data
import additems as add


def supplier_greet( user_id ) :
    var = data.supplier_info ( user_id )
    supplier_first_name = var[0][0]
    welcome = tk.Label( root,text = f'WELCOME {supplier_first_name}',bg = '#3a77ae',font = ("Times New Roman",34))  
    welcome.pack( fill = 'x' )

def products_supplied( user_id ) :
    window = tk.Tk() 
    window.resizable(width = 1, height = 1)  
    treev = ttk.Treeview(window, selectmode ='browse') 
    treev.pack(side ='right') 
    
    # Constructing vertical scrollbar 
    # with treeview 
    verscrlbar = ttk.Scrollbar(window,  
                            orient ="vertical",  
                            command = treev.yview) 
    
    # Calling pack method w.r.to verical  
    # scrollbar 
    verscrlbar.pack(side ='right', fill ='x') 
    
    # Configuring treeview 
    treev.configure(xscrollcommand = verscrlbar.set) 
    
    # Defining number of columns 
    treev["columns"] = ("1", "2", "3") 
    
    # Defining heading 
    treev['show'] = 'headings'
    
    # Assigning the width and anchor to  the 
    # respective columns 
    treev.column("1", width = 90, anchor ='c') 
    treev.column("2", width = 90, anchor ='se') 
    treev.column("3", width = 90, anchor ='se') 
    
    # Assigning the heading names to the  
    # respective columns 
    treev.heading("1", text ="Product Id") 
    treev.heading("2", text ="Product Name") 
    treev.heading("3", text ="Product Type") 
    var = data.products_supplied( user_id )
    for tuple in var:
        treev.insert("", 'end', 
                    values =tuple)
    

def main_jaya(user_id):
    supplier_greet( user_id )
    button = tk.Button( root , text = "Products Supplied" , command = lambda :products_supplied( user_id ),bg = '#3a77ae' ,font = ("Times New Roman",12) )
    button.place(x= 100 , y = 100)

    button = tk.Button( root , text = "Add Product" , command = lambda : add.add_items( user_id ),bg = '#3a77ae' ,font = ("Times New Roman",12))
    button.place(x = 100 , y = 150)

    button = tk.Button( root , text = "Remove Product" , command = lambda : add.remove_items( user_id ),bg = '#3a77ae' ,font = ("Times New Roman",12))
    button.place(x = 100 , y = 200)

    button = tk.Button( root , text = "All Products" , command = lambda :add.all_products( ),bg = '#3a77ae' ,font = ("Times New Roman",12) )
    button.place(x= 100 , y = 250)

    button = tk.Button( root , text = "Add existing Product" , command = lambda : add.add_existing_items( user_id ),bg = '#3a77ae' ,font = ("Times New Roman",12))
    button.place(x = 100 , y = 300)

    
    root.mainloop()






root= Tk()
root.configure(bg="#3a77ae")
root.geometry("2160x1110")

myLabel1 = Label(root,text="Login", bg="#3a77ae" ,fg="white",anchor=S, height=10,font="Helvetica 14 bold")
myLabel2 = Label(root, text= "Email" ,bg="#3a77ae" ,fg="white",anchor=W, height=2, font="Helvetica 12 bold",width=28)
e1 = Entry(root, width = 30)
myLabel3 = Label(root, text= "Password",bg="#3a77ae" ,fg="white",anchor=W, font="Helvetica 12 bold", width=28)
e2 = Entry(root,width = 30,show="*")
Button1 = Button(root, text="Log in",padx=10 ,pady = 5,bg="#3a77ae" ,fg="white",command = login)
button2 = Button(root, text="Forgot password", padx=5, bg="#3a77ae" ,fg="white",command = Forgot)


label1 = Label(root, text="Enter your emailid used for registration:",fg="white", bg="#3a77ae")
ent1 = Entry(root, width=30)
Button_1 = Button(root, text="Reset password",padx=10 ,pady = 5,bg="#3a77ae" ,fg="white",command = verrification)

labelotp = Label(root, text="otp:")
entotp = Entry(root,width = 30)
otpsubmit = Button(root, text="Reset",padx=10 ,pady = 5,bg="#3a77ae" ,fg="white",command = checkotp)


new = Label(root, text="New password")
entnewpassword = Entry(root,width = 30)
confirm = Label(root, text="Confirm new password")
entconfirnpassword = Entry(root,width = 30)
change = Button(root, text="Reset",padx=10 ,pady = 5,bg="#3a77ae" ,fg="white",command = checkforconfirmation)
wrong = Label(root, text="New password does't match with the confirm new password")
login_screen()
root.mainloop() 
