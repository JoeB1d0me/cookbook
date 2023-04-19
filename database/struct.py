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
        
    def load_recipe(self):
        try:
            query = ("""SELECT recipes.id, recipes.name, 
                     recipes.description, recipes.instructions, recipes.category_id, 
                     recipe_ingredients.quantity,
                     ingredients.unit, ingredients.name, categories.name
                     FROM recipes
                     INNER JOIN """)
        except mysql.connector.Error:
            return 2
    
        
        
        
        
        
    def __init__(self) -> None:
        self.connected = False
        self.recipe = []
        self.ingredient_records = []
        self.categories = []
        
        self.recipe_placeholder = ["", "", "", 0]
        self.recipe_updater = [0, "", "", "", 0]
        
        self.ingredient_placeholder = ["", ""]
        self.ingredient_updater = [0, "", ""]
        
        
        