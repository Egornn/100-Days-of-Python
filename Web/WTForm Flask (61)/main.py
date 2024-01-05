from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask import request
from flask_bootstrap import Bootstrap5


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = EmailField(label="Email:", validators =[DataRequired(message= "Field is required"), Email(message="Email should have a '@' and a '.'.")])
    password = PasswordField(label = 'Password:', validators =[DataRequired(message= "Field is required"), Length(min=8, message="Password has to be at least 8 symbols long.")])
    submit = SubmitField(label='Log in')




app = Flask(__name__)
app.secret_key = "secret_string"
bootstrap = Bootstrap5(app)



@app.route("/")
def home():
    form =MyForm()
    return render_template('index.html', form=form)

@app.route('/login', methods = ["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data=="12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = login_form)

if __name__ == '__main__':
    app.run(debug=True)
