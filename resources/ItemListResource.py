import sqlite3
from flask_restful import Resource
from models.item import ItemModel

class ItemListResource(Resource):
    def get(self):
        return {
            'items': [item.json() for item in ItemModel.query.all()]
            #'items': list(map(lambda x: x.json(), ItemModel.query.all()))
        }, 200


        # return {
        #     'items': items
        # }
