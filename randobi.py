from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os, sys
import random

def popup():
    popup = Tk()
    popup.title("Done!")
    root.minsize()
    label = ttk.Label(popup, text="all files in ( {} ) are renamed".format(root.directory))
    label.pack(side="top", fill="x", padx=5, pady=5)
    B1 = ttk.Button(popup, text="Ok", command = popup.destroy)
    B1.pack(pady=5)
    popup.mainloop()

def select():
	root.directory = filedialog.askdirectory()

def randomize():
	print(root.directory)
	for filename in os.listdir(root.directory):	
		src = os.path.join(root.directory, filename)
		rand = str(random.randrange(100000, 999999))
		newname = os.path.join(root.directory, rand)
		spl = os.path.splitext(src)
		os.rename(src, newname + spl[1])
	popup()

root = Tk()
Button(root, text="Open Folder", command=select).pack(side="left", padx=1, pady=5)
Button(root, text="Randomize Names", command=randomize).pack(side="left", padx=1, pady=5)
Button(root, text="Quit", command=root.destroy).pack(side="left", padx=1, pady=5)
root.title("Randomizer")
root.minsize()
root.mainloop()
