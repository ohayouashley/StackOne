from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user 
from pprint import pprint

class Recipe:
    db = "recipes"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under30 = data['under30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None 
#data side should always watch your database
    @classmethod
    def create(cls,data): #? only use data if using %()s
        query = "INSERT INTO recipes (name, description, instructions, date, under30, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date)s,%(under30)s,%(user_id)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name =%(name)s, description =%(description)s, instructions=%(instructions)s,date=%(date)s,under30=%(under30)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)



    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            pprint(row,sort_dicts=False,width=1)
            this_recipe = (cls(row))
            user_dict = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }    
            this_recipe.creator = user.User(user_dict)
            recipes.append(this_recipe)
        return recipes

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1 : 
            return False
        row = results[0]
        recipe = cls(row)
        user_dict = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }    
        this_user = user.User(user_dict)
        recipe.user = this_user 
        return recipe

        

    @staticmethod
    def validate_recipe(recipe_data):
        is_valid = True
        if len(recipe_data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(recipe_data['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(recipe_data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        if recipe_data['date'] == '':
            flash("Must input date")
            is_valid = False
        if "under30" not in recipe_data: 
            flash("Must select yes or no")
            is_valid = False 
        return is_valid
        
        #check length of each of your fields - if len of descript less than 