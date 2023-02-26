from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash

db = 'commissions_schema'

class Social_media:
    def __init__(self, data):
        self.id = data['id']
        self.platform = data['platform']
        self.user_handle = data['user_handle']
        self.follows = data['follows']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #Create
        @classmethod
        def insert_social_media(cls, data):
            query = "INSERT INTO social_medias (platform, user_handle, follows, client_id) VALUES (%(platform)s, %(user_handle)s, %(follows)s, %(client_id)s)"
            results = connectToMySQL(db).query_db(query, data)
            return results
        
        #Read 
        @classmethod
        def get_soical_media_by_client(cls, data):
            query = "SELECT * FROM social_medias WHERE client_id=%(client_id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Update
        @classmethod
        def update_social_media(cls, data):
            query = "UPDATE social_medias SET platform=%(platform)s, user_handle=%(user_handle)s, follows=%(follows)s"
            results = connectToMySQL(db).query_db(query, data)
            return results

        #Delete
        @classmethod
        def delete_social_media(cls, data):
            query = "DELETE from social_medias WHERE id=%(id)s"
            results = connectToMySQL(db).query_db(query, data)
            return results