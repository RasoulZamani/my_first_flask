from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'massage': f"A store {name} not founded!"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'massage': f"A store {name} is already exist!"},400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"massage": "An error occure in creating store."},500
        return store.json(),201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        else:
            return {'massage': f"A store {name} is not exist!"},400
        return {'massage': f" store {name} deleted successfully"}

class StoreList(Resource):
    def get(self):
        return {'store': [store.json() for store in StoreModel.find_all()] }
