from flask import Blueprint, render_template, request
from utils import get_posts_all, get_comments_by_post_id, search_for_posts, get_post_by_pk


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

#представление для всех постов
@main_blueprint.route('/')
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)

@main_blueprint.route('/posts/<int:post_id>')
def post_list(post_id):
    post = get_post_by_pk(post_id)
    post_comment = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, post_comment=post_comment)

@main_blueprint.route('/search/')
def search():
    data = request.values["s"]
    posts = search_for_posts(data)
    return render_template('search.html', posts = posts)


