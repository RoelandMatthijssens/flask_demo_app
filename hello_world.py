from flask import Flask

app = Flask('some app name')

@app.route('/')
def hello():
    return 'sup brah'

@app.route('/second_route')
def second_route():
    return 'ya found me'
