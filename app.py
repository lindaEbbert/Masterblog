from flask import Flask, render_template, request, redirect, url_for

from storage.posts_repository import get_posts, add_post, delete_post_by_id, update_post_by_id, get_post_by_id

app = Flask(__name__)


@app.route('/')
def index():
    posts = get_posts()
    posts.reverse()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        post_author = request.form['author']
        post_title = request.form.get('title')
        post_content = request.form.get('content')
        add_post(post_author, post_title, post_content)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    delete_post_by_id(post_id)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    if request.method == 'POST':
        post_author = request.form['author']
        post_title = request.form.get('title')
        post_content = request.form.get('content')
        update_post_by_id(post_id, post_author, post_title, post_content)
        return redirect(url_for('index'))
    original_post = get_post_by_id(post_id)
    if not original_post:
        return "Post not found", 404
    return render_template('update.html',
                           original_author=original_post["author"],
                           original_title=original_post["title"],
                           original_content=original_post["content"],
                           post_id=post_id)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


"""
**************** COMMENTS FOR ALEJANDRO *******************
1) 
I really would love to go the extra bonus steps and get 
creative with the codio projects but I need to finish everything 
by the end of this week as I will start an internship next week.
That's why I'm a little bit under time pressure right now. ':D

2) 
I wrote you a message in discord regarding another codio project.
Could you have a look please? :)
*************************************************************
"""
