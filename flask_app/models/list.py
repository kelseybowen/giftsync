from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

class List:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.owner_id = data['owner_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

