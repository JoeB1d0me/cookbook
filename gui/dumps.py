###Stuff that was cut out from code and is being re-addded later:

"""
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
        self.quantity_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.quantity_entry = tk.Entry(self.ingredientFrame, width=10)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        self.unit_label = tk.Label(self.ingredientFrame, text="Unit", font=("Helvetica", 12))
        self.unit_label.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.units = ["Select Unit", "tsp", "tbsp", "cup", "oz", "lb", "kg"]
        self.unit_var = tk.StringVar(self.ingredientFrame)
        self.unit_var.set(self.units[0])
        self.unit_option = tk.OptionMenu(self.ingredientFrame, self.unit_var, *self.units)
        self.unit_option.grid(row=3, column=3, padx=10, pady=10)

        self.add_ingredient_btn = tk.Button(self.ingredientFrame, text="Add", font=("Helvetica", 12))
        self.add_ingredient_btn.grid(row=4, column=3, padx=10, pady=10, sticky="e")
        self.remove_ingredient_btn = tk.Button(self.ingredientFrame, text="Remove", font=("Helvetica", 12))
        self.remove_ingredient_btn.grid(row=4, column=2, padx=10, pady=10, sticky="e")
                """
                
import tkinter as tk
# Example of how handling of ingredients will be done
class RecipeGUI:
    def __init__(self, master):
        self.master = master
        self.ingredients = []

        # create the listbox and add it to the main frame
        self.ingredients_listbox = tk.Listbox(self.master, height=10, width=50)
        self.ingredients_listbox.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        # create a scrollbar for the listbox and add it to the main frame
        self.ingredients_scrollbar = tk.Scrollbar(self.master)
        self.ingredients_scrollbar.grid(row=4, column=2, sticky="NS", pady=10)
        self.ingredients_listbox.config(yscrollcommand=self.ingredients_scrollbar.set)
        self.ingredients_scrollbar.config(command=self.ingredients_listbox.yview)

        # create a button to add an ingredient to the listbox
        self.add_ingredient_btn = tk.Button(self.master, text="Add Ingredient", command=self.add_ingredient)
        self.add_ingredient_btn.grid(row=5, column=0, pady=10)

        # create a button to remove an ingredient from the listbox
        self.remove_ingredient_btn = tk.Button(self.master, text="Remove Ingredient", command=self.remove_ingredient)
        self.remove_ingredient_btn.grid(row=5, column=1, pady=10)

    def add_ingredient(self):
        # open a new window to add a new ingredient to the recipe
        ingredient_window = tk.Toplevel(self.master)

        # create labels and entry fields for the ingredient data
        ingredient_name_label = tk.Label(ingredient_window, text="Ingredient Name")
        ingredient_name_label.grid(row=0, column=0, padx=10, pady=10)
        ingredient_name_entry = tk.Entry(ingredient_window)
        ingredient_name_entry.grid(row=0, column=1, padx=10, pady=10)

        ingredient_quantity_label = tk.Label(ingredient_window, text="Ingredient Quantity")
        ingredient_quantity_label.grid(row=1, column=0, padx=10, pady=10)
        ingredient_quantity_entry = tk.Entry(ingredient_window)
        ingredient_quantity_entry.grid(row=1, column=1, padx=10, pady=10)

        # create a button to add the new ingredient to the listbox and close the window
        add_ingredient_button = tk.Button(ingredient_window, text="Add Ingredient", command=lambda: self.insert_ingredient(ingredient_name_entry.get(), ingredient_quantity_entry.get(), ingredient_window))
        add_ingredient_button.grid(row=2, column=0, columnspan=2, pady=10)

    def insert_ingredient(self, name, quantity, window):
        # add the new ingredient to the list of ingredients and to the listbox
        self.ingredients.append((name, quantity))
        self.ingredients_listbox.insert(tk.END, f"{name} - {quantity}")
        window.destroy()

    def remove_ingredient(self):
        # remove the selected ingredient from the list of ingredients and from the listbox
        selected_ingredient = self.ingredients_listbox.curselection()
        if selected_ingredient:
            self.ingredients_listbox.delete(selected_ingredient)
            del self.ingredients[selected_ingredient[0]]

root = tk.Tk()
app = RecipeGUI(root)
root.mainloop()