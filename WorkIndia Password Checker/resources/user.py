from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        user=UserModel(**data)
        user.save_to_db()

        return {"status": "account created"}, 201



class UserVerify(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        user=UserModel.find_by_username(data['username'])
        if user:
            return {"status": "success","userId":user.id}, 400
