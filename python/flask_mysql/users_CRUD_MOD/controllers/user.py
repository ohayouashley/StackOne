# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
db = 'users_schema'
# model the class after the friend table from our database
class User: #!capital letters identify classes - file typically matches the class name lowercase.
    def __init__( self , data ): #! initialization/constructor method | data comes from data base
        self.id = data['id'] #! should have 1 - 1 (match database)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
#? Class = record data of user. 2. CRUD (below) - this is why should be broken up into separate classes. (SIDEBAR)
        # Now we use class methods to query our database
    @classmethod #!gives us access to the cls in get_all method. | cls like self allows ###methods - not classes.
    def get_all(cls): #! needs to have cls with @classmethod | direct reference to User
        query = "SELECT * FROM users;" #!will always return a list if it works
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(db).query_db(query)#!if you can't connect to your database your name may be wrong.
        # Create an empty list to append our instances of friends
        users = []
# Iterate over the db results and create instances of friends with cls.

        for row in results: #!represents a row of data
            users.append( cls(row) ) #cls invoking instance of a class
        return users

    @classmethod #!needs a class method because you're calling the class User
    def save(cls, data): #! want this to be a global method for all users, not individuals
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"

        id = connectToMySQL(db).query_db(query, data) #!when you have a %()s you need data argument
        return id

        #?asking for new person what info do I want to save on them