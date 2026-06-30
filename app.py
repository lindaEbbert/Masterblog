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

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    if request.method == 'POST':
        post_author = request.form['author']
        post_title = request.form.get('title')
        post_content = request.form.get('content')
        update_post_by_id(post_id, post_author, post_title, post_content)
        return redirect(url_for('index'))
    original_post = get_post_by_id(post_id)
    return render_template('edit.html',
                           original_author = original_post["author"],
                           original_title = original_post["title"],
                           original_content = original_post["content"],
                           post_id = post_id)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)