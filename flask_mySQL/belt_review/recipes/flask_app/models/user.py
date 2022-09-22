
from flask_app import DATABASE, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.recipe import Recipe
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    @staticmethod
    def validate_user(user):
        is_valid = True
        # test whether a field matches the pattern
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.", 'first_name')
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.", 'last_name')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Please enter a valid email address.", 'email')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters in length.", 'password')
            is_valid = False
        #How can i check for capital letters lowercase letters a number... and a special character?
        if user['confirm'] != user['password']:
            flash("Passwords must match.", 'confirm')
            is_valid = False
        return is_valid

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        user = User(result[0])
        return user

    # ! AREN'T THESE TWO THINGS THE SAME THING...?
    @classmethod
    def get_one_for_check_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) > 0:
            return True
        else:
            return False

    @classmethod
    def get_one_with_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) < 1:
            return False
        else:
            user = User(result[0])
        return user
    # ! HELLO, THESE TWO THINGS... SAME THING...
    
    @classmethod
    def get_all_with_recipes(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        for result in results:
            recipe_copy = {
                'id' : result['recipes.id'],
                'name' : result['name'],
                'description' : result['description'],
                'instructions' : result['instructions'],
                'date_made' : result['date_made'],
                'under_30' : result['under_30'],
                'created_at' : result['recipes.created_at'],
                'updated_at' : result['recipes.updated_at'],
                'user_id' : result['user_id']
            }
            user.recipes.append(Recipe(recipe_copy))
        return user

    @classmethod
    def get_one_with_recipes(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        for result in results:
            recipe_copy = {
                'id' : result['recipe.id'],
                'name' : result['name'],
                'description' : result['description'],
                'instructions' : result['instructions'],
                'date_cooked' : result['date_cooked'],
                'under_30' : result['under_30'],
                'created_at' : result['recipe.created_at'],
                'updated_at' : result['recipe.updated_at'],
                'user_id' : result['user_id']
            }
            user.recipes.append(Recipe(recipe_copy))
        return user