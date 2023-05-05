"""10/04/2023
Kingsley U.
CS50 AP
Master Project- Cookbook/Recipebook"""

import os,sys
import mysql.connector
import traceback

class DataStructure():
    def __init__(self):
        self.ingredients = []
        self.recipes = []
        
        self.addRecipe = ["","","",""]
        self.updateRecipe = [0,"","","",""]
        
        self.addIngredient = ["",0.0,""]
        self.updateIngredient = [0,"",0.0,""]
        
        
        self.addRecipeIngredient = [0,0]
        
        
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
            insert_recipe_query = f"INSERT INTO recipes (name, description, instructions, category) VALUES ('{self.addRecipe[0]}','{self.addRecipe[1]}','{self.addRecipe[2]}', '{self.addRecipe[3]}')"
            self.cursor.execute(insert_recipe_query)
            self.conn.commit()
            self.get_recipe()
            return 0
        except mysql.connector.Error as error:
            print("Failed to insert record into recipes table: {}".format(error))
            print(traceback.format_exc())
            return 1
#READ
    def get_recipe(self):
        try:
            select_recipe_query = "SELECT * FROM recipes ORDER BY name"
            self.cursor.execute(select_recipe_query)
            self.recipes = self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to retrieve record from recipes table: {}".format(error))
            print(traceback.format_exc())
#UPDATE
    def update_recipe(self):
        try:
            sql = f"UPDATE recipes SET name ='{self.updateRecipe[1]}', description='{self.updateRecipe[2]}', instructions='{self.updateRecipe[3]}', category='{self.updateRecipe[4]}' WHERE id = {self.updateRecipe[0]}"
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print("Failed to update recipe")
            print(traceback.format_exc())
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
            insert_ingredient_query = f"INSERT INTO ingredients (name, quantity, unit) VALUES ('{self.addIngredient[0]}',{self.addIngredient[1]},'{self.addIngredient[2]}')"
            self.cursor.execute(insert_ingredient_query)
            self.conn.commit()
            self.get_ingredient()
            
        except mysql.connector.Error as error:
            print("Failed to insert record into ingredients table: {}".format(error))
            print(traceback.format_exc())

    def get_ingredient(self):
        try:
            select_ingredient_query = "SELECT * FROM ingredients ORDER BY name"
            self.cursor.execute(select_ingredient_query)
            self.ingredients = self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to retrieve record from ingredients table: {}".format(error))
             
    def update_ingredient(self):
        try:
            sql = f"UPDATE ingredients SET name ='{self.update_ingredient[1]}',quantity={str(self.update_ingredient[2])} , unit='{self.update_ingredient[3]}', WHERE id = {self.update_ingredient[0]}"
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except:
            print("Failed to delete recipe")
            return 1

 # delete ingredient
    def delete_ingredient(self, name):
        try:
            sql = f"DELETE FROM ingredients WHERE name = '{name}';"
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print("Failed to delete recipe")
            return 1

# Recipe_Ingredient CRUD methods
    #Create method for the intermediate table
    def add_recipe_ingredient(self):
        try:
            insert_recipe_ingredient_query = "INSERT INTO recipe_ingredients (recipe_id, ingredient_id) VALUES (%s, %s)"
            recipe_ingredient_values = (self.addRecipeIngredient[0], self.addRecipeIngredient[1])
            self.cursor.execute(insert_recipe_ingredient_query, recipe_ingredient_values)
            self.conn.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into recipe_ingredients table: {}".format(error))
            
    #Gets the recipe information and the ingredients for that recipe from the intermediate table        
    def get_all_recipe_ingredients(self, recipe_id):
        try:
            query =f"""SELECT ingredients.name, ingredients.quantity, ingredients.unit
                    FROM recipe_ingredients
                    JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.id
                    WHERE recipe_ingredients.recipe_id = {recipe_id}"""
            self.cursor.execute(query)
            self.ingredients = self.cursor.fetchall()

        except mysql.connector.Error as error:
            print("Failed to retrieve record from recipe_ingredients table: {}".format(error))
