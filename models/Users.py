from app import db

class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self,username,password,email):
        self.username=username,
        self.password=password,
        self.email=email

    def __repr__(self):
        return f"<User {self.username}>"