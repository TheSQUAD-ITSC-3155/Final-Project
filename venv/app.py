from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from src.repositories.post_repository import post_repository_singleton

from src.models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
'mysql://root:MyLiyu2319*@localhost:3306/Data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def index():  
    return render_template('index.html')

@app.route('/home', methods=['POST', 'GET'])
def goHome():
    return render_template('home.html')

@app.route('/test')
def test():
    posts = post_repository_singleton.get_all_posts()
    return render_template('test.html', posts=posts)
'''
@app.route('/test', methods=['POST', 'GET'])
def list_all_posts():
    all_posts = post_repository_singleton.get_all_posts()
    return render_template('test.html', test=True, posts=all_posts)
    
@app.route('/test', methods=['POST', 'GET'])
def goHome():
    return render_template('test.html')

@app.route('/createpost', methods=['POST', 'GET'])
def postcreate():
    return render_template('createpost.html')

@app.route('/account', methods=['POST', 'GET'])
def createA():
    return render_template('account.html')

@app.route('/comment', methods=['POST', 'GET'])
def postcomment():
    return render_template('comment.html')
'''
if __name__ == "__main__":
    app.run(debug = True)