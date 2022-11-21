from tkinter import *

def Restock():
    window=Tk()
    window.geometry("1024x768")
    window.title('Restock Product')

    prodlbl=Label(window, text="Product ID", fg='black', padx = 1, font=("Arial", 25))
    prodlbl.place(x=410, y=90)
    quantlbl=Label(window, text="Quantity", fg='black', padx = 1, font=("Arial", 25))
    quantlbl.place(x=430, y=175)
    costlbl=Label(window, text="Product Cost", fg='black', padx = 1, font=("Arial", 25))
    costlbl.place(x=400, y=270)



    txtfldprd = Entry(window, text="Input Box", bd=5, width = 50)
    txtfldprd.place(x=350, y=140)
    txtfldqnt = Entry(window, text="Input Box", bd=5, width = 50)
    txtfldqnt.place(x=350, y=230)
    txtfldcst = Entry(window, text="Input Box", bd=5, width = 50)
    txtfldcst.place(x=350, y=330)

    btnadd=Button(window, text="Add", fg='black', width = 10, font =("Arial", 15, 'bold'))
    btnadd.place(x=50, y=600)
    btncnl=Button(window, text="Cancel", fg='black', width = 10, font =("Arial", 15, 'bold'))
    btncnl.place(x=190, y=600)




    window.mainloop()