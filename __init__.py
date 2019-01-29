from flask import Flask, render_template

app = Flask('ye olde shoppe')

import flask_intro.products.routes
import flask_intro.lists.routes

from . import db
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')
