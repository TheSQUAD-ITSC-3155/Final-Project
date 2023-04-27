from src.models import *


class PostRepository:
    def get_all_posts(self) -> list[Post]:
        post: list[Post]=Post.query.all()
        return post
    
    def get_all_comments(self) -> list[Comments]:
        comment: list[Comments]=Comments.query.all()
        return comment

    def create_post(self, Post_Id: int, C_Name: str, User_Id: int, Words: str) -> Post:
        new_post = Post(Post_Id= Post_Id, C_Name=C_Name, User_Id = User_Id, Words=Words)
        db.session.add(new_post)
        db.session.commit()
        return new_post

# Singleton to be used in other modules
post_repository_singleton = PostRepository()