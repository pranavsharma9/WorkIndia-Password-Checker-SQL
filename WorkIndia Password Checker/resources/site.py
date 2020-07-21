from flask_restful import Resource, reqparse
from models.sites import SiteModel

class SiteUserList(Resource):
    TABLE_NAME = 'sites'

    parser = reqparse.RequestParser()
    parser.add_argument('website',
                        type=str,
                        required=True,
                        )
    parser.add_argument('username',
                        type=str,
                        required=True,
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        )
    def post(self,userId):
        data = SiteUserList.parser.parse_args()

        if SiteModel.find_by_id(userId):
            return {"message": "User with that userId already exists."}, 400

        user=SiteModel(**data)
        user.save_to_db()

        return {"status": "success"}, 201

class SiteUserListPrint(Resource):
    TABLE_NAME='sites'

    def get(self,userId):
        return {'list': list(map(lambda x: x.json(), SiteModel.query.filter_by(id=userId).all()))}
