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
        
        self.mainFrame = tk.Frame(self.root, height=650, width=1150)
        self.mainFrame.grid(row=0,column=0)
        
        #creating the menu object
        self.mainMenu = tk.Menu(self.mainFrame)
        self.root.config(menu = self.mainMenu)
        self.fileMenu = tk.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="File", menu=self.fileMenu, underline=0)
        
        self.fileMenu.add_command(label="Exit", command=self.exit)
        self.

    