from cProfile import label
from tkinter import *
from tkinter.tix import INTEGER, ButtonBox
from turtle import width

def SellHere():
    window = Tk()
    window.title("Ginsilog's Product Management")
    window.geometry("1024x768")
    window.config(background= "#000000")
        
    frame= Frame(window, relief= 'sunken', bg= "black")
    frame.pack(fill= BOTH, expand= True, padx= 150, pady=20)

    Cancel = Button(frame, text='Cancel',width=15,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised')
    Cancel.grid(row=0,column=0, pady=(10, 10))

    Random = Label(frame,text='SEARCH RESULT WINDOW',width=25,height=15,font='Helvetica 20 bold',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised')
    Random.grid(row=1,column=1, padx=10,pady=(10, 10),rowspan=6)

    search_text = StringVar()
    search1 = Entry(frame,textvariable=search_text, fg='#FFFFFF', bg='#000000', font="Arial, 30",width=10)
    search1.grid(row=1,column=0, pady=(10, 10))

    search = Button(frame, text='SEARCH',width=10,font='Arial, 30',bg='#000000',fg='#ffffff',borderwidth=8,relief='raised')
    search.grid(row=2,column=0, pady=(10, 10))

    price = Label(frame, text='Quantity',width=10,height=1,font='Arial, 30',bg='#000000',fg='#ffffff')
    price.grid(row=3,column=0, pady=(10, 10))

    quantity_val = IntVar()
    quantity1 = Entry(frame, textvariable=quantity_val, fg='#FFFFFF', bg='#000000', font="Arial, 30",width=10)
    quantity1.grid(row=4,column=0, pady=(10, 10))


    price = Label(frame, text='Price Sold',width=10,height=1,font='Helvetica 20 bold',bg='#000000',fg='#ffffff')
    price.grid(row=5,column=0, pady=(10, 10))

    price_val = DoubleVar()
    price1 = Entry(frame, textvariable=price_val, fg='#FFFFFF', bg='#000000', font="Arial, 30",width=10)
    price1.grid(row=6,column=0, pady=(10, 10))



    btn = Button(frame, text='Delete BTN', fg='#FFFFFF', bg='#000000', font="Arial, 20",width=10)
    btn.grid(row=7,column=0, pady=(10, 10),columnspan=2)

    window.mainloop()




