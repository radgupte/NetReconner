#!/usr/bin/env python
from tkinter import *


def save_info():
    regex_info = Regex.get()
    filenumber_info = File_Number.get()

    print(regex_info, filenumber_info)
    regex.delete(0, END)
    File_Number.delete(0, END)

    if filenumber_info == 'xss' or filenumber_info == 'XSS':
        with open('regex-database/temp_xss_regex.txt', 'w') as t1:
            t1.write(regex_info)
            t1.write('\n')
        label = Label(screen, text="Saved successfully!", height=300)
        # this creates a new label to the GUI
        label.pack()

    if filenumber_info == 'sqli' or filenumber_info == 'SQLI':
        with open('regex-database/temp_sqli_regex.txt', 'w') as t2:
            t2.write(regex_info)
            t2.write('\n')
        label = Label(screen, text="Saved successfully!", height=300)
        # this creates a new label to the GUI
        label.pack()

    if filenumber_info == 'dos' or filenumber_info == 'DOS':
        with open('regex-database/temp_dos_regex.txt', 'w') as t3:
            t3.write(regex_info)
            t3.write('\n')
        label = Label(screen, text="Saved successfully!", height=300)
        # this creates a new label to the GUI
        label.pack()


screen = Tk()  # to initialize a screen
screen.geometry("1000x1000")
screen.title('Admin form')
heading = Label(text='python form', bg='grey', fg='yellow')
heading.pack()  # to put the heading in the centre

Regex = Label(text='Regex')
File_Number = Label(text='Attack Type')
Regex.place(x=10, y=100)
File_Number.place(x=10, y=150)

Regex = StringVar()
File_Number = IntVar()

regex = Entry(text=Regex)
File_Number = Entry(text=File_Number)
regex.place(x=100, y=100)
File_Number.place(x=100, y=150)

register = Button(text='Add to data', command=save_info)
register.place(x=10, y=200)

screen.mainloop()
