"""13/04/2023
CS50AP
Master Project
"""
from database.struct import DataStructure
import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import OptionMenu
from tkinter import messagebox
from tkinter.messagebox import showerror,showinfo,showwarning,YESNOCANCEL,YESNO
import os,sys
import PIL

class BookApp():
    def help_display(self):
        tk.messagebox.showinfo("About", "This is a digital cookbook" )
    def clear_fields(self):
        pass
    def delete_confirmation(self):
        pass
    def exit(self):
        feedback = tk.messagebox.askyesnocancel("Exit", "Are you sure?")
        if(feedback):
            self.root.destroy()
    
    def connect_handle(self):
        if(not self.db.connected):
            a = self.db.connect()
            self.feedback.config(text=a)
            self.connect
    
    def __init__(self):
        self.db = DataStructure()
        
        self.currentRecipe = 0
        self.holdRec = ()
        
        self.msg = ""
        
        self.root = tk.Tk()
        self.root.title("cookbook")
        self.root.resizable(False, False)
        
        self.mainFrame = tk.Frame(self.root, height=800, width=600)
        self.mainFrame.grid(row=0,column=0)
        
        # Menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        self.file_menu = tk.Menu(menubar)
        self.menubar.add_cascade(label="File", menu=file_menu)
        self.add_command(label="Exit", command=self.exit_program)
        help_menu = tk.Menu(menubar)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)