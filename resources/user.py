""" this is for user searching and registering
"""
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user import UserModel
import sqlite3

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
        type=str,
        required=True,
        help="enter username "
    )
_user_parser.add_argument('password',
        type=str,
        required=True,
        help="enter password "
    )


class UserRegister(Resource):

    def post(self):
        data = _user_parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"massage": f" username {data['username']} is already exists"},400

        user = UserModel(**data)
        user.save_to_db()
        return {"massage": f"user {data['username']} created successfully."},201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'massage': f" User with id {user_id} not founded"}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):



        user = UserModel.find_by_id(user_id)
        if not user:
            return {'massage': f" User with id:{user_id} not founded"}, 404
        user.delete_from_db()
        return {'massage': f" User with id:{user_id} deleted seccessfully"}, 200


class UserLogin(Resource):

    @classmethod
    def post(cls):
        # get data from parser
        data = _user_parser.parse_args()

        #find user in database
        user = UserModel.find_by_username(data['username'])

        #check password and creating token
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token= create_refresh_token(user.id)
            return {
                'access_token':access_token,
                'refresh_token':refresh_token
            }, 200
        return {'masssage':'invalid credential'}, 401
