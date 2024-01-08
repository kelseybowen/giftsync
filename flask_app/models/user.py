from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
# from flask_bcrypt import Bcrypt
# import re

# bcrypt = Bcrypt(app)
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PASSWORD_REGEX = re.compile(r'^(?=.*[0-9]$)(?=.*[a-zA-Z])')

class User:
    db = "giftsync_db"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # @classmethod
    # def create_ninja(cls, data):
    #     query = "INSERT INTO ninjas ( first_name, last_name, age, created_at, dojo_id ) VALUES ( %(first_name)s , %(last_name)s , %(age)s, NOW(), %(dojo_id)s );"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)