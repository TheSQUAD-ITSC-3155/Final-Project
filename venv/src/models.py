from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Person(db.Model):

    User_Id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    passwords = db.Column(db.String, nullable=False)
    '''Picture_Id = db.Column(db.Integer, nullable=False)'''

class Post(db.Model):

    Post_Id = db.Column(db.Integer, primary_key=True)
    C_Name = db.Column(db.String, nullable=True)
    User_Id = db.Column(db.Integer, nullable=True)
    Words = db.Column(db.String, nullable=True) 
    
class Comments(db.Model):

    Comment_Id = db.Column(db.Integer, primary_key=True)
    '''Post_Id = db.Column(db.Integer, nullable=False)'''
    Post_Id = db.Column(db.Integer, db.ForeignKey('post.Post_Id'), nullable=False)
    User_Id = db.Column(db.Integer, nullable=False)
    Words = db.Column(db.String(500), nullable=False) 

    post = db.relationship('Post', backref=db.backref('comment', lazy=True))

class liked_posts(db.Model):
    
    Post_Id = db.Column(db.Integer, primary_key=True)
    User_Id = db.Column(db.Integer, primary_key=True)

class liked_comments(db.Model):
    
    Comment_Id = db.Column(db.Integer, primary_key=True)
    User_Id = db.Column(db.Integer, primary_key=True)