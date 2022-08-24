from flask import Blueprint, render_template, request
from app.posts_comment.dao.posts_dao import PostDAO
from app.posts_comment.dao.comments_dao import CommentDAO
from config.paths import POST_PATH, COMMENTS_PATH
import logging


pc_blueprint = Blueprint('pc_blueprint', __name__, template_folder='templates', static_folder='static')


posts_dao = PostDAO(POST_PATH)
comments_dao = CommentDAO(COMMENTS_PATH)

@pc_blueprint.route('/')
def index_page():
    posts = posts_dao.get_posts_all()
    return render_template('index.html', posts=posts)

@pc_blueprint.route('/posts/<int:post_id>')
def post_id_page(post_id):

    post = posts_dao.get_post_by_pk(post_id)
    comments = comments_dao.get_comments_by_post_id(post_id)
    comments_len = len(comments)

    return render_template('post.html', post=post, comments=comments, comments_len=comments_len)

@pc_blueprint.route('/search')
def search_page():
    s = request.args.get('s', '')
    posts = posts_dao.search_for_posts(s)
    post_count = len(posts)
    return render_template('search.html', posts=posts, post_count=post_count, query=s)

@pc_blueprint.route('/users/<user_name>')
def user_name_page(user_name):
    posts = posts_dao.get_posts_by_user(user_name)
    posts_count = len(posts)
    return render_template('user-feed.html', posts=posts, posts_count=posts_count)
