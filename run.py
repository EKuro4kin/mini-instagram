from flask import Flask

from app.posts.views import posts_blueprint # Импортируем блюпринт
# from app.vacancies.views import vacancies_blueprint
# from app.main.views import main_blueprint


app = Flask(__name__)                   # Создаем экземпляр Flask
app.register_blueprint(posts_blueprint)  # регистрируем первый блюпринт


if __name__ == "__main__":               # Запускаем сервер только, если файл запущен, а не импортирован
    app.run()