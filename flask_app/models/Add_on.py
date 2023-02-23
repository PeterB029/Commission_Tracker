from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'commissions_schema'

class Add_on:
    def __init__(self, data):
        self.id = data['id']
        self.additional_cost = data['additional_cost']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        @classmethod
        def get_commission_add_ons(self, data):
            pass

        @classmethod
        def insert_add_on(self, data):
            pass

        