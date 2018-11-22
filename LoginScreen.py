#This import the tkinter "tool box" this cotains
#all the support material to make GUI elements.
#by including "as tk" we are giving a short name to use.
import tkinter as tk

#With the login page all elements are vertically alligned
#So i am just going to use pack.


#Main Window
root = tk.Tk() #creates the standard main window.
#Tk() is a special function called CONSTRUCTION
#If a function is written with a capital letter it indicates it
#is a constructor.

#********************WIDGET 1********************
#Three stages to build elements/objects
#1. CONSTRUCT the Object: We build and configure it.
#2. Configure the Object: We specify behaviours and settings (OPTIONAL) 
#3. Pack the Object: Put it in the window
labUN = tk.Label(root, text = "User Name")
#ordered parameters: the order we send the matters. (COMMON)
#named parameters: JavaScrypt and Python specific
labUN.pack()

entUn = tk.Entry(root)
entUn.pack(padx = 10)

labPassword = tk.Label(root, text = "Password")
labPassword.pack()

entPassword = tk.Entry(root, show = "*")
entPassword.pack()

btnSumbit = tk.Button(root, text = "Sumbit")
btnSumbit.pack()


#We are writing an EVENT DRIVE PROGRAM. 
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program