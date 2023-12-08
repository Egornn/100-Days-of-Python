from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/bye')
def bye():
    return '<h1> Bye! </h1>'

@app.route('/user/<path:name>/')
def hellO_user(name):
    return f'<h1>Hello, {name+"12"}!</h1>'


@app.route('/usernumber/<name>/<int:number>')
def hello_someone(name,number):
    return f'<h1 style= "text-align:center">Hello, {name}!'\
    f'</h1><p>Your number is {number}</p>'\
    '<img src= https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juvenile_Ragdoll.jpg/220px-Juvenile_Ragdoll.jpg width=200>'


if __name__ == "__main__":
    app.run(debug=True)