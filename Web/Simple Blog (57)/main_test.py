from flask import Flask
from flask import render_template 
from random import randint
import datetime
import requests

AGE_URL='https://api.agify.io'
SEX_URL="https://api.genderize.io"

app= Flask(__name__)

@app.route('/')
def main_page():
    rnd_num = randint(1,999)
    year = datetime.datetime.now().year
    # context = {"rnd_num":rnd_num}    
    return render_template("index_test.html",num=rnd_num,year=year)

@app.route('/guess/<name>/')
def guess(name):
    parameters  = {'name':name}
    age_response = requests.get(AGE_URL, params=parameters).json()
    age = age_response.get('age')
    sex_response = requests.get(SEX_URL, params=parameters).json()
    sex = sex_response.get('gender')
    probability = sex_response.get('probability')
    return render_template('guess_test.html', name=name, sex=sex, years=age, prob=probability)

@app.route('/blog/<int:id>')
def get_blog(id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    blog_json= requests.get(url=blog_url).json()
    return render_template('blog_test.html', posts = blog_json, id=id)

if __name__=='__main__':
    app.run(debug=True)
