from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = {
    0:{
        'id' : 0,
        'title' : 'Hello World!',
        'content' : "This is my first blog!"
    }
}

@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.html', message = f"A post with id {post_id} was not found.")
    
    #return f"Post: {post['title']}, Content:\n\n{post['content']}"
    return render_template('post.html', post = post)

"""@app.route('/post/form')
def form():
    return render_template('create.html')"""

@app.route('/post/create', methods=['GET', 'POST'])
def create_post():
    if request.method=='POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id':post_id, 'title':title, 'content':content}
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.html')

if __name__=='__main__':
    app.run(debug=True)
