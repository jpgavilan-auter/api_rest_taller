from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    admin = db.Column(db.Text, nullable=False)
    profile_picture = db.Column(db.Text, nullable=True)
    jwt_token = db.Column(db.Text, nullable=True)

    def serialize(self):
        return {
            "id" : self.id,
            "username" : self.username,            
            "admin" : self.admin,
            "profile_picture" : self.profile_picture,
            "jwt_token" : self.jwt_token
        }