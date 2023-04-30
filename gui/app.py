"""13/04/2023
CS50AP
Master Project
"""
from struct import DataStructure
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
        self.root.config(menu=self.menubar)
        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.exit)
        self.help_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)
        
        self.buttonsFrame = tk.Frame(self.mainFrame)
        self.buttonsFrame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        
        self.newButton = tk.Button(self.buttonsFrame, text="New", width=10)
        self.newButton.grid(row=0, column=0, padx=5, pady=5)
        self.editButton = tk.Button(self.buttonsFrame, text="Edit", width=10)
        self.editButton.grid(row=0, column=1, padx=5, pady=5)
        self.deleteButton = tk.Button(self.buttonsFrame, text="Delete", width=10)
        self.deleteButton.grid(row=0, column=2, padx=5, pady=5)
        
        # create data entry frame
        self.dataEntryFrame = tk.Frame(self.mainFrame)
        self.dataEntryFrame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.recipeLabel = tk.Label(self.dataEntryFrame, text="Recipe:")
        self.recipeLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.recipeEntry = tk.Entry(self.dataEntryFrame, width=30)
        self.recipeEntry.grid(row=0, column=1, padx=5, pady=5)
        
        self.categoryLabel = tk.Label(self.dataEntryFrame, text="Category:")
        self.categoryLabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.categoryOption = tk.OptionMenu(self.dataEntryFrame, tk.StringVar(), "Select Category", "Category 1", "Category 2", "Category 3")
        self.categoryOption.grid(row=1, column=1, padx=5, pady=5)
        
        self.ingredientFrame = tk.Frame(self.mainFrame)
        self.ingredientFrame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

# create labels and option menus for ingredient data
        self.ingredient_label = tk.Label(self.ingredientFrame, text="Ingredients", font=("Helvetica", 16))
        self.ingredient_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.type_label = tk.Label(self.ingredientFrame, text="Type", font=("Helvetica", 12))
        self.type_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        types = ["Select Type", "Produce", "Protein", "Grain", "Dairy", "Other"]
        self.type_var = tk.StringVar(self.ingredientFrame)
        self.type_var.set(types[0])
        self.type_option = tk.OptionMenu(self.ingredientFrame, self.type_var, *types)
        self.type_option.grid(row=1, column=1, padx=10, pady=10)

        self.name_label = tk.Label(self.ingredientFrame, text="Name", font=("Helvetica", 12))
        self.name_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.ingredientFrame, width=30)
        self.name_entry.grid(row=2, column=1, padx=10, pady=10)

        self.quantity_label = tk.Label(self.ingredientFrame, text="Quantity", font=("Helvetica", 12))
        self.self.quantity_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.quantity_entry = tk.Entry(self.ingredientFrame, width=10)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        self.unit_label = tk.Label(self.ingredientFrame, text="Unit", font=("Helvetica", 12))
        self.unit_label.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        units = ["Select Unit", "tsp", "tbsp", "cup", "oz", "lb", "kg"]
        self.unit_var = tk.StringVar(self.ingredientFrame)
        self.unit_var.set(units[0])
        self.unit_option = tk.OptionMenu(self.ingredientFrame, self.unit_var, *units)
        self.unit_option.grid(row=3, column=3, padx=10, pady=10)

        self.add_ingredient_btn = tk.Button(self.ingredientFrame, text="Add", font=("Helvetica", 12))
        self.add_ingredient_btn.grid(row=4, column=3, padx=10, pady=10, sticky="e")
        self.remove_ingredient_btn = tk.Button(self.ingredientFrame, text="Remove", font=("Helvetica", 12))
        self.remove_ingredient_btn.grid(row=4, column=2, padx=10, pady=10, sticky="e")
                
        
        self.root.mainloop()