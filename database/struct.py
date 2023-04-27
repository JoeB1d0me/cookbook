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
    def add_recipe(self, name, description, instructions, category_id):
        try:
            insert_recipe_query = "INSERT INTO recipes (name, description, instructions, category_id) VALUES (%s, %s, %s, %s)"
            recipe_values = (name, description, instructions, category_id)
            self.cursor.execute(insert_recipe_query, recipe_values)
            self.connection.commit()
            recipe_id = self.cursor.lastrowid

            return recipe_id
        except mysql.connector.Error as error:
            print("Failed to insert record into recipes table: {}".format(error))

    def add_ingredient(self, name, unit):
        try:
            insert_ingredient_query = "INSERT INTO ingredients (name, unit) VALUES (%s, %s)"
            ingredient_values = (name, unit)
            self.cursor.execute(insert_ingredient_query, ingredient_values)
            self.connection.commit()
            ingredient_id = self.cursor.lastrowid

            return ingredient_id
        except mysql.connector.Error as error:
            print("Failed to insert record into ingredients table: {}".format(error))

    def add_recipe_ingredient(self, recipe_id, ingredient_id, quantity):
        try:
            insert_recipe_ingredient_query = "INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)"
            recipe_ingredient_values = (recipe_id, ingredient_id, quantity)
            self.cursor.execute(insert_recipe_ingredient_query, recipe_ingredient_values)
            self.connection.commit()
        except mysql.connector.Error as error:
            print("Failed to insert record into recipe_ingredients table: {}".format(error))

    def add_category(self, name):  
        try:
            insert_category_query = "INSERT INTO categories (name) VALUES (%s)"
            category_values = (name,)
            self.cursor.execute(insert_category_query, category_values)
            self.connection.commit()
            category_id = self.cursor.lastrowid

            return category_id
        except mysql.connector.Error as error:
            print("Failed to insert record into categories table: {}".format(error))

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
            
    def get_category(self, category_id):
        try:
            pass
        
        except Exception as e:
            print(f"Error getting category with id {category_id}: {e}")
            return None
        
        
    def __init__(self) -> None:
        self.connected = False
        self.recipe = []
        self.ingredient_records = []
        self.categories = []
        
        self.recipe_placeholder = ["", "", "", 0]
        self.recipe_updater = [0, "", "", "", 0]
        
        self.ingredient_placeholder = ["", ""]
        self.ingredient_updater = [0, "", ""]
        
        
        