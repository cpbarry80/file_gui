import os
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
from listfiles import files_potentially_missing
from pandastable import Table, TableModel

# setup container window
container = tk.Tk()
container.geometry('1200x900')
container.title('file recon')
w = Label(container, justify=LEFT, text ='1. find old model work files in new model work files \n 2. files highlighted red are likely missing \n 3. numbers, spaces, periods and underscores are removed before matching \n', font = "50") 
w.pack(pady=20, side= TOP, anchor="w")


# define listbox and its contents
folder = 'C:\Models'
filelist = [fname for fname in os.listdir(folder)]
list_items = tk.StringVar(value=filelist)
listbox = tk.Listbox(listvariable=list_items, height=len(filelist), selectmode='browse')
listbox.pack(fill='x')


f = Frame(container)
f.pack(fill='x')

# get contents for text box
def files_needed(event):
    folder_selected = listbox.get(listbox.curselection()[0])
    old_folder = f'C:\Models\{folder_selected}\OLD MODEL\WORK'
    new_folder = f'C:\Models\{folder_selected}\CURRENT MODEL\WORK'

    df  = files_potentially_missing(old_folder, new_folder)
    pt = Table(f, dataframe=df)
    mask_1 = pt.model.df['match_score'].astype(float) <= 0.5
    pt.setColorByMask('old model file', mask_1, 'red')
    pt.show()

listbox.bind('<<ListboxSelect>>', files_needed)
container.mainloop()


