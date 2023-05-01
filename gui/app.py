"""13/04/2023
CS50AP
Master Project
"""

import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import OptionMenu
from tkinter import messagebox
from tkinter.messagebox import showerror,showinfo,showwarning,YESNOCANCEL,YESNO
import os,sys
import PIL

from database import DataStructure

class BookApp():
    
    def about(self):
        tk.messagebox.showinfo("About", "This is a digital cookbook" )
        
    def help_display(self):
        tk.messagebox.showinfo("About", "This is a digital cookbook" )
        
        
    def clear_fields(self):
        #Clears all entry fields and sets the option menu to the first option
        self.recipeEntry.delete(0, END)
        self.categoryEntry.delete(0, END)
        self.descriptionEntry.delete(0, END)
        self.instructionsEntry.delete(0, END)
        self.categoryEntry.insert(0, self.categories[0])
        
    #Clear fields for the ingredients
    def clear_ingredients(self):
        self.name_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.unit_var.set(self.units[0])
        
        
    
    def new(self):
        if(self.db.connected):
            if(not self.midInsert):
                self.clear_fields()
                self.clear_ingredients()
                self.midInsert = True
        
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
            self.db.connected = True
            self.connectButton.config(text="Disconnect")
        else:
            self.db.disconnect()
            self.clear_fields()
            self.clear_ingredients()
            self.connectButton.config(text="Connect")
            self.recipe_insertFrame.config(height=10)
            self.recipe
                       
                       
                       
    def __init__(self):
        
        self.db = DataStructure()
        
        
        
        self.currentRecipe = 0
        self.holdRec = ()
        
        self.midInsert = False
        
        self.msg = ""
        
        self.root = tk.Tk()
        self.root.title("cookbook")
        self.root.resizable(False, False)
        self.root.geometry("854x480")
        

        # Menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.exit)
        self.help_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)
        # Frame creation
        self.mainFrame = tk.Frame(self.root, height=480, width=854)
        self.mainFrame.grid(row=0,column=0)
        
        self.middle = tk.Frame(self.mainFrame, height=460, width=854)
        self.middle.place(x=40,y=0)
        
        # Data insert frame
        self.inputFrame = tk.Frame(self.middle, height=440, width=834)
        self.inputFrame.place(x=40,y=0)
        
        #Connection button
        self.connectButton = tk.Button(self.middle, text="Connect", command=self.connect_handle)
        self.connectButton.place(x=320,y=30)
        
        self.recipeIdNum = tk.Label(self.inputFrame, text="")
        self.recipeIdLabel = tk.Label(self.inputFrame, text="Recipe ID:")
        #Input fields
        self.recipeName = tk.Label(self.inputFrame, text="Recipe Name:")
        self.recipeNameEntry = tk.Entry(self.inputFrame, width=30)
        self.description = tk.Label(self.inputFrame, text="Description:")
        self.descriptionEntry = tk.Text(self.inputFrame, height=5, width=30)
        self.instructions = tk.Label(self.inputFrame, text="Instructions:")
        self.instructionsEntry = tk.Text(self.inputFrame, height=5, width=30)
        
        #Button to open the ingredients window
       
        
        
        
        
       
        
        self.root.mainloop()
    
    