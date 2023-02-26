from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash

db = 'commissions_schema'

class Template:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.medium = data['medium']
        self.canvas = data['canvas']
        self.size = data['size']
        self.subject = data['subject']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Create
        @classmethod
        def insert_template(cls, data):
            query = "INSERT INTO templates (name, medium, canvas, size, subject) VALUES (%(name)s, %(medium)s, %(canvas)s, %(size)s, %(subject)s)"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        #Read 
        @classmethod
        def get_template(cls, data):
            query = "SELECT * FROM templates WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        @classmethod
        def get_all_templates(cls):
            query = "SELECT * FROM templates"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Update
        @classmethod
        def update_template(cls, data):
            query = "UPDATE templates SET name=%(name)s, medium=%(medium)s, canvas=%(canvas)s, size=%(size)s, subject=%(subject)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Delete
        @classmethod
        def delete_template(cls, data):
            query = "DELETE from templates WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results