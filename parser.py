import requests
from bs4 import BeautifulSoup
import csv

import tkinter as tk
from tkinter import Entry, Frame, Label, ttk, Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter.constants import LEFT, W


def makeSound():
    return 0

def createContent():
    global win
    frame1 = Frame(win,bg="Yellow")

    lable1 = Label(frame1, text="Enter text for convert:", font="Arial 14",padx=1, pady=1, bg="Gray")
    lable2 = Label(frame1, text="Catalog for save:", font="Arial 14",padx=1, pady=1, bg="Gray")
    textField1 = Entry(frame1, font="Arial 14",width=31)
    textField2 = Entry(frame1, font="Arial 14",width=31)
    textField2.insert(0,"C:\\Users\\Kolyanys\\AppData\\Roaming\\Leppsoft")
    button_makeSound = tk.Button(frame1, text="Make Sound", font="Arial 14", command=makeSound)

    lable1.grid(row=0, column=0, sticky="w")
    textField1.grid(row=1, column=0, pady=10,sticky="w")
    lable2.grid(row=2, column=0, sticky="w")
    textField2.grid(row=3, column=0, pady=10,sticky="w")
    button_makeSound.grid(row=4, column=0,sticky="w")

    frame1.pack(expand = True, fill='both', padx= 10, pady=10)

    #to do: change catalog

def _quit():
    win.quit()
    win.destroy()
    exit()

def _restart():
    win.destroy()
    _start()

def _start():
    global win
    win = tk.Tk()

    # Add a title
    win.title("Voise Parser")
    # Gets the requested values of the height and widht.
    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(win.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(win.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    win.geometry("400x300+{}+{}".format(positionRight, positionDown))

    # Disable resizing the GUI by passing in False/False
    win.resizable(False, False)

    createContent()

    # Creating a Menu Bar
    menu_bar = Menu(win)
    win.config(menu=menu_bar)

    # Add menu items
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Restart", command=_restart)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=_quit)
    menu_bar.add_cascade(label="Tasks", menu=file_menu)

    # Display a Message Box
    def _msgBox():
        msg.showinfo('Parser Message Info Box',
                    'Its parser for convert text to audio from site ')

    # Add another Menu to the Menu Bar and an item
    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", command=_msgBox)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    # ======================
    # Start GUI
    # ======================
    win.mainloop()

_start()