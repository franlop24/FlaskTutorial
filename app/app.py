from flask import Flask, render_template, abort

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages/<int:idx>/')
def message(idx):
    app.logger.info('Building the messages list')
    messages = ['Message zero', 'Message one', 'Message two']
    try:
        app.logger.debug('Get message with index {}'.format(idx))
        return render_template('message.html', message=messages[idx])
    except Exception:
        app.logger.debug('Index {} is causing an IndexError'.format(idx))
        abort(404)

@app.route('/contact/')
def contact():
    return '<h1>Contact Page</h1>'

@app.route('/500/')
def error500():
    abort(500)

if __name__ == '__main__':
    app.run(debug=True)