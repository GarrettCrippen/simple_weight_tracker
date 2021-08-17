import tkinter as tk
from chester import *
from tkinter import ttk
from tkinter import * 

# this is the function called when the button is clicked
def btnClickFunction():
    weight= getInputBoxValue()
    name = getListboxValue()
    try:
        entryToCell(name[0],weight.strip())
    except:
        pass

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInput.get()
	return userInput


# this is a function to get the selected list box value
def getListboxValue():
	itemSelected = listTwo.curselection()
	return itemSelected



root = Tk()

# This is the section of code which creates the main window
root.geometry('278x206')
root.configure(background='#F0F8FF')
root.title('Weight Tracker')


# This is the section of code which creates a button
Button(root, text='submit to google sheets', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=43, y=131)


# This is the section of code which creates a text input box
tInput=Entry(root)
tInput.place(x=76, y=101)


# This is the section of code which creates the a label
Label(root, text='lbs.', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=213, y=105)


# This is the section of code which creates a listbox
listTwo=Listbox(root, bg='#F0F8FF', font=('arial', 12, 'normal'), width=0, height=0)
listTwo.insert('0', 'Garrett')
listTwo.insert('1', 'Chester')
listTwo.place(x=112, y=42)


root.mainloop()

