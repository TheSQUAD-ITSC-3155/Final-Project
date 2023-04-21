from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Person(db.Model):

    User_Id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String, nullable=False)
    Picture_Id = db.Column(db.Integer, nullable=False)
'''
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(100))
    post_content = db.Column(db.Text)
'''

class Post(db.Model):

    Post_Id = db.Column(db.Integer, primary_key=True)
    C_Name = db.Column(db.String, nullable=False)
    User_Id = db.Column(db.Integer, nullable=False)
    Words = db.Column(db.String, nullable=False) 

class C_Comment(db.Model):

    Comment_Id = db.Column(db.Integer, primary_key=True)
    Post_Id = db.Column(db.Integer, nullable=False)
    C_Name = db.Column(db.String, nullable=False)
    User_Id = db.Column(db.Integer, nullable=False)
    Words = db.Column(db.String, nullable=False) 

class liked_posts(db.Model):
    
    Post_Id = db.Column(db.Integer, primary_key=True)
    User_Id = db.Column(db.Integer, primary_key=True)

class liked_comments(db.Model):
    
    Comment_Id = db.Column(db.Integer, primary_key=True)
    User_Id = db.Column(db.Integer, primary_key=True)