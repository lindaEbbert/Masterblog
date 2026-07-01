import json
import os

JSON_PATH = "posts.json"

def initialize_json():
    """ Initializes the json file if needed"""
    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, "w") as data_obj:
            """@Alejandro: I know that there (and below in save_posts()) 
            probably should be an encoding parameter. Pls have a look at discord. 
            I wrote you a message with a question there."""
            json.dump([], data_obj)


def get_posts():
    """ Gets all posts from the database and return them as a dictionary"""
    initialize_json()
    with open(JSON_PATH, "r") as data_obj:
        return json.load(data_obj)


def save_posts(posts):
    """ Saves posts to the database"""
    with open(JSON_PATH, "w") as data_obj:
        json.dump(posts, data_obj)


def get_max_post_id():
    """ Gets the max post id from the database. If there are no posts, returns 0"""
    posts = get_posts()
    if not posts:
        return 0
    max_id = int(posts[0]["id"])
    for post in posts:
        if int(post["id"]) > max_id:
            max_id = int(post["id"])
    return max_id


def add_post(author, title, content):
    """ Adds a new post to the database"""
    posts = get_posts()
    next_post_id = get_max_post_id() + 1
    posts.append({"id": str(next_post_id),
                  "author": author,
                  "title": title,
                  "content": content})
    save_posts(posts)


def update_post_by_id(post_id, author=None, title=None, content=None):
    """ Updates a post in the database"""
    posts = get_posts()
    for post in posts:
        if post["id"] == str(post_id):
            post_index = posts.index(post)
            if author:
                posts[post_index]["author"] = author
            if title:
                posts[post_index]["title"] = title
            if content:
                posts[post_index]["content"] = content
            break
    save_posts(posts)


def delete_post_by_id(post_id):
    """ Deletes a post from the database
    :param post_id: The id of the post to delete"""
    posts = get_posts()
    post_id_found = False
    for post in posts:
        if post["id"] == str(post_id):
            post_index_in_posts = posts.index(post)
            del posts[post_index_in_posts]
            post_id_found = True
            break
    if post_id_found:
        print(f"Entry with post id {post_id} successfully deleted.")
        save_posts(posts)
    else:
        print(f"No entry found for post id {post_id}.")


def get_post_by_id(post_id):
    """ Gets a post from the database by its id
    :param post_id: post id
    :return: dictionary of the post, none if not found
    """
    posts = get_posts()
    for post in posts:
        if post["id"] == str(post_id):
            return post
    return None