import tkinter as tk
from tkinter import ttk,messagebox,BOTH
from tkinter.font import BOLD
from turtle import width
from Sample import samplecontent
from delete_group import SellHere



def Main1():
    windows = tk.Tk()
    windows.title('Main Menu')
    windows.geometry('1024x768')
    windows.config(background="#000000")

    frame= tk.Frame(windows, relief= 'sunken', bg= "black")
    frame.pack(fill= BOTH, expand= True, padx= 150, pady=20)

    def RediRestock():
        windows.destroy()
        samplecontent()

    def RediView():
        windows.destroy()
        ViewContent = tk.Tk()
        ViewContent.title('View')
        ViewContent.geometry('1024x768')
        ViewContent.config(background="#000000")

        frame= tk.Frame(ViewContent, relief= 'sunken', bg= "black")
        frame.pack(fill= BOTH, expand= True, padx= 150, pady=20)

        heading = tk.Label(frame, text='GINSILOG\'S PRODUCT MANAGEMENT SYSTEM',fg="#FFFFFF",bg="#000000",font=("Verdana",40),wraplength='924',borderwidth=1, relief="groove",width=20)
        heading.grid(row=0,padx=10,pady=10)

        ViewContent.mainloop()

    def RediSell():
        windows.destroy()
        SellHere()

    def RediReport():
        windows.destroy()
        ReportContent = tk.Tk()
        ReportContent.title('Report')
        ReportContent.geometry('1024x768')
        ReportContent.config(background="#000000")

        frame= tk.Frame(ReportContent, relief= 'sunken', bg= "black")
        frame.pack(fill= BOTH, expand= True, padx= 150, pady=20)

        heading = tk.Label(frame, text='GINSILOG\'S PRODUCT MANAGEMENT SYSTEM',fg="#FFFFFF",bg="#000000",font=("Verdana",40),wraplength='924',borderwidth=1, relief="groove",width=20)
        heading.grid(row=0,padx=10,pady=10)

        ReportContent.mainloop()

    heading = tk.Label(frame, text='GINSILOG\'S PRODUCT MANAGEMENT SYSTEM',fg="#FFFFFF",bg="#000000",font=("Verdana",40),wraplength='924',borderwidth=1, relief="groove",width=20)
    heading.grid(row=0,padx=10,pady=10)



    Restock_button =tk.Button(frame, text='RESTOCK',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= lambda :RediRestock())
    Restock_button.grid(row=2,column=0, pady=(40, 10))

    View_button =tk.Button(frame, text='VIEW',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= lambda :RediView())
    View_button.grid(row=3,column=0, pady=(20, 10))

    Sell_button =tk.Button(frame, text='SELL',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= lambda :RediSell())
    Sell_button.grid(row=4,column=0, pady=(20, 10))

    Report_button =tk.Button(frame, text='REPORT',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised', command= lambda :RediReport())
    Report_button.grid(row=5,column=0, pady=(20, 10))

    windows.mainloop()
