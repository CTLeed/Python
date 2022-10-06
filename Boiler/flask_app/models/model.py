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
        query = "SELECT * FROM table"
        tables_from_db = connectToMySQL(DATABASE).query_db(query)
        tables = []
        for each_one in tables_from_db:
            table_instance = cls(each_one)
            tables.append(table_instance)
        return tables

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM table WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return cls(results[0])
        else:
            return False

    # Add info to table
    @classmethod
    def create(cls, data):
        query = "INSERT INTO table (name, ) VALUES (%(names)s, )"
        table_id = connectToMySQL(DATABASE).query_db(query, data)
        return table_id

    #  Update info in table
    @classmethod
    def update(cls, data):
        pass

    # Delete info from table
    @classmethod
    def delete(cls, data):
        pass
