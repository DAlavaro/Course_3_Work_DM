import json


def get_posts_all():
    """Возвращает посты"""
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_comments_all():
    """Возвращает комментарии"""
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя."""
    posts = get_posts_all()
    return [post for post in posts if post['poster_name'] == user_name]


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста."""
    comments = get_comments_all()
    return [comment for comment in comments if comment["post_id"] == post_id]


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    return [post for post in posts if query in post["content"]]


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору."""
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
