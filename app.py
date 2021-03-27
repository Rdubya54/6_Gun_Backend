from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:fuckstick@localhost:5432/SixGun"
db = SQLAlchemy(app)

migrate= Migrate(app, db)

from models.Posts import Posts
from models.Users import Users
from models.NewsFeed import NewsFeed

@app.route('/')
def hello():
    return {"hello":"world"}

@app.route('/posts',methods=['POST','GET'])
@cross_origin(expose_headers='Location')
def handle_posts():

    if request.method == 'POST':
        new_post = Posts(post=request.form['post'],userid=request.form['user'])
        db.session.add(new_post)
        db.session.commit()
        return {"message": f"post for user {new_post.userid} has been created sucessfully."}

    elif request.method =='GET':
        posts = Posts.query.all()
        results = [
            {
                "post": post.post,
                "user": post.user
            } for post in posts]

        return {"count":len(results), "posts":results}


@app.route('/users',methods=['POST','GET'])
@cross_origin(expose_headers='Location')
def handle_users():

    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = Users(username=data['username'],password=data['password'],email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"new user {new_user.username} has been created sucessfully."}
        else:
            return {"error":"The request payload is not in JSON format"}

    elif request.method =='GET':
        users = Users.query.all()
        results = [
            {
                "username": user.username,
                "password": user.password,
                "email":user.email
            } for user in users]

        return {"count":len(results), "users":results}

@app.route('/newsfeed',methods=['POST','GET'])
@cross_origin(expose_headers='Location')
def handle_newsfeed():

    if request.method =='GET':
        newsfeed = db.Table('newsfeed',db.metadata,autoload=True,autoload_with=db.engine)
        results=db.session.query(newsfeed).all()
        results = [
            {
                "username": post[1],
                "post":post[2]
            } for post in results]

        return {"count":len(results), "newsfeed":results}

    return {"error"}


if __name__ == '__main__':
    app.run(debug=True)