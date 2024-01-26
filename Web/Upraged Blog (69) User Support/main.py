from datetime import date
from flask import Flask, request, abort, render_template, redirect, url_for, flash
from typing import List
# import flask-gravatar
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import AnonymousUserMixin, UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
from flask import g, request, redirect, url_for
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


# Import your forms from the forms.py
from forms import CreatePostForm, CommentForm
import os
from forms import RegisterForm, LoginForm





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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(base_dir,'static')

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, "instance/posts.db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        return redirect(url_for('get_all_posts'))
    return decorated_function


# CONFIGURE TABLES


class User(db.Model, UserMixin):
    __tablename__='user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    children: Mapped[List["BlogPost"]] = relationship()
    children_comment: Mapped[List["Comment"]] = relationship()
    
    

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    parent_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    parent: Mapped["User"] = relationship(back_populates="children")
    children: Mapped[List["Comment"]] = relationship()

    

class Comment(db.Model):
    __tablename__='comments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    parent_id_blogpost: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
    parent_blogpost: Mapped["BlogPost"] = relationship(back_populates="children")
    parent_id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))
    parent_user: Mapped["User"] = relationship(back_populates="children_comment")



with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods= ["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        hash_password = generate_password_hash(request.form.get('password'),method='pbkdf2:sha256', salt_length=8)
        
        new_user = User(
            name = request.form.get('name'),
            email = request.form.get('email'),
            password = hash_password,
        )
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
                flash('User with such email already exists')
                return redirect(url_for('login'))
        else: 
            db.session.add(new_user)
            db.session.commit()     
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)



# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user:
            if check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:
                flash('Wrong password.', 'danger')
        else: 
            flash('Wrong email.', 'danger')
    return render_template("login.html", form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods= {"GET","POST"})
def show_post(post_id):
    
    requested_post = db.get_or_404(BlogPost, post_id)
    form= CommentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            comment = Comment(
                text= form.body.data,
                parent_id_blogpost=post_id,
                parent_id_user=current_user.id,
            )
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Please login into your account first')
            return redirect(url_for('login'))
    return render_template("post.html", post=requested_post, form =form, comments = requested_post.children)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.name,
            parent_id = current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user.name
        post.body = edit_form.body.data
        
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
