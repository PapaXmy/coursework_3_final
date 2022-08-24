from flask import Blueprint, jsonify
from app.posts_comment.dao.posts_dao import PostDAO
from config.paths import POST_PATH
import logging


api_blueprint = Blueprint("api_blueprint", __name__)
logging.basicConfig(filename="logs/api.log",
                    level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s"
                    )
logging.info('Запрос')

post_dao = PostDAO(POST_PATH)

@api_blueprint.route('/api/posts/')
def posts_api():
    logging.info('Запрос')
    posts = post_dao.get_posts_all()
    return jsonify(posts), 200

@api_blueprint.route('/api/posts/<int:post_id>')
def single_post_api(post_id):
    logging.info('Запрос')
    post = post_dao.get_post_by_pk(post_id)
    return jsonify(post), 200
