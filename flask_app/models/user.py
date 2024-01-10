from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class User:
    db = "giftsync_db"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users ( name, email, created_at ) VALUES ( %(name)s , %(email)s, NOW() );"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.db).query_db(query)
    
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": data}
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {"email": data}
        result = connectToMySQL(cls.db).query_db(query, data)
        return result


    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": data}
        return connectToMySQL(cls.db).query_db(query, data)
    
