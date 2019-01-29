import sqlite3
import click
from flask import g, current_app
from flask.cli import with_appcontext
from flask_intro import app

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("shoppinglist")
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def query(query_string, args=(), one=False):
    db = get_db()
    cursor = db.execute(query_string, args)
    results = cursor.fetchall()
    db.commit()
    cursor.close()
    return (results[0] if results else None) if one else results
