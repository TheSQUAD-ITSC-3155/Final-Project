from src.models import *


class PostRepository:
    def get_all_posts(self) -> list[Post]:
        post: list[Post]=Post.query.all()
        return post

# Singleton to be used in other modules
post_repository_singleton = PostRepository()