
import connector as data
import additems as add


def supplier_greet( user_id ) :
    var = data.supplier_info ( user_id )
    supplier_first_name = var[0][0]
    welcome = tk.Label( root,text = f'WELCOME {supplier_first_name}',bg = '#3a77ae',font = ("Times New Roman",34))  
    welcome.pack( fill = 'x' )

def products_supplied( user_id ) :
    root1 = tk.Tk()
    root1.geometry("600x400")
    root1.title('Supplier')
    root1.configure(bg = bgc) 
    var = data.products_supplied( user_id )
    label = tk.Label(root1,text = var,bg = '#3a77ae' )
    label.place( x = 150 , y = 30)
    root1.mainloop()s

def main(user_id):
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

