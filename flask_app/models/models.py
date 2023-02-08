from flask_app.config.mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #to verify is a proper gmail
from flask import flash  #for messages to display
import re 

#  connect other model if needed

class Sample:
    database = "name of schema goes here"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        

# create 
    @classmethod
    def save(cls,data):
        query = "INSERT INTO samples (name, create_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.database).query_db(query, data)

# retreive
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM samples;"
        results =  connectToMySQL(cls.database).query_db(query)
        all_samples = []
        for row in results:
            print(row)
            all_samples.append( cls(row) )
        return all_samples

# retrieve by one by id
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM samples WHERE id = %(id)s;"
        results = connectToMySQL(cls.database).query_db(query,data)
        return cls( results[0] )

# update colmn in table
    @classmethod
    def update(cls, data):
        query = "UPDATE samples SET name = %(name)s,  created_at = NOW(),updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.database).query_db(query,data)

# DELETE
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM samples WHERE id = %(id)s;"
        return connectToMySQL(cls.database).query_db(query,data)
    

# validaations 
    @staticmethod
    def validate_sample(sample):
        is_valid = True
        if len(sample['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","sample")
        return is_valid
