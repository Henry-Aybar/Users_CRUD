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

        # Create an empty list to append our instances of friends
        users = []

        # Iterate over the db results and create instances of friends with cls.
        for single_obj in results:
            users.append( cls(single_obj) )
        return users

    @classmethod
    def save_user(cld, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL('users_schema').query_db(query, data)
        return results