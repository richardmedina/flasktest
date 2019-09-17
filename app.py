import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

from resources.UserListResource import UserListResource
from resources.UserResource import UserResource
from resources.ItemListResource import ItemListResource
from resources.ItemResource import ItemResource
from resources.StoreResource import StoreResource, StoreListResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'Jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(StoreListResource, '/stores')
api.add_resource(StoreResource, '/store/<string:name>')

api.add_resource(ItemListResource, '/items')
api.add_resource(ItemResource, '/item/<string:name>')

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/user')

print(f'{__name__}')
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run (port=5000, debug=True)
