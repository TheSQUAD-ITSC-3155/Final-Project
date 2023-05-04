import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
import unittest
from flask import Flask
from src.models import Post

from src.models import db

app = Flask(__name__)

class TestPost(unittest.TestCase):

    def test_get_all_posts(self):
        with app.app_context():
            # Add some test data to the database
            post1 = Post.create_post(Post_Id=0, C_Name='Post 1', User_Id=0, Words='Content for post 1')
            post2 = Post.create_post(Post_Id=1, C_Name='Post 2', User_Id=1, Words='Content for post 2')
            db.session.add(post1)
            db.session.add(post2)
            db.session.commit()

            # Call the method being tested
            result = Post.get_all_posts()

