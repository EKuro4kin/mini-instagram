# from flask import Blueprint, render_template
# from app.posts.dao.comments_dao import CommentsDAO
#
# # Создаем блупринт
# comments_blueprint = Blueprint('comments_blueprint', __name__, template_folder="templates")
#
# # Создаем DAO
# comments_dao = CommentsDAO("./data/posts.json")
#
# # Создаем вьюшку для кандидатов
# @comments_blueprint.route('/posts/')
# def page_candidates_all():
#     # posts = posts_dao.get_posts_all()
#     return render_template("post.html")