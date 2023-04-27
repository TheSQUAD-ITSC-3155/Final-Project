from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from src.repositories.post_repository import post_repository_singleton
import pymysql
import random

from sqlalchemy import func
from src.models import Post

from src.models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
'mysql+pymysql://root:password@localhost:3306/Reddit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def index():  
    return render_template('index.html')

@app.route('/home', methods=['POST', 'GET'])
def goHome():
    posts = post_repository_singleton.get_all_posts()
    return render_template('home.html', posts=posts)

@app.route('/test')
def test():
    posts = post_repository_singleton.get_all_posts()
    return render_template('test.html', posts=posts)


"""@app.route('/createpost', methods=['POST', 'GET'])
def postcreate():
    if request.method == 'POST':
        Post_Id = 3
        C_Name = request.form.get('post_name', "hi")
        User_Id = 0
        Words = request.form.get('post_content', "hello")
        print("C_Name: ", C_Name)
        print("Words: ", Words)
        return render_template('createpost.html', C_Name=C_Name, Words=Words)
    return render_template('createpost.html')"""

@app.route('/createpost', methods=['POST', 'GET'])
def postcreate():
    C_Name = ""
    Words = ""
    if request.method == 'POST':
        C_Name = request.form.get('post_name')
        Words = request.form.get('post_content')
        Post_Id = db.session.query(func.count(Post.Post_Id)+1).scalar()
        User_Id = 0
        if (C_Name != ""):
            created_post = post_repository_singleton.create_post(Post_Id, C_Name, User_Id, Words)
            return redirect('/home')
    return render_template('createpost.html')


@app.route('/account', methods=['POST', 'GET'])
def createA():
    return render_template('account.html')

@app.route('/comment', methods=['POST', 'GET'])
def postcomment():
    return render_template('comment.html')

if __name__ == "__main__":
    app.run(debug = True)