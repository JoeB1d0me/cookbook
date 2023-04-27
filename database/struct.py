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
        query = "INSERT INTO recipes (name, description, instructions, category_id) VALUES (%s, %s, %s, %s)"
        values = (name, description, instructions, category_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_recipe_by_id(self, recipe_id):
        query = "SELECT * FROM recipes WHERE id = %s"
        values = (recipe_id,)
        self.cursor.execute(query, values)
        recipe = self.cursor.fetchone()
        if recipe:
            recipe_id, name, description, instructions, category_id = recipe
            category = self.get_category_by_id(category_id)
            recipe_ingredients = self.get_recipe_ingredients(recipe_id)
            ingredients = []
            for recipe_ingredient in recipe_ingredients:
                ingredient_id, quantity = recipe_ingredient[1:]
                ingredient = self.get_ingredient_by_id(ingredient_id)
                ingredients.append((ingredient, quantity))
            return {
                "id": recipe_id,
                "name": name,
                "description": description,
                "instructions": instructions,
                "category": category,
                "ingredients": ingredients
            }
        else:
            return None

    def get_all_recipes(self):
        query = "SELECT * FROM recipes"
        self.cursor.execute(query)
        recipes = self.cursor.fetchall()
        all_recipes = []
        for recipe in recipes:
            recipe_id, name, description, instructions, category_id = recipe
            category = self.get_category_by_id(category_id)
            recipe_ingredients = self.get_recipe_ingredients(recipe_id)
            ingredients = []
            for recipe_ingredient in recipe_ingredients:
                ingredient_id, quantity = recipe_ingredient[1:]
                ingredient = self.get_ingredient_by_id(ingredient_id)
                ingredients.append((ingredient, quantity))
            all_recipes.append({
                "id": recipe_id,
                "name": name,
                "description": description,
                "instructions": instructions,
                "category": category,
                "ingredients": ingredients
            })
        return all_recipes

    def add_ingredient(self, name, unit):
        query = "INSERT INTO ingredients (name, unit) VALUES (%s, %s)"
        values = (name, unit)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_ingredient_by_id(self, ingredient_id):
        query = "SELECT * FROM ingredients WHERE id = %s"
        values = (ingredient_id,)
        self.cursor.execute(query, values)
        ingredient = self.cursor.fetchone()
        if ingredient:
            ingredient_id, name, unit = ingredient
            return {
                "id": ingredient_id,
                "name": name,
                "unit": unit
            }
        else:
            return None

    def get_all_ingredients(self):
            query = "SELECT * FROM ingredients"
            self.cursor.execute(query)
            ingredients = self.cursor.fetchall()
            all_ingredients = []
            for ingredient in ingredients:
                ingredient_id, name, unit = ingredient
                all_ingredients.append({
                    "id": ingredient_id,
                    "name": name,
                    "unit": unit
                })
            return all_ingredients

    def add_recipe_ingredient(self, recipe_id, ingredient_id, quantity):
        query = "INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)"
        values = (recipe_id, ingredient_id, quantity)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_recipe_ingredients(self, recipe_id):
        query = "SELECT * FROM recipe_ingredients WHERE recipe_id = %s"
        values = (recipe_id,)
        self.cursor.execute(query, values)
        recipe_ingredients = self.cursor.fetchall()
        return recipe_ingredients

    def add_category(self, name):
        query = "INSERT INTO categories (name) VALUES (%s)"
        values = (name,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_category_by_id(self, category_id):
        query = "SELECT * FROM categories WHERE id = %s"
        values = (category_id,)
        self.cursor.execute(query, values)
        category = self.cursor.fetchone()
        if category:
            category_id, name = category
            return {
                "id": category_id,
                "name": name
            }
        else:
            return None

    def get_all_categories(self):
        query = "SELECT * FROM categories"
        self.cursor.execute(query)
        categories = self.cursor.fetchall()
        all_categories = []
        for category in categories:
            category_id, name = category
            all_categories.append({
                "id": category_id,
                "name": name
            })
        return all_categories
        
        
    def __init__(self) -> None:
        self.connected = False
        self.recipe = []
        self.ingredient_records = []
        self.categories = []
        
        self.recipe_placeholder = ["", "", "", 0]
        self.recipe_updater = [0, "", "", "", 0]
        
        self.ingredient_placeholder = ["", ""]
        self.ingredient_updater = [0, "", ""]
        
        
        