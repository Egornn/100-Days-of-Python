from flask import Flask, render_template, url_for, request
from post import Post
from password import GOGGLE_PASS
import smtplib as smtplib
import datetime as dt
import random as rnd
import pandas as pd
import os
import time

MY_EMAIL = "egornnn@gmail.com"
RECEIVER = "egornnnn@gmail.com"
TEMPLATE_PATH = "templates/"


app = Flask(__name__)
POSTS = Post()

@app.route('/')
def home():
    return render_template( "index.html", blog = POSTS.blog_json)

@app.route('/index.html')
def index():
    
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

def send_data(form):
    message = f"Name: {form['name']}\nEmail: {form['email']}\nPhone: {form['phone']}\nMessage: {form['message']}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, GOGGLE_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,                            msg=message)
    return



@app.route('/contact', methods = ["GET", "POST"])
def contact():
    if request.method =="POST":
        send_data(request.form)
        return render_template("contact.html", message= "Thank you for you message!")
    
    return render_template("contact.html")
        


        
if __name__ == "__main__":
    app.run(debug=True)
    