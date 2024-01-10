from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os



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
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
def raiting_list(symbols):
    return  ['✘']+[symbols*i for i in range(1,6)]


class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe Name',validators =[DataRequired(message= "Field is required")])
    link = URLField(label = 'Location', validators =[DataRequired(message= "Field is required"), URL(message="URL is Required") ])
    open_time = StringField(label="Open from (eg 9:00AM)", validators =[DataRequired(message= "Field is Required")])
    close_time = StringField(label="Close at (eg 9:00PM)", validators =[DataRequired(message= "Field is Required")])
    coffee_raiting= SelectField(label='Coffee Raiting', validators =[DataRequired(message= "Field is Required")], choices=raiting_list('☕️'))
    wifi_raiting =SelectField(label='Wifi Power Raiting', validators =[DataRequired(message= "Field is Required")], choices=raiting_list("💪"))
    power_raiting =SelectField(label='Available Power Sockets', validators =[DataRequired(message= "Field is Required")], choices=raiting_list('🔌'))
    submit = SubmitField(label="Add entry")

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("web/coffee & wifi (62)/cafe-data.csv", mode='a', encoding='utf-8') as csv_file:
            new_line =[form.cafe_name.data, form.link.data, form.open_time.data, form.close_time.data, form.coffee_raiting.data,  form.wifi_raiting.data, form.power_raiting.data]
            csv_file.write("\n"+','.join(new_line))
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open("web/coffee & wifi (62)/cafe-data.csv", newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    
    app.run(debug=True)
