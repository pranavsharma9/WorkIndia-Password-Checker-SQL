from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from resources.user import UserRegister,UserVerify
from resources.site import SiteUserList,SiteUserListPrint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'pranav'
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(UserRegister,'/app/user')
api.add_resource(UserVerify,'/app/user/auth')
api.add_resource(SiteUserList,'/app/sites/<int:userId>')
api.add_resource(SiteUserListPrint,'/app/sites/list/<int:userId>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000,debug=True)
