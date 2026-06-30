from flask import Flask, render_template, request, redirect, url_for

from storage.posts_repository import get_posts, add_post

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)