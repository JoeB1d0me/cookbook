"""10/04/2023
Kingsley U.
CS50 AP
Master Project- Cookbook/Recipebook"""

import os,sys
import mysql.connector

class DataStructure():
    def __init__(self):
        self.ingredients = []
        self.recipes = []
        
        self.addRecipe = ["","","",0]
        self.updateRecipe = [0,"","","",0]
        
        self.addIngredient = ["",""]
        self.updateIngredient = [0,"",""]
        
        self.addCategory = [""]
        self.updateCategory = [0,""]
        
        self.addRecipeIngredient = [0,0,0]
        
        
        self.connected = False
        
            
    def connect(self,host,port,user,password,database):
        """Creates a connection object to the database"""
        try:
            self.conn = mysql.connector.connect(
                host = host,
                port = port,
                user = user,
                password = password,
                database = database   
            )
            self.cursor = self.conn.cursor()
            self.connected = True
        except mysql.connector.Error:
            print("Error with connection")
            return 1
        print("Connection worked")
        return 0
    
    def disconnect(self):
        """Closes the mysql connection
        """
        if(self.connected):
            try:
                self.conn.close()
                self.connected = False
            except mysql.connector.Error:
                print("Disconnect failed")
                return 1
            print("Discconnect success")
            return 0
        
# Recipe CRUD methods
#CREATE
    def add_recipe(self):
        """It takes the arguments and runs a mysql query to insert into the 'recipes' table
        
        Returns:
            int: Should return 0 if runs succesfully.
        """
        try:
            insert_recipe_query = "INSERT INTO recipes (name, description, instructions, category_id) VALUES (%s, %s, %s, %s)"
            recipe_values = (self.addRecipe[0], self.addRecipe[1], self.addRecipe[2], self.addRecipe[3])
            self.cursor.execute(insert_recipe_query, recipe_values)
            self.conn.commit()
            recipe_id = self.cursor.lastrowid

            return recipe_id
        except mysql.connector.Error as error:
            print("Failed to insert record into recipes table: {}".format(error))
#READ
    def get_recipe(self):
        try:
            select_recipe_query = "SELECT * FROM recipes ORDER BY name"
            self.cursor.execute(select_recipe_query)
            self.recipes = self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to retrieve record from recipes table: {}".format(error))
#UPDATE
    def update_recipe(self):
        try:
            sql = f"UPDATE recipes SET name ='{self.updateRecipe[1]}', description='{self.updateRecipe[2]}', instructions='{self.updateRecipe[3]}', category_id={self.updateRecipe[4]} WHERE id = {self.updateRecipe[0]}"
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print("Failed to update recipe")
#DELETE
    def delete_recipe(self, recipe_id):
        try:
            sql = f"DELETE FROM recipes WHERE id = {str(recipe_id)};"
            self.cursor.execute(sql)
            self.conn.commit()
            self.get_recipe()
            return 0
        except:
            print("Failed to delete recipe")
            return 1

# Ingredient CRUD methods
    def add_ingredient(self):
        try:
            insert_ingredient_query = "INSERT INTO ingredients (name, unit) VALUES (%s, %s)"
            ingredient_values = (self.addIngredient[0], self.addIngredient[1])
            self.cursor.execute(insert_ingredient_query, ingredient_values)
            self.conn.commit()
            ingredient_id = self.cursor.lastrowid()

            return ingredient_id
        except mysql.connector.Error as error:
            print("Failed to insert record into ingredients table: {}".format(error))

    def get_ingredient(self):
        try:
            select_ingredient_query = "SELECT * FROM ingredients ORDER BY name"
            self.cursor.execute(select_ingredient_query)
            self.ingredients = self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to retrieve record from ingredients table: {}".format(error))
             
    def update_ingredient(self):
        try:
            sql = f"UPDATE ingredients SET name ='{self.update_ingredient[1]}', unit='{self.update_ingredient[2]}', WHERE id = {self.update_ingredient[0]}"
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except:
            print("Failed to delete recipe")
            return 1

 # delete ingredient
    def delete_ingredient(self, ingredient_id):
        try:
            sql = f"DELETE FROM ingredients WHERE id = {ingredient_id};"
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print("Failed to delete recipe")
            return 1

# Recipe_Ingredient CRUD methods
    #Create method for the intermediate table
    def add_recipe_ingredient(self, recipe_id, ingredient_id, quantity):
        try:
            insert_recipe_ingredient_query = "INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)"
            recipe_ingredient_values = (recipe_id, ingredient_id, quantity)
            self.cursor.execute(insert_recipe_ingredient_query, recipe_ingredient_values)
            self.conn.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into recipe_ingredients table: {}".format(error))
            
    #Gets recipe information using joins from the intermediate table        
    def get_recipe_ingredients(self, recipe_id):
        try:
            query =f"""SELECT ingredients.name, recipe_ingredients.quantity
                    FROM recipe_ingredients
                    JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.id
                    WHERE recipe_ingredients.recipe_id = {recipe_id}"""
            self.cursor.execute(query)
            self.ingredients = self.cursor.fetchall()

        except mysql.connector.Error as error:
            print("Failed to retrieve record from recipe_ingredients table: {}".format(error))

# Category CRUD methods

    def add_category(self, name):  
        try:
            insert_category_query = "INSERT INTO categories (name) VALUES (%s)"
            category_values = (name,)
            self.cursor.execute(insert_category_query, category_values)
            self.conn.commit()
            category_id = self.cursor.lastrowid

            return category_id
        except mysql.connector.Error as error:
            print("Failed to insert record into categories table: {}".format(error))
            
    def get_category(self, category_id):
        try:
            select_category_query = "SELECT * FROM categories WHERE id=%s"
            self.cursor.execute(select_category_query, (category_id,))
            category = self.cursor.fetchone()
            if category:
                return category
        
        except Exception as e:
            print(f"Error getting category with id {category_id}: {e}")
            return None
        
    def update_category(self, category_id, name):
        try:
            sql = f"UPDATE categories SET name = '{name}' WHERE id = {category_id};"
            self.cursor.execute(sql)
            self.connection.commit()
        except:
            print("Failed to update category")

    def delete_category(self, category_id):
        try:
            sql = f"DELETE FROM categories WHERE id = {category_id};"
            self.cursor.execute(sql)
            self.connection.commit()
        except:
            print("Failed to delete category")
        
