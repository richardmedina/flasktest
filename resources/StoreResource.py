from flask_restful import Resource
from models.store import StoreModel

class StoreResource(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {
            'message': 'Store not found'
        }, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {
                'message': f'A store with name {name} already exists'
            }
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {
                'message': 'An error ocurred while creating the store'
            }, 500

        return store.json(), 201

    def delete(self, name):
        if StoreModel.find_by_name(name):
            store.delete_from_db()

        return {
            'message': 'Store deleted'
        }

class StoreListResource(Resource):
    def get(self):
        return [store.json() for store in StoreModel.query.all ()]
