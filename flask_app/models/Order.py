from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash

db = 'commissions_schema'

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.status = data['status']
        self.date_ordered = data['date_orderd']
        self.date_due = data['date_due']
        self.image1 = data['image1']
        self.image2 = data['image2']
        self.image3 = data['image3']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Create
        @classmethod
        def insert_order(cls, data):
            query = "INSERT INTO orders (name, status, date_ordered, date_due, image1, image2, image3, client_id, template_id, payment_id) VALUES (%(name)s, %(status)s, %(date_ordered)s, %(date_due)s, %(image1)s, %(image2)s, %(image3)s, %(client_id)s, %(template_id)s, %(payment_id)s)"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        #Read 
        @classmethod
        def get_order_by_client(cls, data):
            query = "SELECT * FROM orders WHERE client_id=%(client_id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        @classmethod
        def get_open_orders(cls, data):
            query = "SELECT * FROM orders WHERE status='Open' OR status='Ongoing' OR staus='Paused'"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        @classmethod
        def get_closed_orders(cls, data):
            query = "SELECT * FROM orders WHERE status='Ghosted' OR status='Delivered'"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Update
        @classmethod
        def update_order(cls, data):
            query = "UPDATE orders SET name=%(name)s, status=%(status)s, date_orderd=%(date_ordered)s, date_due=%(date_due)s, image1=%(image1)s, image2=%(image2)s, image3=%(image3)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Delete
        @classmethod
        def delete_order(cls, data):
            query = "DELETE from orders WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results