import json
import os


if not os.path.exists("posts.json"):
    with open("posts.json", "w") as data_obj:
        json.dump({}, data_obj)


def get_posts():
    with open("posts.json", "r") as data_obj:
        return json.load(data_obj)


def save_posts(posts):
    with open("posts.json", "w") as data_obj:
        json.dump(posts, data_obj)


def add_post(author, title, content):
    posts = get_posts()
    post_id = max([int(key) for key in posts.keys()], default=0) + 1
    posts[str(post_id)] = {"author": author,
                      "title": title,
                      "content": content}
    save_posts(posts)

def update_post_by_id(post_id, author=None, title=None, content=None):
    posts = get_posts()
    if author:
        posts[str(post_id)]["author"] = author
    if title:
        posts[str(post_id)]["title"] = title
    if content:
        posts[str(post_id)]["content"] = content
    save_posts(posts)


def delete_post_by_id(post_id):
    posts = get_posts()
    del posts[str(post_id)]
    save_posts(posts)

