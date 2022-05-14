from flask import Flask
from run import app

class TestApi:

# Тестируем все посты

    def test_app_all_posts_status_code(self):
        """Проверяем получен ли корректный вывод данных"""
        response = app.test_client().get("/api/posts", follow_redirects=True)
        assert response.status_code == 200, "Статус код всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_app_posts_type_count_content(self):
        """Проверяем правильность получения данных"""
        response = app.test_client().get("/api/posts", follow_redirects=True)
        assert type(response.json) == list, "Получен не список"
        # assert len(response.json) == 8, "Получено неверное количество элементов в списке"

    def test_app_all_posts_type_check_keys(self):
        """Проверяем есть ли нужные ключи в полученных данных"""

        keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

        response = app.test_client().get("/api/posts", follow_redirects=True)
        first_keys = set(response.json[0].keys())
        assert keys == first_keys, "Полученные ключи не совпадают"

# Тестируем один пост

    def test_app_one_post_type(self):
        """Проверяем правильность получения данных одного поста"""
        response = app.test_client().get("/api/posts/1", follow_redirects=True)
        assert type(response.json) == dict, "Получен не словарь"


    def test_app_all_one_post_type_check_keys(self):
        """Проверяем есть ли нужные ключи в полученном посте"""

        keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

        response = app.test_client().get("/api/posts/1", follow_redirects=True)
        one_keys = set(response.json.keys())
        assert keys == one_keys, "Полученные ключи не совпадают"