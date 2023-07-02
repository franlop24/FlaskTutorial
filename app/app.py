import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.datetime.utcnow()
    return render_template('index.html', utc_dt=today)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comments = ['This is a first comment',
                'This is a second comment',
                'This is a third comment',
                'This is a fourth comment'
                ]
    return render_template('comments.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)