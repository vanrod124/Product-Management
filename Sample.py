import tkinter as tk
from tkinter import ttk,messagebox,BOTH
from tkinter.font import BOLD
from turtle import width

def samplecontent():
    RestockContent = tk.Tk()
    RestockContent.title('Restock')
    RestockContent.geometry('1024x768')
    RestockContent.config(background="#000000")

    frame= tk.Frame(RestockContent, relief= 'sunken', bg= "black")
    frame.pack(fill= BOTH, expand= True, padx= 150, pady=20)

    heading = tk.Label(frame, text='This is restock',fg="#FFFFFF",bg="#000000",font=("Verdana",40),wraplength='924',borderwidth=1, relief="groove",width=20)
    heading.grid(row=0,padx=10,pady=10)

    RestockContent.mainloop()
