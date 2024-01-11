from flask import Flask, render_template, request, redirect, url_for, Request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
import os 
from sqlalchemy import desc


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''



app = Flask(__name__)
db = SQLAlchemy()
base_dir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "new-books-collection.db")
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

with app.app_context():
    db.create_all()
all_books = []


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(desc(Book.rating))).scalars()

    return render_template('index.html', all_books=all_books)


@app.route("/add", methods= ['GET', "POST"])
def add():
    if request.method=="POST":
        new_book= Book(title= request.form["name"],
            author= request.form["author"],
            rating= float(request.form["rating"]))
        db.session.add(new_book)
        db.session.commit()    
        return render_template('add.html', id=new_book.id)
    return render_template('add.html')


@app.route("/edit/<int:id>", methods= ['GET', "POST"])
def edit(id):
    with app.app_context():
        # book_to_update = db.session.execute(db.select(Book).where(Book.id == int(id))).scalar()
        book_to_update = db.session.get(Book, id)

    if request.method=="POST":
        book_to_update = db.session.get(Book, id)
        print(book_to_update.rating)
        book_to_update.rating = float(request.form["rating"])
        print(book_to_update.rating)
        db.session.commit()    
        return redirect(url_for('home'))
    
    return render_template('edit.html', title= book_to_update.title, rating = book_to_update.rating, id=id)

if __name__ == "__main__":
    app.run(debug=True)

