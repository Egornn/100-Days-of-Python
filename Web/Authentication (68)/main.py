from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os


from wtforms import StringField, EmailField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
# CREATE DATABASE
class Base(DeclarativeBase):
    pass

base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(base_dir,'static')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, "instance/users.db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)

    # def get_id(self):
    #     return str(self.id)

 
class UserForm(FlaskForm):
    name = StringField(label='Name',validators =[DataRequired(message= "Field is required")])
    email = EmailField(label='Email',validators =[DataRequired(message= "Field is required")])
    password = PasswordField(label='Password',validators =[DataRequired(message= "Field is required")])

class LoginForm(FlaskForm):
        email = EmailField(label='Email',validators =[DataRequired(message= "Field is required")])
        password = PasswordField(label='Password',validators =[DataRequired(message= "Field is required")])



with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods= ["GET", "POST"])
def register():
    
    if request.method == 'POST':
        hash_password = generate_password_hash(request.form.get('password'),method='pbkdf2:sha256', salt_length=6)
        
        new_user = User(
            name = request.form.get('name'),
            email = request.form.get('email'),
            password = hash_password,
        )
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user:
                flash('User with such email already exists')
                return redirect(url_for('login'))
        else: 
            db.session.add(new_user)
            db.session.commit()     
            login_user(new_user)
            return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods =['GET', "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
    # if form.validate_on_submit():
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user:
            if check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Wrong password.', 'danger')
        else: 
            flash('Wrong email.', 'danger')
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)

    return render_template("secrets.html", name = current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], 'files/cheat_sheet.pdf', as_attachment=True
    )



if __name__ == "__main__":
    app.run(debug=True)
