from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session, request

class List:
    db = "giftsync_db"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.owner_id = data['owner_id']
        self.is_public = data['is_public']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_list(cls, data):
        query = "INSERT INTO lists ( name, description, owner_id, created_at ) VALUES ( %(name)s , %(description)s , %(owner_id)s, NOW() );"
        new_data = {
            "name": data["name"],
            "description": data["description"],
            "is_public": data["is_public"],
            "owner_id": session["user"][0]["id"]
            }
        result = connectToMySQL(cls.db).query_db(query, new_data)
        print(result)
        return result
    
    @classmethod
    def get_all_lists(cls, data):
        query = "SELECT * FROM lists WHERE owner_id=%(user_id)s;"
        data = {"user_id": session["user"][0]["id"]}
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_list_by_id(cls, data):
        query = "SELECT * FROM lists WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_lists_by_owner_id(cls, data):
        query = "SELECT * FROM lists WHERE owner_id = %(owner_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)


    
    @classmethod
    def update_list(cls, data):
        query = "UPDATE lists SET name=%(name)s, description=%(description)s, is_public=%(is_public)s, updated_at=NOW() WHERE id=%(list_id)s;"
        data = {
            "name": request.form["list_name"],
            "description": request.form["description"],
            "is_public": request.form["is_public"]
            }
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_list(cls, data):
        query = "DELETE lists WHERE id=%(id)s;"
        # data = {"id": data["id"]}
        return connectToMySQL(cls.db).query_db(query, data)




