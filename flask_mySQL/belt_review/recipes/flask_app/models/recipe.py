
from flask_app import DATABASE, flash, session
from flask_app.config.mysqlconnection import connectToMySQL

# some of these classmethods might not be used

class Recipe:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        # test whether a field matches the pattern
        if len(recipe['name']) < 1 or len(recipe['description']) < 1 or len(recipe['instructions']) < 1 or recipe['date_made'] != '' or 'under_30' not in recipe:
            flash("All fields are requied.")
            is_valid = False
        return is_valid

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_30, user_id) VALUES (%(name)s , %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for recipe in results:
            all_recipes.append(cls(recipe))
        return all_recipes

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        recipe_id = connectToMySQL(DATABASE).query_db(query, data)
        return recipe_id

    @classmethod
    def get_one_with_recipes(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return Recipe(results[0])