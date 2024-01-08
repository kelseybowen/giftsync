from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

class Gift:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.link = data['link']
        self.quantity = data['quantity']
        self.notes = data['notes']
        self.reserved = data['reserved']
        self.receiver_id = data['receiver_id']
        self.buyer_id = data['buyer_id']
        self.list_id = data['list_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']