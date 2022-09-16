
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        return dojo

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_one_w_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        for result in results:
            ninja_clone = {
                'id' : result['ninjas.id'],
                'first_name' : result['first_name'],
                'last_name' : result['last_name'],
                'age' : result['age'],
                'created_at' : result['ninjas.created_at'],
                'updated_at' : result['ninjas.updated_at'],
                'dojo_id' : result['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_clone))
        return dojo