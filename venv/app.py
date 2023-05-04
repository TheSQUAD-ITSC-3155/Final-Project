from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from src.repositories.post_repository import post_repository_singleton
import pymysql
import random

from sqlalchemy import func
from src.models import Post
from src.models import Comments
from src.models import Person

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
    password = request.form.get('password')
    username = request.form.get('username')
    posts = post_repository_singleton.get_all_posts()
    users = post_repository_singleton.get_all_accounts()
    if request.method == 'POST':
        for user in users:
            if (password == user.passwords and username == user.Username):
                return render_template('home.html', posts=posts)
    return render_template('index.html')

@app.route('/newAccount', methods=['POST', 'GET'])
def pengus():
    return redirect('/account')

@app.route('/test')
def test():
    posts = post_repository_singleton.get_all_posts()
    return render_template('test.html', posts=posts)

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
'''
@app.route('/comment', methods=['POST', 'GET'])
def postcomment():
    comments = post_repository_singleton.get_all_comments()
    return render_template('comment.html',comments=comments)

@app.route('/comment', methods=['POST', 'GET'])
def postcomment():
    if request.method == 'POST':
        Words = request.form.get('post_comment')
        if Words:
            Comment_Id = db.session.query(func.count(Comments.Comment_Id)+1).scalar()
            Post_Id = 1
            User_Id = 1
            created_comment = post_repository_singleton.create_comment(Comment_Id, Post_Id, User_Id, Words)
            return redirect('/comment')
    comments = post_repository_singleton.get_all_comments()
    return render_template('comment.html', comments=comments)
'''
@app.route('/comment', methods=['POST', 'GET'])
def postcomment():
    posts = post_repository_singleton.get_all_posts()
    #if (request.form.get('debug2'))
    #Post_Id = 0
    Post_Id = int(request.form.get('debug2'))
    comments = post_repository_singleton.get_all_comments()
    Words = request.form.get('post_comment')
    Comment_Id = db.session.query(func.count(Comments.Comment_Id)+1).scalar()
    User_Id = 1
    created_comment = post_repository_singleton.create_comment(Comment_Id, Post_Id, User_Id, Words)
    return render_template('comment.html', comments=comments, posts = posts, Post_Id = Post_Id)
    #return redirect("/comment")

@app.route('/commentPage', methods=['POST', 'GET'])
def viewcomment():
    posts = post_repository_singleton.get_all_posts()
    #if (request.form.get('debug2'))
    #Post_Id = 0
    Post_Id = int(request.form.get('debug'))
    comments = post_repository_singleton.get_all_comments()
    return render_template('comment.html', comments=comments, posts = posts, Post_Id = Post_Id)

'''
@app.route('/account', methods=['POST', 'GET'])
def createA():
    person = post_repository_singleton.get_all_accounts()
    return render_template('account.html', person=person)
'''
@app.route('/account', methods=['POST', 'GET'])
def createA():
    Username = ""
    email = ""
    password=""
    if request.method == 'POST':
        Username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        User_Id = db.session.query(func.count(Person.User_Id)+1).scalar()
        if (Username != ""):
            created_account = post_repository_singleton.create_account(User_Id, Username, email, password)
            return redirect('/home')
    return render_template('account.html')

if __name__ == "__main__":
    app.run(debug = True)