import json
from pprint import pprint as pp

class CommentDAO:

    def __init__(self, path):
        self.path = path

    def load_comments(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data_comments = json.load(file)
        return data_comments

    def get_all_comments(self):

        comments = self.load_comments()
        return comments

    def get_comments_by_post_id(self, post_id):
        comments = self.load_comments()

        comment_id = []

        for comment in comments:
            if comment['post_id'] == post_id:
                comment_id.append(comment)

        return comment_id

# cd = CommentDAO('../../data/comments.json')
# pp(cd.get_comments_by_post_id(3))