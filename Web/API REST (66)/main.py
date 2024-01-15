from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(base_dir, "instance/cafes.db")

db = SQLAlchemy()
db.init_app(app)


def make_data(list_of_db):
    all_data={}
    for row in list_of_db:
        cafe_data = {
            "name": row.name,
            "map_url":row.map_url,
            'img_url': row.img_url,
            'location': row.location,
            'seats': row.seats,
            'has_toilet': row.has_toilet,
            'has_wifi': row.has_wifi,
            'has_sockets': row.has_sockets,
            'can_take_calls': row.can_take_calls,
            'coffee_price': row.coffee_price,
            }
        all_data[f'{row.id}']=cafe_data
    return all_data

# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random')
def random():
    session = db.session
    row =  session.query(Cafe).order_by(func.random()).first()
    if row:
        # cafe_data = {
        #     "name": row.name,
        #     "map_url":row.map_url,
        #     'img_url': row.img_url,
        #     'location': row.location,
        #     'seats': row.seats,
        #     'has_toilet': row.has_toilet,
        #     'has_wifi': row.has_wifi,
        #     'has_sockets': row.has_sockets,
        #     'can_take_calls': row.can_take_calls,
        #     'coffee_price': row.coffee_price,
        #     }
        # return jsonify(cafe_data)
        return jsonify(name=row.name, map_url=row.map_url, img_url=row.img_url, location = row.location, seats = row.seats, has_toilet = row.has_toilet, has_wifi=row.has_wifi, has_sockets = row.has_sockets, can_take_calls = row.can_take_calls, coffee_price=row.coffee_price)
    return '<h1>Probably missing DB</h1>'

@app.route('/all')
def all():
    all_cafe_DB =  Cafe.query.order_by(Cafe.id).all()
    return jsonify(make_data(all_cafe_DB))

@app.route('/search')
def search():
    location = request.args.get('loc').capitalize() 
    subselection = Cafe.query.filter(Cafe.location == location).all()
    print(subselection)
    if len(subselection) == 0:
        return jsonify(Not_found='No Cafe in Specified Location')
    return jsonify(make_data(subselection)) 

@app.route('/add_cafe', methods=["GET","POST"])
def add_cafe():
    try:

    
        new_cafe = Cafe (name = request.form['name'],
        map_url = request.form['map_url'],
        img_url = request.form['img_url'], 
        location = request.form['location'],
        seats = (request.form['seats']),
        has_toilet = bool(request.form['has_toilet']),
        has_wifi = bool(request.form['has_wifi']),
        has_sockets = bool(request.form['has_sockets']),
        can_take_calls = bool(request.form['can_take_calls']),
        coffee_price = request.form['coffee_price'],
        )
        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()
        return jsonify(response={'Success':'Your cafe was successfully added'})
    except:
        return jsonify(response={'Error':'Something went wrong'}), 400
# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods = ["GET","PATCH"])
def update_price(cafe_id):
    try:
        cafe_to_update = db.session.get(Cafe, cafe_id)
        cafe_to_update.coffee_price=request.form['coffee_price']
        db.session.commit()
        return jsonify(response={'Success':'The Price for Coffee was updated'})
    except:
        return jsonify(response={'Error':'ID not exists'}), 400
# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods =["DELETE"])
def report_closed(cafe_id):
    if request.form['api_key']=="TopSecretKey":
        cafe_to_delrte = db.session.get(Cafe, cafe_id)
        db.session.delete(cafe_to_delrte)
        db.session.commit()
        return jsonify(response={'Success':'The Cafe was deleted'})
    else:
        return  jsonify(response={'Error':'Wrong API_key'}), 400

if __name__ == '__main__':
    app.run(debug=True)
