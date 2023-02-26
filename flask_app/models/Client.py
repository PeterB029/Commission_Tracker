from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash

db = 'commissions_schema'

class Client:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone = data['phone']
        self.state = data['state']
        self.city = data['city']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Create
        @classmethod
        def insert_client(cls, data):
            query = "INSERT INTO clients (first_name, last_name, email, phone, state, city, address) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone)s, %(state)s, %(city)s, %(address)s)"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        #Read
        @classmethod
        def get_single_client(cls, data):
            query = "SELECT * FROM clients WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        @classmethod
        def get_all_clients(cls):
            query = "SELECT * FROM clients"
            results = connectToMySQL(db).query_db(query)
            return results

        #Update
        @classmethod
        def update_client(cls, data):
            query = "UPDATE clients SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, phone=%(phone)s, state=%(state)s, city=%(city)s, address=%(address)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Delete
        @classmethod
        def delete_client(cls, data):
            query = "DELETE from clients WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results