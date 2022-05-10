import json

class CommentsDAO:

    def __init__(self, path):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id):
        """ возвращает комментарии определенного поста"""
        comments = self.load_data()
        comments_founded = []
        for comment in comments:
            if comment["post_id"] == post_id:
                comments_founded.append(comment)
        return comments_founded