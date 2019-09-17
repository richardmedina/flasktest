import sqlite3
from flask_restful import Resource

class UserListResource(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM users")
        users = []
        for row in result:
            users.append({
                'id': row[0],
                'username': row[1],
                'password': row[2]
            })
        return {
            'users': users
        }, 200
