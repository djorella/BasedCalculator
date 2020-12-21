#! /usr/bin/python3
import tkinter
from tkinter import *
from tkinter import messagebox
#The Tkinter module (“Tk interface”)
# is the standard Python interface to the Tk GUI toolkit
# Frame of calc
def bCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

# Create Button
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add( '*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('The Based Calculator')
        
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, 
        justify='right', bd=30, bg="powder blue").pack(side=TOP, expand=YES,
        fill=BOTH)

        for clearButton in ("C"):
            erase = bCalc(self, TOP)
            for bchar in clearButton:
                button(erase, LEFT, bchar, lambda storeObj=display, q=bchar: storeObj.set(''))
        
        for negateButton in ("-"):
            negate = bCalc(self, TOP)
            for bchar in negateButton:
                button(negate, LEFT, bchar, lambda storeObj=display, q=bchar: storeObj.set('-' + storeObj.get()))
                
            

        for basedButtons in ("789/", "456*", "123-", "0.+"):
            FunctionNum = bCalc(self, TOP)
            for bEquals in basedButtons:
                button(FunctionNum, LEFT, bEquals, lambda storeObj=display, q=bEquals:
                storeObj.set(storeObj.get() + q))
        equalButton = bCalc(self, TOP)
        for bEquals in "=":
            if bEquals == "=":
                btnbEquals = button(equalButton, LEFT, bEquals)
                btnbEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                storeObj=display: s.calc(storeObj), '+')
                
            else:
                btnbEquals = button(equalButton, LEFT, bEquals, lambda storageObj=display, 
                s =' %s ' % bEquals: storeObj.set(storageObj.get() + s))

    def calc(self, display):
        try: 
            display.set(eval(display.get()))
        except:
            display.set("ERROR")    

if __name__ =='__main__':
   messagebox.showinfo("Welcome!", "Hi, I am the Based Calculator, I am simple and direct.        Have fun interacting with me!")
   app().mainloop()
    
