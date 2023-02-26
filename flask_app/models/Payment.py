from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash

db = 'commissions_schema'

class Payment:
    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']
        self.trade = data['trade']
        self.cost = data['cost']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Create
        @classmethod
        def insert_payment(cls, data):
            query = "INSERT INTO payments (type, trade, cost, status) VALUES (%(type)s, %(trade)s, %(cost)s, %(status)s)"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        #Read 
        @classmethod
        def get_payment(cls, data):
            query = "SELECT * FROM payments WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        @classmethod
        def get_all_payments(cls, data):
            query = "SELECT * FROM payments"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Update
        @classmethod
        def update_payment(cls, data):
            query = "UPDATE payments SET type=%(type)s, trade=%(trade)s, cost=%(cost)s, status=%(status)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Delete
        @classmethod
        def delete_payment(cls, data):
            query = "DELETE from payments WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results