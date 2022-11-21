from email import message
from tkinter import *
import sqlite3
import sys
import os
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from turtle import width
from PIL import Image, ImageTk
from datetime import date

window = Tk()
window.title("Ginsilog's Product Management")
window.config(background="#000000")
window.geometry('1024x768')

#VARIABLES

USERNAME = StringVar()
PASSWORD = StringVar()


#Database Methods
def Database():
    global conn, cursor 
    conn = sqlite3.connect("inventorydata.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `report` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT, product_add TEXT, product_del TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")#change password here
        conn.commit()
        
def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        result = messagebox.askquestion('Ginsilog', 'Did you fill the login credentials?', icon="warning")
        if result == 'yes':
            USERNAME.set("")
            PASSWORD.set("")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            #login success
            #insert next window function
            messagebox.showinfo('Ginsilog', 'Login Success!')
            window.destroy()
            Main1()
        else:
            messagebox.showwarning('Ginsilog', 'Invalid Credentials')
            USERNAME.set("")
            PASSWORD.set("")
        cursor.close()
        conn.close()

#ADD
def Addnew():
    Database()
    messagebox.showinfo('Ginsilog', 'Product Added Successfully!')
    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    cursor.execute("INSERT INTO `report` (product_name, product_qty, product_price, product_add, product_del) VALUES(?, ?, ?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get()), str(PRODUCT_ADD), str(PRODUCT_STAT)))
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    cursor.close()
    conn.close()

#Search
def Search():
    window = Tk()
    window.geometry("800x200")
    window.title("View Product")

    def back():
            window.destroy()

    def Search1():
        x = search_text.get()
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_id` = ?", (x,))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('','end', values = (data))
        cursor.close()
        conn.close()

    frm = Frame(window)
    frm.pack(side=tk.LEFT,padx=20, pady=20)
    scrollbarx = Scrollbar(frm, orient=HORIZONTAL)
    tree = ttk.Treeview(frm, columns=("Product ID", "Product Name", "Product Qty", "Product Price"), height=5, xscrollcommand=scrollbarx.set)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Product ID', text="Product ID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    b1= Button(window, text="Back", width=12, font="Arial, 16", command=back)
    b1.pack(pady = 20)
    Search1()

#Display All
def DisplayAllWindow():
    global tree
    window = Tk()
    window.geometry("800x600")
    window.title("All Products")

    def Mainmenu():
        result = messagebox.askquestion('Ginsilog', 'Are you done?', icon='warning')
        if result == 'yes':
            window.destroy()
            Main1()

    frm = Frame(window)
    frm.pack(side=tk.LEFT,padx=20)
    scrollbarx = Scrollbar(frm, orient=HORIZONTAL)
    scrollbary = Scrollbar(frm, orient=VERTICAL)
    tree = ttk.Treeview(frm, columns=("Product ID", "Product Name", "Product Qty", "Product Price"), height=60, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Product ID', text="Product ID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    b1= Button(window, text="Main Menu", width=12, font="Arial, 16", command=Mainmenu)
    b1.pack()
    DisplayData()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#REPORTS WINDOW
def ReportWindow():
    global tree1
    window = Tk()
    window.geometry("1000x600")
    window.title("Report")

    def Mainmenu():
        result = messagebox.askquestion('Ginsilog', 'Are you done?', icon='warning')
        if result == 'yes':
            window.destroy()

    frm = Frame(window)
    frm.pack(side=tk.LEFT,padx=20)
    scrollbarx = Scrollbar(frm, orient=HORIZONTAL)
    scrollbary = Scrollbar(frm, orient=VERTICAL)
    tree1 = ttk.Treeview(frm, columns=("Product ID", "Product Name", "Product Qty", "Product Price", "Date Added", "Product Status"), height=60, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree1.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree1.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree1.heading('Product ID', text="Product ID",anchor=W)
    tree1.heading('Product Name', text="Product Name",anchor=W)
    tree1.heading('Product Qty', text="Product Qty",anchor=W)
    tree1.heading('Product Price', text="Product Price",anchor=W)
    tree1.heading('Date Added', text="Date Added",anchor=W)
    tree1.heading('Product Status', text="Product Status",anchor=W)
    tree1.column('#0', stretch=NO, minwidth=0, width=0)
    tree1.column('#1', stretch=NO, minwidth=0, width=100)
    tree1.column('#2', stretch=NO, minwidth=0, width=200)
    tree1.column('#3', stretch=NO, minwidth=0, width=120)
    tree1.column('#4', stretch=NO, minwidth=0, width=120)
    tree1.column('#5', stretch=NO, minwidth=0, width=100)
    tree1.column('#6', stretch=NO, minwidth=0, width=120)
    tree1.pack()
    b1= Button(window, text="Main Menu", width=12, font="Arial, 16", command=Mainmenu)
    b1.pack()
    DisplayReport()

def DisplayReport():
    Database()
    cursor.execute("SELECT * FROM `report`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree1.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#Delete/Sell/Update Report
def Delete():
    x = search_text.get()
    result = messagebox.askquestion('Ginsilog', 'Are you sure you want to sell the item?', icon = "warning")
    if result == 'yes':
        Database()
        cursor.execute("DELETE FROM `product` WHERE `product_id` = ?", (x,))
        conn.commit()
        cursor.close()
        conn.close()
        UpdateReport()
    else:
        print(x)

def UpdateReport():
    x = search_text.get()
    y = "Sold"
    Database()
    cursor.execute("UPDATE report SET product_del = ? WHERE product_id = ?",(str(y),x,))
    conn.commit()
    cursor.close()
    conn.close()
    print(y)



#Restock
def Restock():
    window=Tk()
    window.geometry("1024x768")
    window.title('Restock Product')
    window.config(background="#000000")
    global PRODUCT_NAME,PRODUCT_PRICE,PRODUCT_QTY,PRODUCT_ADD,PRODUCT_STAT
    #Method
    def Mainmenu():
        result = messagebox.askquestion('Ginsilog', 'Are you done?', icon='warning')
        if result == 'yes':
            window.destroy()
            Main1()
            
    PRODUCT_NAME = StringVar()
    PRODUCT_QTY = IntVar()
    PRODUCT_PRICE = IntVar()
    PRODUCT_ADD = date.today()
    PRODUCT_STAT = "In Stock"

    
    prodlbl=Label(window, text="Product Name", padx = 1, fg="#FFFFFF", bg="#000000", font="Arial, 20")
    prodlbl.place(x=425, y=90)
    quantlbl=Label(window, text="Quantity", padx = 1, fg="#FFFFFF", bg="#000000", font="Arial, 20")
    quantlbl.place(x=460, y=190)
    costlbl=Label(window, text="Product Cost", padx = 1, fg="#FFFFFF", bg="#000000", font="Arial, 20")
    costlbl.place(x=430, y=290)

    PRODUCT_NAME = Entry(window, textvariable=PRODUCT_NAME, font="Arial, 20", width=15, highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", insertbackground="white" )
    PRODUCT_NAME.place(x=400, y=140)

    
    PRODUCT_QTY = Entry(window, textvariable=PRODUCT_QTY, font="Arial, 20", width=15, highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", insertbackground="white" )
    PRODUCT_QTY.place(x=400, y=240)

    
    PRODUCT_PRICE = Entry(window, textvariable=PRODUCT_PRICE, font="Arial, 20", width=15, highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", insertbackground="white" )
    PRODUCT_PRICE.place(x=400, y=340)

    btnadd=Button(window, text="ADD", width=12, font="Arial, 16", highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", command=Addnew)
    btnadd.place(x=50, y=600)
    btncnl=Button(window, text="CANCEL", width=12, font="Arial, 16", highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", command=Mainmenu)
    btncnl.place(x=250, y=600)

    window.mainloop()

#SELL
def SellHere():
    window = Tk()
    window.title("Ginsilog's Product Management")
    window.geometry("1024x768")
    window.config(background= "#000000")
    global search_text
    quantity_val = int(0)
    def menu():
        result = messagebox.askquestion('Ginsilog', 'Are you sure?', icon = "warning")
        if result == 'yes':
            window.destroy()
            Main1()

    def quantityget():
        Database()
        if search_text.get() != 0:
            cursor.execute("SELECT 'product_qty' FROM 'product' WHERE 'product_id' = ?", (search_text.get(),))
            fetch = cursor.fetchall()
            for data in fetch:
                print(data)
            cursor.close()
            conn.close()
            
        

    frame= Frame(window, relief= 'sunken', bg= "black", width=700, height=500)
    frame.pack(fill= BOTH, expand= True, padx= 10, pady=10)

    Cancel = Button(frame, text='Cancel',width=15,height=1,font='Arial 20',highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", command=menu)
    Cancel.grid(row=0,column=0, pady=(10, 10))

    Random = Label(frame,text='SEARCH RESULT WINDOW',width=25,height=15,font='Arial 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised')
    Random.grid(row=1,column=1, padx=10,pady=(10, 10),rowspan=6)

    search_text = IntVar()
    search1 = Entry(frame,textvariable=search_text, fg='#FFFFFF', bg='#000000', font="Arial, 20",width=10,insertbackground="white")
    search1.grid(row=1,column=0, pady=(10, 10))

    search = Button(frame, text='SEARCH',width=10,font='Arial, 20',highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", command=lambda:[Search(),quantityget()])
    search.grid(row=2,column=0, pady=(10, 10))

    price = Label(frame, text='Quantity',width=10,height=1,font='Arial, 20',bg='#000000',fg='#ffffff')
    price.grid(row=3,column=0, pady=(10, 10))


    quantity1 = Label(frame, text=quantity_val, fg='#FFFFFF', bg='#000000', font="Arial, 20",width=10)
    quantity1.grid(row=4,column=0, pady=(10, 10))


    price = Label(frame, text='Price Sold',width=10,height=1,font='Arial 20 bold',bg='#000000',fg='#ffffff')
    price.grid(row=5,column=0, pady=(10, 10))

    price_val = DoubleVar()
    price1 = Entry(frame, textvariable=price_val, fg='#FFFFFF', bg='#000000', font="Arial, 20",width=10)
    price1.grid(row=6,column=0, pady=(10, 10))



    btn = Button(frame, text='Delete BTN', fg='#FFFFFF', bg='#000000', font="Arial, 20",width=10, command=Delete)
    btn.grid(row=7,column=0, pady=(10, 10),columnspan=2)

    window.mainloop()


#MAIN MENU
def Main1():
    windows = Tk()
    windows.title('Main Menu')
    windows.geometry('1024x768')
    windows.config(background="#000000")

    frame= Frame(windows, relief= 'sunken', bg= "black")
    frame.pack(fill= BOTH, expand= True, padx= 150, pady=20)

    def RediRestock():
        windows.destroy()
        Restock()

    def RediView():
        windows.destroy()
        DisplayAllWindow()

    def RediSell():
        windows.destroy()
        SellHere()

    def RediReport():
        windows.destroy()
        DisplayReport()

    heading = Label(frame, text='GINSILOG\'S PRODUCT MANAGEMENT SYSTEM',fg="#FFFFFF",bg="#000000",font=("Verdana",40),wraplength='924',borderwidth=1, relief="groove",width=20)
    heading.grid(row=0,padx=10,pady=10)



    Restock_button =Button(frame, text='RESTOCK',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= lambda :RediRestock())
    Restock_button.grid(row=2,column=0, pady=(40, 10))

    View_button =Button(frame, text='VIEW',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= lambda :RediView())
    View_button.grid(row=3,column=0, pady=(20, 10))

    Sell_button =Button(frame, text='SELL',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= lambda :RediSell())
    Sell_button.grid(row=4,column=0, pady=(20, 10))

    Report_button =Button(frame, text='REPORT',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= ReportWindow)
    Report_button.grid(row=5,column=0, pady=(20, 10))

    windows.mainloop()

def cancelation():
    window.destroy()
    Main1()


#MAIN--------------------------------------------------------------

canvas = Canvas(window, width=400, height=400, bg="black", highlightcolor="black")
canvas.place(x=310, y= 20)

logo = ImageTk.PhotoImage(Image.open("ginsiloglogo.png"))
canvas.create_image(200,200, anchor=CENTER, image=logo)

#Login
l1=Label(window,text="Username ", fg="#FFFFFF", bg="#000000", font="Arial, 20")
l1.place(x=310,y=450)

l2=Label(window,text="Password" , fg="#FFFFFF", bg="#000000", font="Arial, 20")
l2.place(x=310,y=510)


user1 = Entry(window, textvariable=USERNAME, font="Arial, 20", width=15, highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", insertbackground="white" )
user1.place(x=480, y=450)


pass1 = Entry(window,textvariable=PASSWORD, font="Arial, 20", width=15,show="*", highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", insertbackground="white")
pass1.place(x=480, y=510)

b1= Button(window, text="Login", width=12, font="Arial, 16", highlightcolor="white", highlightthickness=1, fg="#FFFFFF", bg="#000000", command = Login)
b1.place(x=425, y=570)
b1.bind('<Return>', Login)

window.mainloop()