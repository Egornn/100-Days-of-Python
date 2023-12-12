from flask import Flask, render_template
from post import Post

app = Flask(__name__)
POSTED= Post()

@app.route('/')
def home():
    return render_template("index.html", blog = POSTED.blog_json)

@app.route('/blog/<int:id>')
def get_post(id):
    title = 'Error 404'
    subtitle = 'Not found'
    body = "Probably, you have a wrong id."
    for page in POSTED.blog_json:
        if page.get('id')==id:
            title = page.get('title')
            subtitle = page.get('subtitle')
            body = page.get('body')
            break
    return render_template('post.html', title=title, subtitle=subtitle, body=body)   
     
        
if __name__ == "__main__":
    app.run(debug=True)
