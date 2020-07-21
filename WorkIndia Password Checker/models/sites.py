from db import db
class SiteModel(db.Model):
    __tablename__ = 'sites'

    id=db.Column(db.Integer,primary_key=True)
    website=db.Column(db.String(80))
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))

    def __init__(self,website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def json(self):
        return {'website': self.website, 'username': self.username,'password':self.password}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, userId):
        return cls.query.filter_by(id=userId).first()
