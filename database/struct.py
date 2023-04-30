"""10/04/2023
Kingsley U.
CS50 AP
Master Project- Cookbook/Recipebook"""

import os,sys
import mysql.connector

class DataStructure():
    
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
    def add_recipe(self, name, description, instructions, category_id):
        """It takes the arguments and runs a mysql query to insert into the 'recipes' table
        
        Returns:
            int: Should return 0 if runs succesfully.
        """
        try:
            insert_recipe_query = "INSERT INTO recipes (name, description, instructions, category_id) VALUES (%s, %s, %s, %s)"
            recipe_values = (name, description, instructions, category_id)
            self.cursor.execute(insert_recipe_query, recipe_values)
            self.conn.commit()
            recipe_id = self.cursor.lastrowid

            return recipe_id
        except mysql.connector.Error as error:
            print("Failed to insert record into recipes table: {}".format(error))
#READ
    def get_recipe(self, recipe_id):
        try:
            select_recipe_query = "SELECT * FROM recipes WHERE id=%s"
            self.cursor.execute(select_recipe_query, (recipe_id,))
            recipe = self.cursor.fetchone()
            if recipe:
                return recipe
            else:
                print("No recipe found with id = {}".format(recipe_id))
        except mysql.connector.Error as error:
            print("Failed to retrieve record from recipes table: {}".format(error))
#UPDATE
    def update_recipe(self, recipe_id, name, description, instructions, category_id):
        try:
            sql = f"UPDATE recipes SET name = '{name}', description = '{description}', instructions = '{instructions}', category_id = {category_id} WHERE id = {recipe_id};"
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print("Failed to update recipe")
#DELETE
    def delete_recipe(self, recipe_id):
        try:
            sql = f"DELETE FROM recipes WHERE id = {recipe_id};"
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except:
            print("Failed to delete recipe")
            return 1

# Ingredient CRUD methods
    def add_ingredient(self, name, unit):
        try:
            insert_ingredient_query = "INSERT INTO ingredients (name, unit) VALUES (%s, %s)"
            ingredient_values = (name, unit)
            self.cursor.execute(insert_ingredient_query, ingredient_values)
            self.conn.commit()
            ingredient_id = self.cursor.lastrowid()

            return ingredient_id
        except mysql.connector.Error as error:
            print("Failed to insert record into ingredients table: {}".format(error))

    def get_ingredient(self, ingredient_id):
        try:
            select_ingredient_query = "SELECT * FROM ingredients WHERE id=%s"
            self.cursor.execute(select_ingredient_query, (ingredient_id,))
            ingredient = self.cursor.fetchone()
            if ingredient:
                return ingredient
            else:
                print("No ingredient found with id = {}".format(ingredient_id))
        except mysql.connector.Error as error:
            print("Failed to retrieve record from ingredients table: {}".format(error))
             
    def update_ingredient(self, ingredient_id, name, unit):
        try:
            sql = f"UPDATE ingredients SET name ='{name}', unit='{unit}', WHERE id = {ingredient_id}"
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except:
            print("Fialed to delete recipe")
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
        
    def __init__(self) -> None:
        self.connected = False
        
        