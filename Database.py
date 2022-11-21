import sqlite3
from tkinter import StringVar, messagebox
from MainMenu import Main1

def CreateDatabase():
    global conn, cursor 
    conn = sqlite3.connect("inventorydata.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty INTEGER, product_price REAL)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")#change password here
        conn.commit()

def Login(USERNAME, PASSWORD):
    global admin_id
    CreateDatabase()
    if USERNAME.get == "" or PASSWORD.get() == "":
        result = messagebox.showwarning('Ginsilog', 'Please Fill the Fields!')
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

