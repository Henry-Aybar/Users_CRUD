from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        # make sure to call the connectToMySQL function with the schema you are targeting.

        # Create an empty list to append our instances of users
        users = []

        # Iterate over the db results and create instances of users with cls.
        for single_obj in results:
            users.append( cls(single_obj) )
        return users

    @classmethod
    def save_user(cld, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL('users_schema').query_db(query, data)
        return results

    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"

        results = connectToMySQL('users_schema').query_db(query, data)

        return cls( results[0] ) 

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"

        results = connectToMySQL('users_schema').query_db(query, data)
        return results

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        results = connectToMySQL('users_schema').query_db(query, data)
        return results