import os

import pytest

from app.posts.dao.posts_dao import PostsDAO

class TestPostsDAO:

    @pytest.fixture
    def posts_dao(self):
        print(os.getcwd())
        return PostsDAO("../../../data/posts.json")

    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    # Получение постов

    def test_get_all_check_type(self, posts_dao):
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "Список постов должен быть списком"
        assert type(posts[0]) == dict, "Каждый пост должен быть словарём"

    def test_get_all_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.get_posts_all()
        first_post = posts[0]
        first_post_keys = set(first_post.keys())
        assert first_post_keys == keys_expected, "Полученные ключи неверны"


    # Получение одного поста

    def test_get_one_chack_type(self, posts_dao):
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, "Пост должен быть словарем"

    def test_get_one_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_post_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == keys_expected, "Полученные ключи неверны"

    parameters_to_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize("post_pk", parameters_to_get_by_pk)
    def test_get_one_chack_type_has_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_post_by_pk(post_pk)
        assert post["pk"] == post_pk, "Номер полученного поста не соответствует запрошенному"

    # Получение по пользователю

    post_parameters_by_user = [("leo", {1,5}), ("larry", {4,8}), ("hank", {3,7})]

    @pytest.mark.parametrize("poster_name, post_pks_correct", post_parameters_by_user)
    def test_get_posts_by_user(self, posts_dao, poster_name, post_pks_correct):
        """Проверяет, что поиск по пользователю работает верно"""

        posts = posts_dao.get_posts_by_user(poster_name)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct

    # Поиск постов

    post_parameters_search = [("пирог", {1}), ("елки", {3}), ("проснулся", {4})]

    @pytest.mark.parametrize("query, post_pks_correct", post_parameters_search)
    def test_search_for_posts(self, posts_dao, query, post_pks_correct):
        """Проверяет, что поиск работает"""
        posts = posts_dao.get_search_for_posts(query)
        post_pks = set()
        for post in posts:
            post_pks.add(post["pk"])

        assert post_pks == post_pks_correct