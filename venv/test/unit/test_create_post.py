import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import unittest
from flask import Flask
from src.models import Post
from src.models import db

app = Flask(__name__)

class TestPost(unittest.TestCase):

    def test_create_post(self):
        with app.app_context():
            # Call the method being tested
            new_post = Post.create_post(Post_Id=0, C_Name='Test Post', User_Id=0, Words='This is a test post')
            
            # Check if the new post was added to the database
            retrieved_post = Post.query.filter_by(Post_Id=0).first()
            self.assertIsNotNone(retrieved_post)
            
            # Check if the details of the retrieved post match with the details of the new post
            self.assertEqual(new_post.Post_Id, retrieved_post.Post_Id)
            self.assertEqual(new_post.C_Name, retrieved_post.C_Name)
            self.assertEqual(new_post.User_Id, retrieved_post.User_Id)
            self.assertEqual(new_post.Words, retrieved_post.Words)