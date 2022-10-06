from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "table_name"


class Model:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        return

    # Get all info from table

     @classmethod
    def get_all(cls):
        query = "SELECT * FROM table_name"
        table_from_db = connectToMySQL(DATABASE).query_db(query)
        all_data = []
        for each_dict in table_from_db:
            dict_instance = cls(each_dict)
            all_data.append(dict_instance)
        return all_data

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return cls(results[0])
        return False

    # Add info to table
    @classmethod
    def create(cls, data):
        query = "INSERT INTO table_name (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

    #  Update info in table
    @classmethod
    def update(cls, data):
        query = "UPDATE table_name SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # Delete info from table

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM table_name WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

