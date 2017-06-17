#!/usr/bin/python3

#import tkinter as tk
from tkinter import tix

class App:

    def __init__(self, master):

        frame = tix.Frame(master)
        frame.pack()

        self.entry_field = tix.Entry(master)
        self.entry_field.pack(side='bottom', fill=tix.X, expand=1)

        self.text_field = tix.Text(master)
        self.text_field.pack(side='right', fill=tix.BOTH, expand=1)

        #self.canvas = tk.Canvas(master)
        #self.canvas.pack(side='left', fill=tk.BOTH, expand=1)

        self.dir_list = tix.DirTree(master, command=self.say_hi_dir, showhidden=True)
        self.dir_list.pack(side='left', fill=tix.BOTH, expand=1)

        menubar = tix.Menu(root)

        #create a pulldown menu, and add it to the menu bar
        filemenu = tix.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.say_hi)
        filemenu.add_command(label="Save", command=self.say_hi)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        #display the menu
        root.config(menu=menubar)

    def say_hi_dir(self, my_dir):
        print("hi there, ", my_dir)

    def say_hi(self):
        print("hi there, everyone!")

root = tix.Tk()

app = App(root)

root.mainloop()
root.destroy()
