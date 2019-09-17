from flask import jsonify
from flask_restful import Resource, reqparse, request
from flask_jwt import JWT, jwt_required
from models.item import ItemModel

class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left black!")

    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'Item not Found'}, 404

    def post (self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': f'An item with name {name} already exists'}, 400 #bad request

        data = request.get_json()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except Exception as e:
            return {
                'message': f'Error ocurrend inserting item {e}'
            }

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return { 'message': 'Item deleted' }

    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = ['price']

        item.save_to_db()

        return item.json()
