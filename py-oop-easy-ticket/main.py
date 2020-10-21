# Question 1
#Laeeqah Esau

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("500x500")
window.title("Ticket Sales")

frame = Frame(window)

l1 = Label(window, text = "Enter CellNumber: " ,justify = "left")
l1.pack(side = LEFT)
l1.place(x= 1, y= 1)


e1 = Entry(window, bd = 1)
e1.pack(side = RIGHT)
e1.place(x = 200, y = 1)

#Making label and combobox

l2 = Label(window, text = "Select Ticket Category: ",justify = "left")
l2.pack(side = LEFT)
l2.place(x = 1, y = 50)

var2 = StringVar()
var2.set("Select Ticket")
drop = ttk. Combobox(window, value =("Soccer", "Movie", "Theater") , textvariable = var2)
drop.pack(side = RIGHT)
drop.place(x = 200, y = 50)

#Making a spinbox with label


l3 = Label(window, text = "Number of Tickets Bought: ", justify= "left")
l3.pack(side = LEFT)
l3.place(x = 1, y = 100)

var = IntVar()
var.set(0)
box = Spinbox(window, from_=0, to=100, width = 5, textvariable = var)
box.pack(side = RIGHT)
box.place(x = 200, y = 100)

#Buttons and calculating
btn1 = Button(window, text = "Calculate Ticket")
btn1.pack(side = RIGHT)
btn1.place(x = 1, y = 150)

class clsticketsales:
    def __init__(self):
        self. soccer = 40
        self. movie = 75
        self. theater = 100

class CellNumber(clsticketsales):
    def __init__(self):
        self.cellnumber =

def AmountPayable(ticketsales):
    AmountPayable=nr_tickets * tPrice + 14% VAT




#clear everything
def clear_all():
    e1.delete(0,END)
    var = IntVar()
    var.set(0)
    box.config(textvariable = var)
    var2 = StringVar()
    var2.set("")
    drop.config(textvariable = var2)


btn2 = Button(window, text = "Clear Entries", command = clear_all)
btn2.pack( side= LEFT)
btn2.place(x = 200, y = 150 )












window.mainloop()
