import pytest


class TestPostsDAO:


    # Все посты

    def test_get_all_check_type(self, posts_dao):
        """Тестирует получение всех постов"""
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "Нет списка комментариев"
        assert len(posts) == 8

    def test_get_all_check_structure(self, posts_dao):
        """Тестирует получение всех постов возвращает верную структуру"""
        posts = posts_dao.get_posts_all()
        first_post = posts[0]
        keys_expected = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
        first_post_keys = set(first_post.keys())
        assert first_post_keys == keys_expected, "Полученные ключи неверны"


    # Один пост

    get_post_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]
    @pytest.mark.parametrize("post_pk", get_post_by_pk)
    def test_get_post_by_pk(self, posts_dao, post_pk):
        """Тестирует получение поста по его id"""

        post = posts_dao.get_post_by_pk(post_pk)


    def test_get_by_pk_none(self, posts_dao):
        """Тестирует получение несуществующего поста"""
        no_post = posts_dao.get_post_by_pk(0)
        assert no_post == None


    # Посты по пользователю

    post_by_user = [("johnny", {2, 6}),
                    ("larry", {4, 8}),
                    ("leo", {1, 5}),
                    ('hank', {3, 7})
                    ]

    @pytest.mark.parametrize("poster_name, post_pks_correct", post_by_user)
    def test_get_posts_by_user(self, posts_dao, poster_name, post_pks_correct):
        """Тестирует поиск по пользователю"""

        posts = posts_dao.get_posts_by_user(poster_name)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct

    # Поиск постов

    post_search = [("еда", {1}),
                   ("свалка", {3}),
                   ("пальто", {4}),
                   ("закат", {7})
                   ]

    @pytest.mark.parametrize("query, post_pks_correct", post_search)
    def test_search_for_posts(self, posts_dao, query, post_pks_correct):
        """Тест поиска"""
        posts = posts_dao.search_for_posts(query)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct, "Пост не найден"