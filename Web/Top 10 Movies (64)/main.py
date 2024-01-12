from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import requests
from sqlalchemy import delete, desc
import os
from password import API_KEY, API_ACCESS


API_SARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
API_BY_ID = "https://api.themoviedb.org/3/movie/"
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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap(app)

db=SQLAlchemy()
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "top-movies.db")
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String, unique=True, nullable=False) 
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False) 
    ranking =db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String, unique=False, nullable=False)
    img_url = db.Column(db.String, unique=True, nullable=False)
    
class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 10 eg. 7.6', validators=[DataRequired()])
    review = StringField(label = "Your Review", validators=[DataRequired()])
    submit = SubmitField(label='Update', render_kw={'class': 'knopka button btn col  text-center container add'})

class AddMovieForm(FlaskForm):
    label = StringField(label= 'Movie Title', validators =[DataRequired()])
    send = SubmitField(label='Find', render_kw={'class': 'knopka button btn col  text-center container add'})

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

with app.app_context():
    db.create_all()
    
    # db.session.add(new_movie)
    # db.session.add(second_movie)
    # db.session.commit()

@app.route("/", methods = ["GET","POST"])
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars()
    for index, movie in enumerate(all_movies, start=1):
        movie.ranking = index
    db.session.commit()
    all_movies = db.session.execute(db.select(Movie).order_by((Movie.ranking))).scalars()
    
    return render_template("index.html", bootstrap=bootstrap, movies = all_movies)
    
@app.route('/edit/<int:id>', methods=["GET","POST"])
def edit(id):
    movie_to_update = db.session.get(Movie, id)
    form = RateMovieForm()
    if request.method=="POST":
        movie_to_update = db.session.get(Movie, id)
        print(movie_to_update.rating)
        movie_to_update.rating = float(request.form["rating"])
        movie_to_update.review= request.form['review']
        db.session.commit()    
        return redirect(url_for('home'))
    
    return render_template('edit.html', title = movie_to_update.title, form = form)


@app.route('/delete/<int:id>')
def delete_film(id):
    stmt = delete(Movie).where(Movie.id == id)
    db.session.execute(stmt)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if request.method=="POST":
        reply = get_movie_details(form.label.data)
        return render_template('select.html', movies = reply)
    return render_template('add.html', form=form)

@app.route('/new_id/<int:id>')
def new_id(id):

    url = f"{API_BY_ID}/{id}"

    headers = {
        "accept": "application/json",
    "Authorization": f"Bearer {API_ACCESS}"}
    response = requests.get(url, headers=headers).json()
    id = add_movie_DB(response)
    return redirect(url_for('edit', id=id))

def add_movie_DB(json):
    print(f"https://image.tmdb.org/t/p/w500{json.get('poster_path')}")
    movie = Movie(
    title=json.get('original_title'),
    year=int(json.get('release_date')[:4]),
    description=json.get('overview'),
    rating=float(json.get('vote_average')),
    ranking=0,
    review="",
    img_url=f"https://image.tmdb.org/t/p/w500{json.get('poster_path')}"
)
    with app.app_context():
        db.session.add(movie)
        db.session.commit()
        db.session.refresh(movie)
    return movie.id

def get_movie_details(movie_name: str):
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_ACCESS}"
    }
    params = {"query": movie_name}
    response = requests.get(API_SARCH_ENDPOINT, headers=headers, params=params)
    print(response.json().get('results',[]))
    return response.json().get('results',[])

if __name__ == '__main__':
    app.run(debug=True)
