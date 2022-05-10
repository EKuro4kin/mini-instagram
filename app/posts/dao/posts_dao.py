import json

class PostsDAO:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        """ Возвращает возвращает посты"""
        posts = self.load_data()
        return posts

    def get_posts_by_user(self, user_name):
        """ возвращает посты определенного пользователя"""
        posts = self.load_data()
        user_posts = []
        for post in posts:
            if user_name.lower() == post["poster_name"].lower():
                user_posts.append(post)
        return user_posts

    def get_post_by_pk(self, pk):
        """ возвращает один пост по его идентификатору"""
        posts = self.load_data()
        for post in posts:
            if post["pk"] == pk:
                return post

    def get_search_for_posts(self, query):
        """ возвращает список постов по ключевому слову"""
        posts = self.load_data()
        posts_founded = []
        for post in posts:
            if query.lower() in post["content"].lower():
                posts_founded.append(post)
        return posts_founded

