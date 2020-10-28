# Question 1
#Laeeqah Esau

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("500x500")
window.title("Ticket Sales")
window.configure(background= "green")
frame = Frame(window)

l1 = Label(window, text = "Enter CellNumber: " ,justify = "left")
l1.pack(side = LEFT)
l1.place(x= 1, y= 1)


cellnum = Entry(window, bd = 1)
cellnum.pack(side = RIGHT)
cellnum.place(x = 200, y = 1)

#Making label and combobox
var2 = StringVar()
var2.set("Select Ticket")

l2 = Label(window, text = "Select Ticket Category: ",justify = "left")
l2.pack(side = LEFT)
l2.place(x = 1, y = 50)

var2 = StringVar()
var2.set("Select Ticket")
tprice = ttk. Combobox(window, value =("Soccer", "Movie", "Theater") , textvariable = var2)
tprice.pack(side = RIGHT)
tprice.place(x = 200, y = 50)

#Making a spinbox with label
var = IntVar()
var.set(0)

l3 = Label(window, text = "Number of Tickets Bought: ", justify= "left")
l3.pack(side = LEFT)
l3.place(x = 1, y = 100)

var = IntVar()
var.set(0)
nr_tickets = Spinbox(window, from_=0, to=30, width = 5, textvariable = var)
nr_tickets.pack(side = RIGHT)
nr_tickets.place(x = 200, y = 100)

#Buttons and calculating


class clsTicketSales():
    def ___init__(self, cellnum, tprice, nr_tickets):
        self.cellnum = cellnum
        self.tprice = tprice
        self.nr_tickets = nr_tickets
        return


def CalcPrepayment():

    self = tprice.get()
    if  self == "Soccer":
        priceOfTickets = 40
    elif self == "Movie":
        priceOfTickets = 75
    elif self == "Theater":
        priceOfTickets = 100
    else:
        displayLabel = Label(window, text="Please select what ticket you would like")
        displayLabel.pack(side =LEFT)
        displayLabel.place(x = 1, y = 250)


    ticketAmt = nr_tickets.get()
    if ticketAmt == "0":
        displayLabel = Label(window, text="Please select how much tickets you would like")
        displayLabel.pack(side =LEFT)
        displayLabel.place(x = 1, y = 400)
    else:
        totalPrice = float(ticketAmt) * float(priceOfTickets) + 0.14
        strTotalPrice = str(totalPrice)
        displayLabel = Label(window, text="Amount Payable: R" + strTotalPrice + "\n" + "Reservation for " + self + " for " + ticketAmt + "\n" + "was done by " + cellnum.get())
        displayLabel.pack(side =LEFT)
        displayLabel.place(x = 1, y = 300)

    var = IntVar()
    var.set()
    nr_tickets.config(textvariable = var)
    var2 = StringVar()
    var2.set("soccer" ,"Movie","theater")
    tprice.config(textvariable = var2)
    displayLabel = Label()
    displayLabel.set(self)
    displayLabel.config(totalPrice)
    
    

    
btn1 = Button(window, text = "Calculate Ticket", command = CalcPrepayment)
btn1.pack(side = RIGHT)
btn1.place(x = 1, y = 150)
    

#clear everything
def clear_all():
    cellnum.delete(0,END)
    var = IntVar()
    var.set(0)
    nr_tickets.config(textvariable = var)
    var2 = StringVar()
    var2.set("")
    tprice.config(textvariable = var2)


btn2 = Button(window, text = "Clear Entries", command = clear_all)
btn2.pack( side= LEFT)
btn2.place(x = 200, y = 150 )


window.mainloop()
