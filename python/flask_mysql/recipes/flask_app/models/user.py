from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile((r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'))
from flask import flash

class User:
    db = "recipes" #!
    def __init__(self,data): #!attributes
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM users;
        """
        results = connectToMySQL(cls.db).query_db(query) #!you need to tell connectToMySQL function what database to connect to. 
        #!(database vs tabl - you can have multiple tables in a database) 
        users = [] #!storing instances of user class - pull out of t he results
        for row in results:
            users.append( cls(row))#!intializing a new user for the db
        return users #!returning list of users.

    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user

    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        row = results[0]
        user = cls(row)
        return user


    @classmethod
    def create (cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_register(form_data): #?form data - being passed through here.
        is_valid = True # we assume this is true
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(User.db).query_db(query,{'email':form_data['email']})
        #!(User.db) - 
        if len(form_data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(form_data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if form_data['email'] == '': 
            flash("Email cannot be blank!") #? can also be used for password. ['password']
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        elif results:
            flash("This email address has already been used!!")
            is_valid = False
        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if form_data['password'] != form_data['confirm']:
            flash("Password does not match!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        user_in_db = User.get_user_by_email(user)
        if not user_in_db:
            flash('Email is not associated with an account')
            is_valid = False
        if not EMAILREGEX.match(user['email']):
                flash('Invalid email address!')
                is_valid = False
        if len(user['password']) < 8:
            flash('Password must be at least 8 characters', 'error')
            is_valid = False
        return is_valid
# @classmethod
# def 


# template.py - controller






# from login_registration.config.mysqlconnection import connectToMySQL, re 
# # singular.py

# # create a regular expression object that we'll use later   
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# class User:
#     @staticmethod
#     def validate_user( user ):
#         is_valid = True
#         # test whether a field matches the pattern
#         if not EMAIL_REGEX.match(user['email']): 
#             flash("Invalid email address!")
#             is_valid = False
#         return is_valid

#         ####

# class Singular:
#     def __init__(self,data):
#         self.id = data['id']
#         self.name = data['name']
#         self.email = data['email']
#         self.password = data['password']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

# #singular.py...
# # gets all the burgers and returns them in a list of burger objects .
# @classmethod
# def get_all(cls):
# 	query = "SELECT * FROM plurals"
# 	plurals_from_db = connectToMySQL('plurals').query_db(query)
# 	plurals = []
# 	for b in plurals_from_db:
# 		plurals.append(cls(b))
# 	return plurals

# # burger.py...
# # gets all the burgers and returns them in a list of burger objects .
# @classmethod
# def save(cls,data):
# 	query = "Insert INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW());"
# 	burger_id = connectToMySQL('burgers').query_db(query,data)
# 	return burger_id

#validate
# @static method 
# def validate_user( user ):
#     is_vaid = True
#     if len(us