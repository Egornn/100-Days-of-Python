from flask import Flask
from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 12
NUMBER_TO_GUESS = randint(LOWER_LIMIT, UPPER_LIMIT)
LINK_HTML = "<br>".join([f'<a href="/{num}">Guess number {num}</a>' for num in range(LOWER_LIMIT, UPPER_LIMIT + 1)])

app = Flask(__name__)

def guess_decorator(function):
    def some_wrapper():
        return function() + "<br>" + LINK_HTML
    return some_wrapper

@app.route("/")
@guess_decorator
def guessing_game():
    return f'<h1>Try to guess a number between {LOWER_LIMIT} and {UPPER_LIMIT}!</h1><br><img src= "https://media.giphy.com/media/3GRwYzxwdceaI/giphy-downsized-large.gif" width=200>'

def win_or_lose_decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) + "<br>" + LINK_HTML
    return wrapper

@app.route('/<int:number>')
@win_or_lose_decorator
def win_or_lose(number):
    if number > NUMBER_TO_GUESS:
        return f'<h1 style="color:red">Too High! Try again!</h1><br><img src= "https://media.giphy.com/media/gyRWkLSQVqlPi/giphy.gif" width=200><br>'
    elif number == NUMBER_TO_GUESS:
        return f'<h1 style="color:green">Congratulation!</h1><br><img src= "https://media.giphy.com/media/4Iw2OzgiiTc4M/giphy.gif" width=200>'
    else:
        return f'<h1 style="color:purple">Too Low! Try again!</h1><br><img src= "https://media.giphy.com/media/dRcMsUUrnR8He/giphy.gif" width=200>'

def make_bold(text):
    def bold():
        output= text() 
        return f'<b>{output}</b>'
    return bold

def make_italic(text):
    def bold():
        output= text() 
        return f'<em>{output}</em>'
    return bold

def make_underlined(text):
    def bold():
        output= text() 
        return f'<u>{output}</u>'
    return bold

@app.route('/bye')
@make_bold
@make_italic
@make_underlined
def bye():
    return '<h1> Bye! </h1>'

@app.route('/user/<path:name>/')
def hellO_user(name):
    return f'<h1>Hello, {name+"12"}!</h1>'

@app.route('/usernumber/<name>/<int:number>')
def hello_someone(name,number):
    return f'<h1 style= "text-align:center">Hello, {name}!'\
    f'</h1><p>Your number is {number}</p>'\
    '<img src= "https://media.giphy.com/media/3GRwYzxwdceaI/giphy-downsized-large.gif" width=200> <br>'\
    '<img src= "https://media.giphy.com/media/gyRWkLSQVqlPi/giphy.gif" width=200>'

class User:
    def __init__(self, name) -> None:
        self.name=name
        self.is_auth=False

def is_auth_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_auth:
            function(args[0])
    return wrapper_function

@is_auth_decorator            
def post(user):
    print(f'{user.name} posted a new article')

if __name__ == "__main__":
    username= User('Egor')
    post(username)
    username.is_auth=True
    post(username)

    app.run(debug=True)
