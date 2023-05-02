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
        self.recipeNameEntry.delete(0, END)
        self.descriptionEntry.delete(0, END)
        self.instructionsEntry.delete(0, END)
        self.cat.set(self.category_default)
        
    #Clear fields for the ingredients
    def clear_ingredients(self):
        self.ingredientsList.delete(0, END)
        
    def add_ingredient(self):
        pass
    def remove_ingredient(self):
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
            self.db.connected = True
            self.connectButton.config(text="Disconnect")
        else:
            self.db.disconnect()
            self.clear_fields()
            self.clear_ingredients()
            self.connectButton.config(text="Connect")
            self.recipe_insertFrame.config(height=10)
            self.recipe_savebtn.grid_forget()
            self.recipe_cancelbtn.grid_forget()
            self.recipe_createbtn['state'] = NORMAL
            self.recipe_createbtn.config(text="insert")
            self.db.connected = False
            self.currentRecipe = 0

    def insert_recipe(self):
        if(self.db.connected):
            if(not self.midInsert):
                self.clear_fields()
                self.clear_ingredients()
                self.midInsert = True                       
                       
    def save_recipe(self):
        pass
    
    def cancel_insert(self):
        pass
    
    def update_recipe(self):
        pass
                       
    def __init__(self):
        
        self.db = DataStructure()
        
        self.category_default = "Breakfast"
        
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
        self.recipeNameEntry = tk.Entry(self.inputFrame, width=20)
        self.description = tk.Label(self.inputFrame, text="Description:")
        self.descriptionEntry = tk.Text(self.inputFrame, height=5, width=20)
        self.instructions = tk.Label(self.inputFrame, text="Instructions:")
        self.instructionsEntry = tk.Text(self.inputFrame, height=5, width=20)
        
        # category option menu
        self.categories = ["Breakfast", "Lunch", "Dinner", "Dessert", "Snack"]
        self.category = tk.Label(self.inputFrame, text="Category:")
        self.cat = tk.StringVar(self.inputFrame)
        self.cat.set(self.category_default)
        self.categoryEntry = tk.OptionMenu(self.inputFrame, self.cat, *self.categories)
        
        
        #Create a listbox for the ingredients
        
        self.ingredients = tk.Label(self.inputFrame, text="Ingredients:")
        self.ingredientsList = tk.Listbox(self.inputFrame, height=5, width=20)
        
        #Create a scrollbar for the ingredients listbox
        self.ingredientsScrollbar = tk.Scrollbar(self.inputFrame, orient=VERTICAL)
        self.ingredientsList.config(yscrollcommand=self.ingredientsScrollbar.set)    
        self.ingredientsScrollbar.config(command=self.ingredientsList.yview)
        
        #Create buttons to add and remove ingredients
        self.add_ingredient_btn = tk.Button(self.inputFrame, text="Add Ingredient", command=self.add_ingredient)
        self.remove_ingredient_btn = tk.Button(self.inputFrame, text="Remove Ingredient", command=self.remove_ingredient)
        
        #Gridding above elements
        self.recipeIdNum.grid(row=0, column=1)
        self.recipeIdLabel.grid(row=0, column=0)
        self.recipeName.grid(row=1, column=0)
        self.recipeNameEntry.grid(row=1, column=1)
        self.description.grid(row=2, column=0)
        self.descriptionEntry.grid(row=2, column=1)
        self.instructions.grid(row=3, column=0)
        self.instructionsEntry.grid(row=3, column=1)
        self.category.grid(row=4, column=0)
        self.categoryEntry.grid(row=4, column=1)
        self.ingredients.grid(row=5, column=0)
        self.ingredientsList.grid(row=5, column=1)
        self.ingredientsScrollbar.grid(row=5, column=2, sticky=N+S)
        
        
        #CRUD buttons and frames
        self.editFrame = tk.Frame(self.middle, height=104, width=105)
        self.editFrame.place(x=400,y=200)
        self.recipe_insertFrame = tk.Frame(self.middle, height=15, width=105)
        self.recipe_insertFrame.place(x=400,y=120)
        
        self.recipe_createbtn = tk.Button(self.recipe_insertFrame, text="Insert", command=self.insert_recipe, width=5)
        self.recipe_savebtn = tk.Button(self.recipe_insertFrame, text="Save insert", command=self.save_recipe, width=5)
        self.recipe_cancelbtn = tk.Button(self.recipe_insertFrame, text="Cancel", command=self.cancel_insert, width=5)
        self.recipe_updatebtn = tk.Button(self.editFrame, text="Update", command=self.update_recipe, width=5)
        self.recipe_deletebtn = tk.Button(self.editFrame, text="Delete", command=self.delete_confirmation, width=5)
        
        self.recipe_createbtn.grid(row=0,column=0)
        
        self.recipe_updatebtn.grid(row=1,column=0)
        self.recipe_deletebtn.grid(row=2,column=0)
        
        #Create the feedback label
        self.feedback = tk.Label(self.middle, text="Connect")
        self.feedback.place(x=320,y=60)
        
        #Data navigation buttons
        
        
        
        
        
        
        
       
        
        
        
        
       
        
        self.root.mainloop()
    
    