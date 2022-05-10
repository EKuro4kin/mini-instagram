from flask import Blueprint, render_template, request
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")

# Создаем DAO
posts_dao = PostsDAO("./data/posts.json")
comments_dao = CommentsDAO("./data/comments.json")

# Создаем вьюшку главной страницы со всеми постами
@posts_blueprint.route('/')
def page_posts_all():
    posts = posts_dao.get_posts_all()
    return render_template("index.html", posts=posts)

# Создаем вьюшку с выводом конкретного поста и комментариями к нему
@posts_blueprint.route('/posts/<int:postid>')
def post_by_pk(postid):
    post = posts_dao.get_post_by_pk(postid)
    comments = comments_dao.get_comments_by_post_id(postid)
    count_comments = len(comments)
    return render_template("post.html", post=post, comments=comments, count_comments=count_comments)

# Создаем вьюшку с выводом конкретного поста и комментариями к нему
@posts_blueprint.route('/search/<s>')
def page_search_for_posts(s):
    # s = request.args.get("s")
    # posts = posts_dao.get_posts_all()
    if s:
        filter_posts = posts_dao.get_search_for_posts(s)
        count_posts = len(filter_posts)
        return render_template("search.html", posts=filter_posts, count_posts=count_posts)
    return "вы не ввели слово для фильтрации постов"

@posts_blueprint.route('/users/<username>')
def page_posts_by_user(username):
    filter_user_posts = posts_dao.get_posts_by_user(username)
    return render_template("user-feed.html", posts=filter_user_posts)




