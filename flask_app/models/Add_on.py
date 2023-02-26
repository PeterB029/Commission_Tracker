from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash

db = 'commissions_schema'

class Add_on:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.additional_cost = data['additional_cost']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Create
        @classmethod
        def insert_add_on(cls, data):
            query = "INSERT INTO add_ons (name, additional_cost, template_id) VALUES (%(name)s, %(additional_cost)s, %(template_id)s)"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        #Read
        @classmethod
        def get_template_add_ons(cls, data):
            query = "SELECT * FROM add_ons WHERE template_id=%(template_id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Update
        @classmethod
        def update_add_on(cls, data):
            query = "UPDATE add_ons SET name=%(name)s, additional_cost=%(additiona_cost)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Delete
        @classmethod
        def delete_add_on(cls, data):
            query = "DELETE from add_ons WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results