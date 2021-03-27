from app import db

class NewsFeed(db.Model):
    __tablename__ = 'newsfeed'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    post = db.Column(db.String())

    def __init__(self,username,post):
        self.username=username,
        self.post=post

    def __repr__(self):
        return f"<Post {self.post}>"