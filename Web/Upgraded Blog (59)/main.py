from flask import Flask, render_template, url_for
from post import Post

app = Flask(__name__)
POSTS = Post()

@app.route('/')
def home():
    return render_template( "index.html", blog = POSTS.blog_json)

@app.route('/index.html')
def index():
    f
    return render_template( "index.html", blog = POSTS.blog_json)

@app.route('/blog/<int:id>')
def get_post(id):
    title = "Error"
    subtitile = "Not Found"
    text = "No blog with such id"
    img = "post-bg.jpg"
    for blog in POSTS.blog_json:
        print(blog.get(id))
        if int(blog.get('id'))==id:
            title = blog.get('title')
            subtitile = blog.get('subtitle')
            text = blog.get('body')
            img = blog.get('pic')
    return render_template ("post.html", title =title, subtitile = subtitile, text = text, picture = img)

@app.route('/about.html')
def about():
    return render_template( "about.html")


@app.route('/contact')
def contact():
    return render_template( "contact.html")



        
if __name__ == "__main__":
    app.run(debug=True)
    