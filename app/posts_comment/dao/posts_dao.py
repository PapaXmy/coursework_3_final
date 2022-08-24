import json
from pprint import pprint as pp

class PostDAO:

    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        """Возвращает все посты"""
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data


    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя"""
        posts = self.get_posts_all()

        posts_user = []
        for post in posts:
            if post['poster_name'] == user_name:
                posts_user.append(post)
        return posts_user

    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""
        posts = self.get_posts_all()
        if query in ['', ' ']:
            return []


        matching_post = []
        query_lower = str(query).lower()

        for post in posts:
            if query_lower in post['content'].lower():
                matching_post.append(post)

        return matching_post

    def get_post_by_pk(self, pk):
        """Возвращает пост по его идентификатору"""
        posts = self.get_posts_all()

        for post in posts:
            if post['pk'] == pk:
                return post


#
# pd = PostDAO("../../data/posts_comment.json")
# pp(pd.get_post_by_pk(2))