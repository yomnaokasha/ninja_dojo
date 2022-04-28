from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        self.ninja = []

    @classmethod
    def get_all(cls):
        query = "select * from dojos;"
        results = connectToMySQL('dojod_ninjas').query_db(query)
        dojos = []
        for row in results:
            dojos.append(Dojo(row))
        return dojos

    @classmethod
    def add(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojod_ninjas').query_db(query, data)
        return result

    # @classmethod
    # def get_one(cls, dojo_id):
    #     query = "select * from dojos where id = %(id)s;"
    #     data = {
    #         "id": dojo_id,
    #     }
    #     result = connectToMySQL('dojod_ninjas').query_db(query, data)
    #     return (Dojo(result[0]))

    @classmethod
    def get_one_with_ninja(cls, data):
        query = "select * from dojos left joins ninjas on dojos.id = ninjas.dojo_id where dojos.id = %(id)s;"
        result = connectToMySQL('dojod_ninjas').query_db(query, data)
        this_dojo = cls(result[0])
        for row in result:
            ninja_info = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
        this_dojo.ninja.append(Ninja(ninja_info))

        return this_dojo
