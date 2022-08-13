#read- sql

@classmethod
def get_user_by_email(cls, email):
    data = {'email' : email}
    query = """
    SELECT *
    FROM users
    WHERE email = %(emails)s;
    """
    result = MySQLConnection(cls,db).query_db(query, data)
    if result: 
        result = cls(result[0])
    return result

# UPDATE user - SQL
# DELETE user SQL

#CREATE
@classmethod
def create_user(cls,data):
    if not cls.validate_user_reg_data(data): #!if doesn't match bad data then return false
        return False
    query = """
    INSERT INTO users (first-name, last_name, email, password)
    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
    """




#fist validate 1    


#login -registration
def validate_user_reg_data(data):
    EMAIL_REGEX = re.compile(r'^[a-zA-0.+_-')

@staticmethod
def parse_registration_data(data):
    parsed_data = {}
    parsed_data['email'] = data['email'].lower()
    