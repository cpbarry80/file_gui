from curses.textpad import Textbox
import os
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *

# setup container window
container = tk.Tk()
container.geometry('600x400')
container.title('missing files')
w = Label(container, text ='\n \n compare contents of old work and new work \n \n', font = "50") 
w.pack()


# define listbox and its contents
folder = '/Users/biffbarry/Desktop/models'
filelist = [fname for fname in os.listdir(folder)]
list_items = tk.StringVar(value=filelist)
listbox = tk.Listbox(listvariable=list_items, height=len(filelist), selectmode='browse')
listbox.pack(fill='x')

# define text box
txt = Text(container, height = 200, width = 200)
txt.pack()

# get contents for text box
def files_needed(event):
    folder_selected = listbox.get(listbox.curselection()[0])
    folder = f'/Users/biffbarry/Desktop/models/{folder_selected}'
    filelist = [fname for fname in os.listdir(folder)]
    txt.delete('1.0', END)
    for i in filelist:
        txt.insert('1.0', f'\t {i} \n')


listbox.bind('<<ListboxSelect>>', files_needed)
container.mainloop()


