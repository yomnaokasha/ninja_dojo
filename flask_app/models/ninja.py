from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        print(data)
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def find_for_dojo(cls, dojo_id):
    #     query = "select * from ninjas where dojo_id = %(dojo_id)s;"
    #     data = {
    #         "dojo_id": dojo_id
    #     }
    #     results = connectToMySQL('dojod_ninjas').query_db(query, data)
    #     ninjas = []
    #     for row in results:
    #         ninjas.append(Ninja(row))
    #     return ninjas

    @classmethod
    def add(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        connectToMySQL('dojod_ninjas').query_db(query, data)
