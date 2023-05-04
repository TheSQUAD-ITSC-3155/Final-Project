from src.models import *


class PostRepository:
    def get_all_posts(self) -> list[Post]:
        post: list[Post]=Post.query.all()
        return post
    
    def get_all_comments(self) -> list[Comments]:
        comment: list[Comments]=Comments.query.all()
        return comment

    def get_all_accounts(self) -> list[Person]:
        person: list[Person]=Person.query.all()
        return person
    
    def get_all_likedcomments(self) -> list[liked_comments]:
        likedcomment: list[liked_comments]=liked_comments.query.all()
        return likedcomment
    
    def get_all_likedposts(self) -> list[liked_posts]:
        likedpost: list[liked_posts]=liked_posts.query.all()
        return likedpost

    def create_post(self, Post_Id: int, C_Name: str, User_Id: int, Words: str) -> Post:
        new_post = Post(Post_Id= Post_Id, C_Name=C_Name, User_Id = User_Id, Words=Words)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def create_comment(self, Comment_Id: int, Post_Id: int, User_Id: int, Words: str) -> Comments:
        '''Post_Id = Post.query.get(Post_Id)'''
        new_comment = Comments(Comment_Id= Comment_Id, Post_Id =Post_Id, User_Id = User_Id, Words=Words)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

    def create_account(self, User_Id: int, Username: str, email: str, passwords: str,) -> Person:
        new_person = Person(User_Id = User_Id, Username=Username, email=email, passwords=passwords)
        db.session.add(new_person)
        db.session.commit()
        return new_person
    
    #Liked Things
    def add_likedcomment(self, Post_Id: int, User_Id: int,) -> liked_comments:
        new_likedcomment = liked_comments(Post_Id = Post_Id, User_Id = User_Id)
        db.session.add(new_likedcomment)
        db.session.commit()
        return new_likedcomment
    
    #Remove Things
    def remove_comment(self, Comment_Id: int,) -> Comments:
        comment_delete = Comments.query.get(Comment_Id)
        db.session.delete(comment_delete)
        db.session.commit()

# Singleton to be used in other modules
post_repository_singleton = PostRepository()