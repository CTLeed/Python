from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas_schema"


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        return

    # Get all info from table

     @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        ninjas_from_db = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for each_ninja in ninjas_from_db:
            ninja_instance = cls(each_ninja)
            all_ninjas.append(ninja_instance)
        return all_ninjas

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return cls(results[0])
        return False

    # Add info to table
    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    #  Update info in table
    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # Delete info from table

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninja WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

