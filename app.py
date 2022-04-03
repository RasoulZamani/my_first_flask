from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList
print("hi, Im using flask-restful and SQLAlchemy!also it is secret by jwt!")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS']=True
app.secret_key = 'Flaskpass#'
api = Api(app)

''' it transformed to run.py due to deployment issue
@app.before_first_request
def create_tables():
    db.create_all()
'''
jwt = JWTManager(app)

#adding claim
#@jwt.user_claim_loader
#def add_claim_to_jwt(identity):
#    if identity==1:
#        return {'is_admin':True}
#    else:
#        return {'is_admin':False}    
#adding resources to api
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister,'/register')
api.add_resource(User,'/user/<int:user_id>')
api.add_resource(UserLogin,'/login')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
