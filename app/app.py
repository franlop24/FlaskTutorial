from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello, World</h1>"

@app.route('/about/')
def about():
    return '<h3>This is a Flask web Application.</h3>'

@app.route('/capitalize/<word>')
def capitalize(word):
    return f'<h1>{ escape(word.capitalize()) }</h1>'

@app.route('/add/<int:n1>/<int:n2>')
def add(n1, n2):
    return f"<h1>{ n1 + n2 }</h1>"

@app.route('/users/<int:user_id>')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return f"<h2>{ users[user_id] }</h2>"
    except Exception:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)