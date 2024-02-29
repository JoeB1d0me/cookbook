"""13/04/2023
🤫🧏‍♀️
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
import traceback

from database import DataStructure

class BookApp():
    
    def about(self):
        tk.messagebox.showinfo("About", "This is a digital cookbook" )
        
    def help_display(self):
        tk.messagebox.showinfo("About", "This is a digital cookbook" )
        

    def clear_fields(self):
        #Clears all entry fields and sets the option menu to the first option
        self.recipeIdNum.config(text="0")
        self.recipeNameEntry.delete(0, tk.END)
        self.descriptionEntry.delete('1.0', 'end')
        self.instructionsEntry.delete('1.0', 'end')
        self.cat.set(self.category_default)
        
    #Clear fields for the ingredients
    def clear_ingredients(self):
        self.ingredientsList.delete(0, tk.END)
        
    def add_ingredient(self):
        if (self.midInsert):
            # open a new window to add a new ingredient to the recipe
            self.ingredient_window = tk.Toplevel(self.root)

            # create labels and entry fields for the ingredient data
            self.ingredientIdLabel = tk.Label(self.ingredient_window, text="Ingredient ID")
            self.ingredientIdLabel.grid(row=0, column=0, padx=10, pady=10)
            self.ingredientIdNum = tk.Label(self.ingredient_window, text=self.storeIngredient[0])
            self.ingredientIdNum.grid(row=0, column=1, padx=10, pady=10)
            
            self.ingredient_name_label = tk.Label(self.ingredient_window, text="Ingredient Name")
            self.ingredient_name_label.grid(row=1, column=0, padx=10, pady=10)
            self.ingredient_name_entry = tk.Entry(self.ingredient_window)
            self.ingredient_name_entry.grid(row=1, column=1, padx=10, pady=10)
            
            

            self.ingredient_quantity_label = tk.Label(self.ingredient_window, text="Ingredient Quantity")
            self.ingredient_quantity_label.grid(row=2, column=0, padx=10, pady=10)
            self.ingredient_quantity_entry = tk.Entry(self.ingredient_window)
            self.ingredient_quantity_entry.grid(row=2, column=1, padx=10, pady=10)
            
            self.ingredient_unit_label = tk.Label(self.ingredient_window, text="Ingredient Unit")
            self.ingredient_unit_label.grid(row=3, column=0, padx=10, pady=10)
            self.ingredient_unit_entry = tk.Entry(self.ingredient_window)
            self.ingredient_unit_entry.grid(row=3, column=1, padx=10, pady=10)

            # create a button to add the new ingredient to the listbox and close the window
            add_ingredient_button = tk.Button(self.ingredient_window, text="Add Ingredient", command=self.insert_ingredient)
            add_ingredient_button.grid(row=4, column=0, columnspan=2, pady=10)

    def insert_ingredient(self):
        try:
            if (self.midInsert):
                self.ingredientName = self.ingredient_name_entry.get()
                self.ingredientQuantity = self.ingredient_quantity_entry.get()
                self.ingredientUnit = self.ingredient_unit_entry.get()
                self.db.addIngredient = [self.ingredientName, float(self.ingredientQuantity), self.ingredientUnit]
                self.storeIngredient = self.db.addIngredient
                self.db.add_ingredient()
                self.listOfIngredients.append((self.ingredientName, self.ingredientQuantity, self.ingredientUnit))
                self.ingredientsList.insert(tk.END, self.ingredientName + " " + self.ingredientQuantity + " " + self.ingredientUnit)
                # close the window
                self.ingredient_window.destroy()
            
        except Exception:
            print(traceback.format_exc())
            tk.messagebox.showerror("Error", "Invalid input")
        
    def remove_ingredient(self):
          # remove the selected ingredient from the list of ingredients and from the listbox
            selected_ingredient = self.ingredientsLists.curselection()
            if (selected_ingredient):
                self.ingredientsList.delete(selected_ingredient)
                del self.listOfIngredients[selected_ingredient[0]]
                self.db.delete_ingredient(self.ingredientName)
            else:
                tk.messagebox.showerror("Error", "No ingredient selected")

    
    def delete_confirmation(self):
       a= tk.messagebox.askyesnocancel("Delete", "Are you sure?")
       if(a):
           self.delete_recipe(self.currentRecipe)
           self.feedback.config(text="Recipe deleted")
               
    def exit(self):
        feedback = tk.messagebox.askyesnocancel("Exit", "Are you sure?")
        if(feedback):
            self.root.destroy()
    
    def connect_handle(self):
        if(not self.db.connected):
            try:
                a = self.db.connect("localhost", "3306", "root", "Hhk,c1bU4am?", "cookbook_test_case")
                if(a == 0):
                    self.feedback.config(text="Connected to database")
                    self.db.connected = True
                    self.connectButton.config(text="Disconnect")
                    self.recipe_createbtn['state'] = NORMAL
                    self.db.get_recipe()
                    self.db.get_recipe_ingredients
                else:
                    self.feedback.config(text="Connection failed")
            except Exception as e:
                print(e)
                self.feedback.config(text="Connection failed")
                
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
                self.recipe_insertFrame.config(height=40)
                self.recipe_savebtn.grid(row=1)
                self.recipe_cancelbtn.grid(row=2)
                self.recipe_createbtn.config(text="cleared")
                self.recipe_createbtn['state'] = DISABLED    
                self.midInsert = True           
            else:
                print("Error")       
                
    def save_recipe(self):
        try:
         if(self.midInsert):
            self.name = self.recipeNameEntry.get()
            self.description = self.descriptionEntry.get("1.0", "end")
            self.instructions = self.instructionsEntry.get("1.0", "end")
            self.category = self.cat.get()
            self.db.addRecipe = [self.name, self.description, self.instructions, self.category]
            self.db.add_recipe()
            self.storeRecipe = self.db.addRecipe
            self.recipe_createbtn['state'] = NORMAL
            self.recipe_createbtn.config(text="New")
            self.feedback.config(text="Recipe saved")
            self.midInsert = False
            self.clear_fields()
            self.clear_ingredients()
            self.display_recipe(0)
            self.display_ingredients(0)
            self.recipe_insertFrame.config(height=10)
            self.recipe_savebtn.grid_forget()
            self.recipe_cancelbtn.grid_forget()
        except Exception:
            print(traceback.format_exc())
            tk.messagebox.showerror("Error", "Invalid input")
             
    def cancel_recipe(self):
        self.recipe_insertFrame.config(height=10)
        self.recipe_savebtn.grid_forget()
        self.recipe_cancelbtn.grid_forget()
        self.recipe_createbtn['state'] = NORMAL
        self.recipe_createbtn.config(text="New")
        self.feedback.config(text="Insert cancelled")   
        self.midInsert = False
        self.clear_fields()
        self.clear_ingredients()
        self.display_recipe(0)
        self.display_ingredients(0) 
    
    def pull_recipe(self):
        try:
            self.name = self.recipeNameEntry.get()
            self.description = self.descriptionEntry.get("1.0", "end")
            self.instructions = self.instructionsEntry.get("1.0", "end")
            self.category = self.cat.get()
            
            self.db.add_recipe = [self.name, self.description, self.instructions, self.category]
        except Exception as e:
            tk.messagebox.showerror("Error", "Error pulling recipe")
            print(e) #Debug check
            
    # Pulls ingredients from the listbox and adds them to the database
    def pull_ingredient(self):
        try:
            for ingredient in self.listOfIngredients:
                self.ingredientName, self.ingredientQuantity, self.ingredientUnit = ingredient
                self.db.addIngredient = [self.ingredientName, float(self.ingredientQuantity), self.ingredientUnit]
                self.storeIngredient = self.db.addIngredient
                self.db.add_ingredient()
        except Exception as e:
            tk.messagebox.showerror("Error", "Error pulling ingredients")
            print(e)
        
    # Displays recipe    
    def display_recipe(self, index):
        try:
            self.tempRecipe = self.db.recipes[index]
            (self.recipeID, self.recipeName, self.recipeDescription, self.recipeInstructions, self.recipeCategory ) = self.tempRecipe
            self.recipeIdNum.config(text=self.recipeID)
            self.clear_fields()
            self.recipeNameEntry.insert(0, self.recipeName)
            self.descriptionEntry.insert("1.0", self.recipeDescription)
            self.instructionsEntry.insert("1.0", self.recipeInstructions)
            self.cat.set(self.recipeCategory)
        except Exception as e:
            self.feedback.config(text="Error: " + str(e))
            print(traceback.format_exc())
        
    # Displays ingredients
    def display_ingredients(self, recipeID):
        try:
            self.tempIngredients = self.db.ingredients[recipeID]
            (self.ingredientID, self.ingredientName, self.ingredientQuantity, self.ingredientUnit) = self.tempIngredients
            self.clear_ingredients()
            for i in self.tempIngredients:
                self.listOfIngredients.append(i)
                self.ingredientsList.insert(END, i[0] + " - " + i[1])
        except Exception as e:
            self.feedback.config(text="No ingredients available")
            print(traceback.format_exc())
    # Update recipe
    def update_recipe(self):
        if(self.db.connected):
            self.recipeID = self.recipeIdNum.cget("text")
            self.name = self.recipeNameEntry.get()
            self.description = self.descriptionEntry.get( "1.0", "end")
            self.instructions = self.instructionsEntry.get( "1.0", "end")
            self.category = self.cat.get()
            self.db.update_recipe = [self.recipeID, self.name, self.description, self.instructions, self.category]
            self.db.update_recipe()
            self.feedback.config(text="Recipe updated")
            self.display_recipe(self.currentRecipe)
        else:
            self.feedback.config(text="Not connected to database")
            
    # Delete recipe
    def delete_recipe(self, index):
        self.db.delete_recipe(index)
        self.feedback.config(text="Recipe deleted")
        self.display_recipe(0)
        self.display_ingredients(0)
        
        
    def resetID(self):
        self.currentRecipe = 0
        self.currentIngredient = 0
        
    #Sorts through recipes
    def navigate_recipe(self, directionindex):
        self.currentRecipe += directionindex
        if(self.currentRecipe < 0):
            self.currentRecipe = len(self.db.recipes)-1
        elif(self.currentRecipe > len(self.db.recipes)-1):
            self.currentRecipe = 0
        self.display_recipe(self.currentRecipe)
        
                       
    def __init__(self):
        
        self.db = DataStructure()
        
        
        
        self.category_default = "Breakfast"
        
        self.currentRecipe = 0
        self.tempRecipe = (0, "", "", "", "")
        self.currentIngredient = 0
        
        self.storeIngredient = ["",0.0,""]
        self.listOfIngredients = []
        
        self.tempIngredients = (0,"",0.0,"")
        
        
        
        self.midInsert = False
        
        self.msg = ""
        
        self.root = tk.Tk()
        self.root.title("cookbook")
        self.root.resizable(False, False)
        self.root.geometry("720x405")
        

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
        self.mainFrame = tk.Frame(self.root, height=405, width=720)
        self.mainFrame.grid(row=0,column=0)
        
        self.middle = tk.Frame(self.mainFrame, height=385, width=720)
        self.middle.place(x=40,y=0)
        
        # Data insert frame
        self.inputFrame = tk.Frame(self.middle, height=365, width=710)
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
        self.descriptionEntry = tk.Text(self.inputFrame, height=3, width=20)
        self.instructions = tk.Label(self.inputFrame, text="Instructions:")
        self.instructionsEntry = tk.Text(self.inputFrame, height=3, width=20)
        
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
        
        #Grid the buttons
        self.add_ingredient_btn.grid(row=7, column=0)
        self.remove_ingredient_btn.grid(row=7, column=1)
        
        #Gridding above elements
        self.recipeIdNum.grid(row=0, column=1)
        self.recipeIdLabel.grid(row=0, column=0)
        self.recipeName.grid(row=1, column=0)
        self.recipeNameEntry.grid(row=1, column=1)
        self.description.grid(row=3, column=0)
        self.descriptionEntry.grid(row=3, column=1)
        self.instructions.grid(row=4, column=0)
        self.instructionsEntry.grid(row=4, column=1)
        self.category.grid(row=5, column=0)
        self.categoryEntry.grid(row=5, column=1)
        self.ingredients.grid(row=6, column=0)
        self.ingredientsList.grid(row=6, column=1)
        self.ingredientsScrollbar.grid(row=6, column=2, sticky=N+S)
        
        
        #CRUD buttons and frames
        self.editFrame = tk.Frame(self.middle, height=104, width=105)
        self.editFrame.place(x=400,y=200)
        self.recipe_insertFrame = tk.Frame(self.middle, height=15, width=105)
        self.recipe_insertFrame.place(x=400,y=120)
        
        self.recipe_createbtn = tk.Button(self.recipe_insertFrame, text="Insert", command=self.insert_recipe, width=10)
        self.recipe_savebtn = tk.Button(self.recipe_insertFrame, text="Save insert", command=self.save_recipe, width=10)
        self.recipe_cancelbtn = tk.Button(self.recipe_insertFrame, text="Cancel", command=self.cancel_recipe, width=10)
        self.recipe_updatebtn = tk.Button(self.editFrame, text="Update", command=self.update_recipe, width=5)
        self.recipe_deletebtn = tk.Button(self.editFrame, text="Delete", command=self.delete_confirmation, width=5)
        
        self.recipe_createbtn.grid(row=0,column=0)
        
        self.recipe_updatebtn.grid(row=1,column=0)
        self.recipe_deletebtn.grid(row=2,column=0)
        
        #Create the feedback label
        self.feedback = tk.Label(self.middle, text="Connect")
        self.feedback.place(x=320,y=60)
        
        #Data navigation buttons
        self.dataFrame = tk.Frame(self.middle, height=15, width=105)
        self.dataFrame.place(x=200,y=340)
        self.firstbtn = tk.Button(self.dataFrame, text="First", command=lambda:[self.resetID(), self.display_recipe(0)], width=5)
        self.prevbtn = tk.Button(self.dataFrame, text="Prev", command=lambda:[self.navigate_recipe(-1)], width=5)
        self.nextbtn = tk.Button(self.dataFrame, text="Next", command=lambda:[self.navigate_recipe(1)], width=5)
        self.lastbtn = tk.Button(self.dataFrame, text="Last", command=lambda:[self.navigate_recipe(len(self.db.recipes))], width=5)        
        
        self.firstbtn.grid(row=0,column=0)
        self.prevbtn.grid(row=0,column=1)
        self.nextbtn.grid(row=0,column=2)
        self.lastbtn.grid(row=0,column=3)
        
       
        
        self.root.mainloop()
    
    
