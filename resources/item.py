""" this file has Item and ItemList classes
    in order to retrivong items from database
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='enter price'
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help='enter store_id that item belongs to'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'massage': 'item not found'}, 404


    def post(self, name):
        # cheking existness of item
        item = ItemModel.find_by_name(name)
        if item:
            return {'massage': f"An item with name {name} already exists"}

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"massage": "error ocurres when inserting data in db"},500
        return item.json(),201


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"massage": f" An item with name {name} was deleted seccessfully!"}
        return {"massage": f" imposible to delete item with name: {name}, due to it is not exist!"}
    def put(self, name):
        #data = request.get_json(silent=True)
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:# item exist so just update it
            item.price = data['price']
        else:# item not exist so create it
            item = ItemModel(name, **data)

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'item': [item.json() for item in ItemModel.query.all()] }
    #or you can use map: list(map(lambda x: x.json, ItemModel.query.all()))
