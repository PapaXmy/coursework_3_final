import pytest

class TestCommentDAO:

    def test_get_comment_all_type(self, comments_dao):
        """Тест типа и количество полученных коментариев"""

        comments = comments_dao.load_comments()
        assert type(comments) == list, "Нет списка комментариев"
        assert len(comments) == 20

    def test_get_comments_all_sructure(self, comments_dao):
        """Тест структуры комментариев"""

        comments = comments_dao.load_comments()
        comment_first = comments[0]
        # ключи комментариев
        key = {"post_id", "commenter_name", "comment", "pk"}
        first_comment_key = set(comment_first.keys())
        assert first_comment_key == key, "Полученные ключи неверные"

    def test_get_comment_by_post_id_type(self, comments_dao):
        """Тест получения комментариев к посту"""
        comments_post = comments_dao.get_comments_by_post_id(7)
        assert type(comments_post) == list, "Коментарии должны быть списком"

    comments_id = [1, 2, 3]

    @pytest.mark.parametrize("post_id", comments_id)
    def test_get_comment_by_post_id_type(self, comments_dao, post_id):
        """Тест полученных комментариев к каждому посту"""

        comment_post = comments_dao.get_comments_by_post_id(post_id)

        for comment in comment_post:
            assert comment["post_id"] == post_id