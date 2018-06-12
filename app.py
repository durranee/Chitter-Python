import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify

# db configuration
DATABASE = 'pythonchitter.db'
DEBUG = True
SECRET_KEY = 'python'
USERNAME = 'admin'
PASSWORD = 'password'

# create and initialise app
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """CONNECTS TO DATABASE"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = open_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def open_db_connection():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__ == '__main__':
    init_db()
    app.run()
