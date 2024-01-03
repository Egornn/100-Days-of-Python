from flask import Flask, render_template, url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/action_page', methods = ['POST', "GET"])
def action():
    if request.method == 'POST':
        name = request.form['username']
        password=  request.form['password']
        return render_template('action.html', name = name, password = password)


if __name__=='__main__':
    app.run(debug=True)