from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime
import os
'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b3'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, "instance/posts.db")
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class BlogForm (FlaskForm):
    title = StringField(label='Blogpost Title',validators =[DataRequired(message= "Field is required")])
    subtitle = StringField(label='Blogpost Subtitle',validators =[DataRequired(message= "Field is equired")])
    author = StringField(label='Blogpost Author',validators =[DataRequired(message= "Field is required")])
    img_url = URLField(label='Blogpost Image URL',validators =[DataRequired(message= "Field is required")])
    body = CKEditorField(label = 'Blog Data',validators =[DataRequired(message= "Field is required")])
    submit = SubmitField(label="Add Post")


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    data:[BlogPost] = BlogPost.query.order_by(BlogPost.id).all()
    print(data)
    for row in data:
        new_element = {'id':row.id,
                       'title':row.title,
                       'date':row.date,
                       'body':row.body,
                       'author':row.author,
                       'img_url':row.img_url,
                       'subtitle':row.subtitle,
                       }
        print(new_element)
        posts.append(new_element)
    print(posts)
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    session = db.session
    post_by_id=session.query(BlogPost).get(post_id)
    requested_post = {'id':post_by_id.id,
                       'title':post_by_id.title,
                       'date':post_by_id.date,
                       'body':post_by_id.body,
                       'author':post_by_id.author,
                       'img_url':post_by_id.img_url,
                       'subtitle':post_by_id.subtitle,
                       }
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods= ["GET", "POST"])
def new_post():
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%B %d, %Y")
        new_blogpost= BlogPost(
                title = request.form['title'],
                subtitle = request.form['subtitle'],
                date =date,
                body =request.form['body'],
                author = request.form['author'],
                img_url = request.form['img_url'],
                )
        with app.app_context():
            db.session.add(new_blogpost)
            db.session.commit()
        return redirect(url_for('get_all_posts'))
    form = BlogForm()
    return render_template('make-post.html', form =form, title_h1='New Post')

# TODO: edit_post() to change an existing blog post

@app.route('/edit_post/<int:post_id>', methods= ["GET", "POST"])
def edit_post(post_id):
    if request.method == 'POST':
        blogpost_update = db.session.query(BlogPost).filter_by(id=post_id).first()
        print(post_id)
        blogpost_update.title = request.form['title']
        blogpost_update.subtitle = request.form['subtitle']
        blogpost_update.body =request.form['body']
        blogpost_update.author = request.form['author']
        blogpost_update.img_url = request.form['img_url']
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    blogpost =db.session.get(BlogPost, post_id)
    form = BlogForm(obj=blogpost)
    print(blogpost)
    return render_template('make-post.html', form =form, title_h1='Edit Post')
# TODO: delete_post() to remove a blog post from the database

@app.route('/delete_post/<int:post_id>', methods= ["GET", "POST"])
def delete_post(post_id):
    post_to_delete = db.session.get(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
