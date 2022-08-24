import pytest

from app.posts_comment.dao.comments_dao import CommentDAO
from app.posts_comment.dao.posts_dao import PostDAO
from config.paths import POST_PATH, COMMENTS_PATH


@pytest.fixture
def comments_dao():
    return CommentDAO(COMMENTS_PATH)

@pytest.fixture
def posts_dao():
    return PostDAO(POST_PATH)