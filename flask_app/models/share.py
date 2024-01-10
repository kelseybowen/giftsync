from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session, request

class Share:
    def __init__(self, data):
        self.id = data["id"]
        self.viewer_id = data["viewer_id"]
        self.list_id = data["list_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_shares(cls):
        query = "SELECT * FROM shares;"
        return connectToMySQL(cls.db).query_db(query)
    
    @classmethod
    def get_one_share(cls, data):
        query = "SELECT * FROM shares WHERE viewer_id=%(viewer_id)s AND list_id=%(list_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def create_share(cls, data):
        query = "INSERT INTO shares (viewer_id, list_id, created_at) VALUES (%(viewer_id)s, %(list_id)s), NOW();"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_share(cls, data):
        query = "DELETE FROM shares WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)