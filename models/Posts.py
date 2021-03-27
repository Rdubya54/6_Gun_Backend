from app import db

class Posts(db.Model):
    __tablename__ = 'Posts'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String())
    userid = db.Column(db.Integer)

    def __init__(self,post,userid):
        self.post=post,
        self.userid=userid

    def __repr__(self):
        return f"<Post {self.post}>"